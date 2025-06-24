# Use Django’s Built-In User Model
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Custom User model extending AbstractUser
class User(AbstractUser):
   # i add this 2 fields to the user model because the first_name , last_name and email ....
   # is already in the AbstractUser model
   age = models.PositiveIntegerField(default=10)
   birthday = models.DateField()
   # and i don't need to hash password manually because AbstractUser already handles that

class Wallet(models.Model):
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   def __str__(self):
       return f"{self.user.first_name}'s Wallet - Balance: {self.balance}"
   
   @receiver(post_save , sender=settings.AUTH_USER_MODEL )
   def create_wallet_for_new_user(sender, instance , created , **kwargs):
         if created:
            Wallet.objects.create(user=instance)


    