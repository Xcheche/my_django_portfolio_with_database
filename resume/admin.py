from django.contrib import admin

# Register your models here.
from resume.models import About, HomeInfo, Projects, Experience,Certificates

admin.site.register(About)
admin.site.register(HomeInfo)
admin.site.register(Projects)
admin.site.register(Experience)
admin.site.register(Certificates)

