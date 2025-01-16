from django.contrib import admin
from django.utils.html import mark_safe
from rangefilter.filters import DateRangeFilter
from django.utils.html import format_html
from .models import Orders
import json

class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'user_full_name',
        'order_time',
        'schedule_date',
        'time_slot',
        'order_type',
        'status',
        'formatted_menu_items',
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
        #   ('Order details', {
        #     'fields': (
        #         'order_id',
        #         'pickup_location',
        #         'user_full_name',
        #         'order_time',
        #         'schedule_date',
        #         'time_slot',
        #         'order_type',
        #         'delivery_location',
        #         'formatted_menu_items',
        #         'notes',
        #         'transaction_id',
        #         'amount',
        #         'shipping_charges',
        #         'total_price',
        #         'status',
        #     ),
        # }),

    )

    def user_full_name(self, obj):
        return obj.user.full_name if obj.user else "N/A"
    user_full_name.short_description = "User Full Name"

    def transaction_id(self, obj):
        return obj.transaction.transaction_id if obj.transaction else "N/A"
    transaction_id.short_description = "Transaction ID"

    # Custom method to format menu items
    def formatted_menu_items(self, obj):
        menu_items = obj.menu_item

        # Initialize menu_items as a list
        if isinstance(menu_items, str):
            try:
                menu_items = json.loads(menu_items)
            except json.JSONDecodeError:
                # logger.error(f"Invalid JSON in menu_item for Order ID {obj.order_id}")
                return "Invalid menu items data."

        if isinstance(menu_items, dict):
            menu_items = [menu_items]  # Ensure it's a list

        if not isinstance(menu_items, list):
            return "No menu items available."

        html = '<div style="padding: 5px;">'
        for item in menu_items:
            if not isinstance(item, dict):
                continue  # Skip invalid items

            meal_name = item.get("meal_name", "")
            portion_name = item.get("selected_meal_portion_name", "")
            portion_price = item.get("selected_meal_portion_price", "")
            addons = item.get("addons", [])
            quantity = item.get("quantity", 1)
            total_price = item.get("total_price", "")

            # Start with meal name in bold
            html += f'<p><strong>{meal_name}</strong></p>'

            # Portion details
            portion_details = f'Portion: {portion_name} (${portion_price})'

            # Addons details
            if addons and isinstance(addons, list):
                addon_names = ", ".join([addon.get("name", "") for addon in addons if isinstance(addon, dict)])
                addon_prices = ", ".join([f'${addon.get("price", "")}' for addon in addons if isinstance(addon, dict)])
                if addon_names and addon_prices:
                    portion_details += f' | Addons: {addon_names} ({addon_prices})'

            # Quantity and total price
            portion_details += f' | Quantity: {quantity} | Total: ${total_price}'

            # Add to HTML
            html += f'<p>{portion_details}</p>'
        html += '</div>'
        return format_html(html)
    formatted_menu_items.short_description = 'Menu Items (Formatted)'

admin.site.register(Orders, OrdersAdmin)
