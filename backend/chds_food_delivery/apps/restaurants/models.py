from django.db import models
from django.utils.translation import gettext_lazy as _

class PickupLocation(models.Model):
    
    name = models.CharField(_("Pickup Location Name") ,max_length=255)
    code = models.UUIDField(_("Pickup Location Code"),max_length=50, unique=True)
    street_address1 = models.CharField(_("Street Address"),max_length=255)
    street_address2 = models.CharField(_("Street Address"),max_length=255)
    city = models.CharField(_("City"),max_length=100,)
    state = models.CharField(_("State"),max_length=100)
    postal_code = models.CharField(_("Postal Code"),max_length=20,null=True,blank=True)
   

    def __str__(self):
        return f"{self.name} ({self.code}) "
    
    def save(self):...
      
    
    class Meta:
        verbose_name ="PickupLocation"
        verbose_name_plural ="PickupLocations"


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
    price = models.DecimalField(
        max_digits=8, decimal_places=2, default=0.00, help_text="Price in US dollars"
    )
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


class TimeSlots(models.Model):
    pass