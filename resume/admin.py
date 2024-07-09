from django.contrib import admin

# Register your models here.
from resume .models import About, HomeInfo

admin.site.register(About)
admin.site.register(HomeInfo)