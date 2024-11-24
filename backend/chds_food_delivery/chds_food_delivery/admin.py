from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = "Custom Admin"
    site_title = "Custom Admin Portal"
    index_title = "Welcome to the Custom Admin"

    def get_app_list(self, request):
        app_list = super().get_app_list(request)

        app_ordering = {
            "restaurants": [
                "Menu Categories",
                "Menu Dishes",
                "Menu Dishes Addons",
                "Menu Dishes Images",
                "PickupLocations",
                "Portion Sizes",
                "Price Lists",
                "Kitchen Open Days",
                "Time Slots",
            ],
        }

        for app in app_list:
            if app['app_label'] in app_ordering:
                custom_order = app_ordering[app['app_label']]
                app['models'].sort(
                    key=lambda model: custom_order.index(model['name'])
                    if model['name'] in custom_order
                    else len(custom_order)
                )

        return app_list


custom_admin = CustomAdminSite(name="custom_admin")