from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid
from django.db import transaction


class UserMangaer(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email=None,mobile_number=None, password=None, **extra_fields):
        if not email:
            raise ValueError("The email field must be required")
        email = self.normalize_email(email) if email else None
        user = self.model(email=email,  mobile_number=mobile_number,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    """
        Custom User Model
    """
    full_name = models.CharField(_("User Full Name"), max_length=30,null=True,blank=True)
    email = models.EmailField(_("User Email"), unique=True,null=True,blank=True)
    mobile_number = models.CharField(_("User Mobile Number"),max_length=13,unique=True,null=True,blank=True)
    created_at = models.DateTimeField(_("User Creation Date&Time"),auto_now_add=True)
    is_active = models.BooleanField(_("User Active"), default=True)
    is_staff = models.BooleanField(_("Is Staff"), default=False)
    is_superuser = models.BooleanField(_("Is Superuser"), default=False)
    
    objects = UserMangaer()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=[]
    
    class Meta:
        ordering = ['id']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self)-> str:
        return f"{self.email}"
    
    def save(self, *args, **kwargs):
    
        if not self.email and not self.mobile_number:
            raise ValueError("The user must have either an email or a mobile number.")
        super().save(*args, **kwargs)
        
        

class UserAddress(models.Model):
    """ 
        Model for storing User Address
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    name = models.CharField(_("Name"), max_length=50,null=True,blank=True)
    street_address1 = models.CharField(_("Street Address1"),max_length=255,null=True,blank=True)
    street_address2 = models.CharField(_("Street Address2"),max_length=255,null=True,blank=True)
    suburbs = models.CharField(_("Suburbs"),max_length=255,null=True,blank=True)
    city = models.CharField(_("City"),max_length=100, null=True,blank=True)
    state = models.CharField(_("State"),max_length=100,null=True,blank=True)
    postal_code = models.CharField(_("Postal Code"),max_length=20,null=True,blank=True)
    is_primary = models.BooleanField(_("Primary Address"),default=False)
    is_billing = models.BooleanField(_("Billing"),default=False)
    created_at = models.DateTimeField(_("Created"),auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"),auto_now=True)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            
            primary_address_exists = UserAddress.objects.filter(user=self.user, is_primary=True).exists()
            if self.is_primary or not primary_address_exists:
                UserAddress.objects.filter(user=self.user, is_primary=True).update(is_primary=False)
                self.is_primary = True
                
            billing_address_exists = UserAddress.objects.filter(user=self.user, is_billing=True).exists()
            if self.is_billing or not billing_address_exists:
                UserAddress.objects.filter(user=self.user, is_billing=True).update(is_billing=False)
                self.is_billing = True
         
            super().save(*args, **kwargs)
                
    class Meta:
        ordering = ['id']
        verbose_name = 'User Address'
        verbose_name_plural = 'User Addresses'
        

    def __str__(self)-> str:
        return f"{self.street_address1}, {self.city}, {self.state}, - {self.postal_code}"
    
    
class UserProfile(models.Model):
    """ 
        Model for storing user  extra data
    """
    user_image = models.ImageField(_("User Image") , upload_to="user_images",null=True,blank=True)
    date_of_birth = models.DateField(_("User Date of birth"),null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
    
    
class UserCardDetails(models.Model):
    """ 
        Model for storing User Card Details 
    """
    PREFERRED_PAYMENT_CHOICES = [
        ('cards', 'Cards'),
        ('alipay', 'Alipay'),
        ('wechat', 'WeChat'),
        ('paypal', 'PayPal'),
        ('wallet', 'Wallet'),
    ]
    card_number = models.CharField(_("Card Number"),max_length=16, unique=True)
    card_fullname = models.CharField(_("Card Holder Name"),max_length=100)
    card_cvv = models.CharField(_("Card cvv number"),max_length=4)
    card_expiry = models.DateField(_("Card Expiry Date"),max_length=8)
    preferred_payment = models.CharField(_("Payment Method"),max_length=10,choices=PREFERRED_PAYMENT_CHOICES,default='cards')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_cards')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Payment Card"
        verbose_name_plural = "Payment Cards"
        ordering = ['-card_expiry']  
        unique_together = ('card_number', 'user')
        
    def __str__(self):
        return f"{self.card_fullname}"
    

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    balance = models.FloatField(_("Wallet Balance"),default=0.0)
    expiry = models.DateTimeField(_("Wallet Expire"),null=True,blank=True)
    unique_id = models.UUIDField(_("Unique Wallet ID"), editable=False, unique=True,null=True,blank=True)
    
    def __str__(self):
        return f"Wallet of {self.user.full_name} - Balance: {self.balance}"
    
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = uuid.uuid4()
        super().save(*args, **kwargs)
            
    class Meta:
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"
        

class EmailToken(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="email_user",
        blank=True,
        null=True,
    )
    email_token = models.CharField(max_length=50)


class ContactUs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(_("Email"))
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    
