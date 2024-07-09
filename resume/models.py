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
