from django.contrib import admin

# Register your models here.
from .models import Employee,Cities
admin.site.register(Employee)
admin.site.register(Cities)
