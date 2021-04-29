from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserModel(AbstractUser):
    avatar=models.ImageField(upload_to='avatar')
    
    
    class Meta:
        db_table="User"
        
    def __str__(self):
        return self.username

