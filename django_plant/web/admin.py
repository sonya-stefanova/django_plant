from django.contrib import admin
from django_plant.web.models import Profile, Plant


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
   pass

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
   pass
