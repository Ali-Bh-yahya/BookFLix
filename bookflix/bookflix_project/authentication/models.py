# Use Django’s Built-In User Model
from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User model extending AbstractUser
class User(AbstractUser):
   # i add this 2 fields to the user model because the first_name , last_name and email ....
   # is already in the AbstractUser model
   age = models.PositiveIntegerField(default=10)
   birthday = models.DateField()
   # and i don't need to hash password manually because AbstractUser already handles that





    