from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Register
from .models import Task

admin.site.register(Task)
admin.site.register(Register,UserAdmin)

# Register your models here.
