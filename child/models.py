from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Child(models.Model):

    GENDERS = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDERS)
    place_of_birth = models.TextField()
    place_of_vaccination = models.TextField()
    parent = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


