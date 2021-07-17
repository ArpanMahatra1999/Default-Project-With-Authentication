from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    mobile_number = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return str(self.user)

