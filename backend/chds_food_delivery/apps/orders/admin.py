from django.contrib import admin
from django.utils.html import format_html
from rangefilter.filters import DateRangeFilter
import json
import csv
from django.http import HttpResponse

from .models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'order_id',
        'schedule_date',
        'formatted_menu_items',
        'time_slot',
        'order_type',
        'status',
        'total_price'
    ]

    readonly_fields = [
        'order_id',
        'pickup_location',
        'user_full_name',
        'order_time',
        'schedule_date',
        'time_slot',
        'order_type',
        'delivery_location',
        'formatted_menu_items',
        'notes',
        'transaction_id',
        'amount',
        'shipping_charges',
        'total_price'
    ]

    search_fields = [
        'order_id',
        'user__full_name',
        'user__email',
        'user__mobile_number',
        'transaction__transaction_id'
    ]

    list_filter = [
        'order_type',
        ('schedule_date', DateRangeFilter),
        ('order_time', DateRangeFilter),
        'status',
        'time_slot'
    ]

    # Show up to 200 entries per page
    list_per_page = 200

    fieldsets = (
        ('Billing details', {
            'fields': (
                'order_id',
                'user_full_name',
                'order_time',
                'amount',
                'shipping_charges',
                'total_price',
                'status',
            ),
        }),
        ('Order details', {
            'fields': (
                'schedule_date',
                'time_slot',
                'order_type',
                'delivery_location',
                'pickup_location',
                'formatted_menu_items',
                'notes',
            ),
        }),
    )

    # -------------
    # CUSTOM FIELDS
    # -------------
    def user_full_name(self, obj):
        return obj.user.full_name if obj.user else "N/A"
    user_full_name.short_description = "User Full Name"

    def transaction_id(self, obj):
        return obj.transaction.transaction_id if obj.transaction else "N/A"
    transaction_id.short_description = "Transaction ID"

    # Custom method to format menu items
    def formatted_menu_items(self, obj):
        menu_items = obj.menu_item

        if isinstance(menu_items, str):
            try:
                menu_items = json.loads(menu_items)
            except json.JSONDecodeError:
                return "Invalid menu items data."

        if isinstance(menu_items, dict):
            menu_items = [menu_items]

        if not isinstance(menu_items, list):
            return "No menu items available."

        html = '<div style="padding: 5px;">'
        for index, item in enumerate(menu_items):
            if not isinstance(item, dict):
                continue

            meal_name = item.get("meal_name", "")
            portion_name = item.get("selected_meal_portion_name", "")
            portion_price = item.get("selected_meal_portion_price", "")
            addons = item.get("addons", [])
            quantity = item.get("quantity", 1)
            total_price = item.get("total_price", "")

            html += f'<p><strong>{index+1}. {meal_name}</strong></p>'

            portion_details = f'Portion: {portion_name} (${portion_price})'

            if addons and isinstance(addons, list):
                addon_names = ", ".join([addon.get("name", "") for addon in addons if isinstance(addon, dict)])
                addon_prices = ", ".join([f'${addon.get("price", "")}' for addon in addons if isinstance(addon, dict)])
                if addon_names and addon_prices:
                    portion_details += f' | Addons: {addon_names} ({addon_prices})'

            portion_details += f' | Quantity: {quantity} | Total: ${total_price}'
            html += f'<p>{portion_details}</p>'
        html += '</div>'
        return format_html(html)
    formatted_menu_items.short_description = 'Ordered Items'

    # -------------
    # HELPER METHOD
    # -------------
    def get_total_quantity(self, obj):
        """
        Returns the sum of quantities from the menu_item JSON.
        """
        menu_items = obj.menu_item

        if isinstance(menu_items, str):
            try:
                menu_items = json.loads(menu_items)
            except json.JSONDecodeError:
                return 0

        if isinstance(menu_items, dict):
            menu_items = [menu_items]

        if not isinstance(menu_items, list):
            return 0

        total_qty = 0
        for item in menu_items:
            if isinstance(item, dict):
                total_qty += int(item.get("quantity", 0))
        return total_qty

    # -------------
    # ADMIN ACTIONS
    # -------------
    def export_order_details_csv(self, request, queryset):
        """
        Export CSV: order_id, schedule_date, time_slot, formatted_menu_items, notes, order_type
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="order_details.csv"'

        writer = csv.writer(response)
        writer.writerow(["order_id", "schedule_date", "time_slot", "formatted_menu_items", "notes", "order_type"])

        for order in queryset:
            writer.writerow([
                order.order_id,
                order.schedule_date or "",
                order.time_slot or "",
                # Use the same logic from formatted_menu_items (but strip HTML if needed)
                # For simplicity, we'll export raw text
                self._menu_items_as_text(order),
                order.notes or "",
                order.order_type or ""
            ])

        return response
    export_order_details_csv.short_description = "Export Order Details CSV (filtered)"

    def export_address_details_csv(self, request, queryset):
        """
        Export CSV: order_id, schedule_date, time_slot, order_type, user.full_name, user.email,
                    user.mobile_number, total_quantity
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="address_details.csv"'

        writer = csv.writer(response)
        writer.writerow([
            "order_id", 
            "schedule_date", 
            "time_slot", 
            "order_type", 
            "user_full_name", 
            "user_email", 
            "user_mobile", 
            "total_quantity"
        ])

        for order in queryset:
            writer.writerow([
                order.order_id,
                order.schedule_date or "",
                order.time_slot or "",
                order.order_type or "",
                order.user.full_name if order.user else "",
                order.user.email if order.user else "",
                order.user.mobile_number if order.user else "",
                self.get_total_quantity(order)
            ])

        return response
    export_address_details_csv.short_description = "Export Address Details CSV (filtered)"

    def _menu_items_as_text(self, obj):
        """
        Helper to convert the JSON menu items to a simple text format (no HTML) 
        so it can be cleanly exported in CSV.
        """
        menu_items = obj.menu_item

        if isinstance(menu_items, str):
            try:
                menu_items = json.loads(menu_items)
            except json.JSONDecodeError:
                return "Invalid menu items data."

        if isinstance(menu_items, dict):
            menu_items = [menu_items]

        if not isinstance(menu_items, list):
            return "No menu items available."

        lines = []
        for index, item in enumerate(menu_items):
            if not isinstance(item, dict):
                continue
            meal_name = item.get("meal_name", "")
            portion_name = item.get("selected_meal_portion_name", "")
            portion_price = item.get("selected_meal_portion_price", "")
            addons = item.get("addons", [])
            quantity = item.get("quantity", 1)
            total_price = item.get("total_price", "")

            line = f"{index+1}. {meal_name}, Portion: {portion_name} (${portion_price}), "
            if addons and isinstance(addons, list):
                addon_names = ", ".join([addon.get("name", "") for addon in addons if isinstance(addon, dict)])
                addon_prices = ", ".join([f'${addon.get("price", "")}' for addon in addons if isinstance(addon, dict)])
                if addon_names and addon_prices:
                    line += f"Addons: {addon_names} ({addon_prices}), "

            line += f"Qty: {quantity}, Item Total: ${total_price}"
            lines.append(line)

        return " | ".join(lines)

    # Register the actions as admin actions (they will appear in the "Actions" dropdown)
    actions = ["export_order_details_csv", "export_address_details_csv"]

admin.site.register(Orders, OrdersAdmin)
