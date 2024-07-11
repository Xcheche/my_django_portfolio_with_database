from django.db import models

# Create your models here.


class HomeInfo(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Home Info"

    def __str__(self):
        return self.title


class About(models.Model):
    about = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.about


class Projects(models.Model):
    title = models.CharField(max_length=100)
    decription = models.TextField(blank=True)
    project_photo = models.ImageField(upload_to="images/projects_img")
    project_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projects"


class Experience(models.Model):
    Company = models.CharField(max_length=100, blank=True, default="ok")
    Position = models.CharField(max_length=100, blank=True, default="ok")
    Duration = models.CharField(max_length=100, blank=True, default="ok")

    def __str__(self):
        return self.Company

    class Meta:
        verbose_name_plural = "Experience"

class Certificates(models.Model):
    title = models.CharField(max_length=100)
    certificate_id = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Certificates"
        
