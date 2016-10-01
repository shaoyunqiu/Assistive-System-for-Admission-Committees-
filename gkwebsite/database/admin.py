from django.contrib import admin

# Register your models here.

from database import models
admin.site.register(models.Student)