from django.db import models
from django.utils.translation import gettext_lazy as _

class Restaurant(models.Model):
    STATUS_CHOICES = [
        ('ON', 'On'),
        ('OFF', 'Off'),
    ]

    name = models.CharField(_("Resturant Name") ,max_length=255)
    location = models.CharField(_("Resturant Location"),max_length=255)
    code = models.CharField(_("Resturant Code"),max_length=50, unique=True)
    from_time = models.TimeField(_("Opening Time"))
    to_time = models.TimeField(_("Closing Time"))
    status = models.CharField(_("Resturant Status"),max_length=3, choices=STATUS_CHOICES, default='OFF')
    phone_number = models.CharField(_("Contact Number"),max_length=15)

    def __str__(self):
        return f"{self.name} ({self.code}) - {self.status}"

    def is_open(self, current_time):
        """Check if the restaurant is open at the given time."""
        return self.status == 'ON' and self.from_time <= current_time <= self.to_time
    
    class Meta:
        verbose_name ="Restaurant"
        verbose_name_plural ="Restaurants"


class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Menu Category"
        verbose_name_plural = "Menu Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    calories = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    carbs = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    category = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, related_name='menu_items'
    )

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.category.name}"

    def get_caloric_breakdown(self):
        """Returns the caloric breakdown as a percentage of total calories."""
        total_calories = self.calories
        if total_calories > 0:
            protein_calories = self.protein * 4
            fat_calories = self.fats * 9
            carb_calories = self.carbs * 4
            return {
                "Protein (%)": round((protein_calories / total_calories) * 100, 2),
                "Fats (%)": round((fat_calories / total_calories) * 100, 2),
                "Carbs (%)": round((carb_calories / total_calories) * 100, 2),
            }
        return {"Protein (%)": 0, "Fats (%)": 0, "Carbs (%)": 0}


from django.db import models

class MenuImage(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='menu_images/')
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Menu Image"
        verbose_name_plural = "Menu Images"
        ordering = ['-is_main'] 

    def __str__(self):
        return f"Image for {self.menu_item.name} ({'Main' if self.is_main else 'Additional'})"
