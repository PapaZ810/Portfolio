from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='', default='zoe.jpg')
    short_description = models.CharField(max_length=100, default='Short description')
    text = models.TextField()

    def __str__(self):
        return self.title


class Home(models.Model):
    bioText = models.TextField()

    def __str__(self):
        return "Home Page"

