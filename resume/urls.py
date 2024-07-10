from django.urls import path
from . import views

app_name = "resume"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("experience/", views.experience, name="experience"),
    path("certificates/", views.certificates, name="certificates"),
    path("contact/", views.contact, name="contact"),
    path("resume/", views.resume, name="resume"),
    path("aboutproject<int:project_id>/", views.aboutproject, name="aboutproject"),
]
