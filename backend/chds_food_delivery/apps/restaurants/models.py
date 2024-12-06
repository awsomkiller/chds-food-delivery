from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class PickupLocation(models.Model):
    name = models.CharField(_("Pickup Location Name") ,max_length=255)
    code = models.UUIDField(_("Pickup Location Code"),max_length=50, unique=True)
    street_address1 = models.CharField(_("Street Address"),max_length=255)
    street_address2 = models.CharField(_("Street Address"),max_length=255)
    city = models.CharField(_("City"),max_length=100,)
    state = models.CharField(_("State"),max_length=100)
    postal_code = models.CharField(_("Postal Code"),max_length=20,null=True,blank=True)
    price = models.DecimalField(_("Pickup charges"),decimal_places=2,max_digits=5,help_text='Price in  Australian dollars',null=True)
   
    def __str__(self):
        return f"{self.name} ({self.code}) "
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = uuid.uuid4()  
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name ="PickupLocation"
        verbose_name_plural ="PickupLocations"


class MenuItemTags(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = "Item Tag"
        verbose_name_plural = "Item Tags"
    def __str__(self):
        return self.name
    

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Menu Category"
        verbose_name_plural = "Menu Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(_("Menu Item Name"),max_length=100)
    price = models.CharField(_("Menu Item Price"),max_length=50, help_text="Price in  Australian dollars")
    description = models.TextField(blank=True, null=True)
    calories = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    carbs = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    category = models.ManyToManyField(MenuCategory, verbose_name=_("Categories"))
    tags = models.ManyToManyField(MenuItemTags, verbose_name=_("Tags"))
    is_popular = models.BooleanField(default=False)
    is_best_selling= models.BooleanField(default=False)
    trans_code = models.CharField(_("Translation Code"), max_length=255, blank=True, null=True)
    trans_desc_code = models.CharField(_("Translation Description Code"), max_length=255,  blank=True, null=True)

    class Meta:
        verbose_name = "Menu Dish"
        verbose_name_plural = "Menu Dishes"
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

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
        verbose_name = "Menu Dish Image"
        verbose_name_plural = "Menu Dishes Images"
        ordering = ['-is_main'] 

    def __str__(self):
        return f"Image for {self.menu_item.name} ({'Main' if self.is_main else 'Additional'})"


class TimeSlots(models.Model):
    DELIVERY_CHOICES =[
        ('ALL', 'All'),
        ('DELIVERY ONLY','Delivery Only'),
        ('PICKUP ONLY', 'Pickup Only')
    ]
    name = models.CharField(_("Name"),max_length=50, null=True)
    type = models.CharField(_("Type"),max_length=50,choices=DELIVERY_CHOICES,null=True)
    
    class Meta:
        verbose_name ="Time Slot"
        verbose_name_plural = "Time Slots"
        
    def __str__(self):
        return f"{self.name} - {self.type}"
        
        
class PortionSize(models.Model):
    name = models.CharField(_("Portion Size"),max_length=50)
    code = models.CharField(_("Portion Code"), max_length=50, blank=True, null=True)
    weight = models.CharField(_("Portion Weight"),max_length=50, help_text="Weight in grams")
    addons = models.ManyToManyField("restaurants.Addons", verbose_name=_("Any Addons"), blank=True)
    
    class Meta:
        verbose_name = "Portion Size"
        verbose_name_plural = "Portion Sizes"
        ordering = ['weight']
        
    def __str__(self):
        return f"{self.name} - {self.weight}"
    

class MenuPortionPriceList(models.Model):
    menu_item = models.ForeignKey(MenuItem, verbose_name=_("Menu Item"), on_delete=models.CASCADE,related_name="menu_items_prices")
    portion_item = models.ForeignKey(PortionSize, verbose_name=_("Portion Item"), on_delete=models.CASCADE,related_name="portion_size_prices")
    price = models.CharField(_("Portion Price"),max_length=50, help_text="Price in  Australian dollars")
    calories = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    carbs = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    
    class Meta:
        verbose_name = "Price List"
        verbose_name_plural = "Price Lists"
        ordering = ['id']
        
    def __str__(self):
        return f"{self.menu_item.name} - {self.portion_item.name} - {self.price}"
    
    
class Addons(models.Model):
    name = models.CharField(_("Addon Name"),max_length=50)
    price = models.CharField(_("Addon Price"),max_length=50, help_text="Price in  Australian dollars")

    class Meta:
        verbose_name = "Menu Dishes Addon"
        verbose_name_plural = "Menu Dishes Addons"
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name} - {self.price}"
    

class WorkingDays(models.Model):
    date = models.DateField(_("Date"),null=True)
    time_slot = models.ManyToManyField(TimeSlots,verbose_name=_("Time Slot"),related_name="working_days")
    is_active = models.BooleanField(_("Is Active"),default=True)

    class Meta:
        verbose_name = "Kitchen Open Day"
        verbose_name_plural = "Kitchen Open Days"


class DeliveryPoint(models.Model):
    name  = models.CharField(_("Delivery location name"), max_length=100,null=True, blank=True)
    price = models.DecimalField(_("Delivery Charges"),decimal_places=2,max_digits=5, help_text="Price in  Australian dollars")
    postal_code = models.CharField(_("Postal Code"),max_length=20,null=True,blank=True)
    
    
    class Meta:
        verbose_name = "Delivery Point"
        verbose_name_plural = "Delivery Points"
    
    def __str__(self):
        return f"{self.name} - {self.price}"
    