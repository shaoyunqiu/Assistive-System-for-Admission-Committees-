from django.contrib import admin

# Register your models here.
import models
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.Volunteer)
admin.site.register(models.RegisterCode)
admin.site.register(models.Picture)
admin.site.register(models.Notice)
admin.site.register(models.Group)
admin.site.register(models.Timer)
admin.site.register(models.WechatURL)



