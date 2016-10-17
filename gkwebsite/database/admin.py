from django.contrib import admin

# Register your models here.
import models
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.Volunteer)
admin.site.register(models.RegisterCode)
