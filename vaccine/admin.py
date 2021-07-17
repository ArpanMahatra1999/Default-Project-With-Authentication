from django.contrib import admin

from vaccine.models import Vaccine, Dose

# Register your models here.
admin.site.register([Vaccine, Dose])
