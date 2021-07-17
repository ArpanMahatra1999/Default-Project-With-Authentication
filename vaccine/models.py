from django.db import models


# Create your models here.
class Vaccine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    side_effects = models.TextField(blank=True, null=True)
    before_care = models.TextField(blank=True, null=True)
    after_care = models.TextField(blank=True, null=True)
    protect_against = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Dose(models.Model):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    first_day_from_birth = models.PositiveIntegerField()
    last_day_from_birth = models.PositiveIntegerField()
    booster = models.BooleanField(default=False)

    def __str__(self):
        return str(self.vaccine) + " dose " + str(self.number)
