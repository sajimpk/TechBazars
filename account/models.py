from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile_otp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=4)
   

    def __str__(self):
        return self.user.username