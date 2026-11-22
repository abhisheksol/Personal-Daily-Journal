from django.db import models

# Create your models here.

# abstract usermodel

from django.contrib.auth.models import AbstractUser



class UserModel(AbstractUser):

    dob = models.DateField(
        null=True,
        blank=True,
        db_column='date_of_birth',
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
        db_column='profile_picture',
    )

    class Meta:
        db_table = 'user_model'

    
