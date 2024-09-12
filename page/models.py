from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')
    short_description = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Home(models.Model):
    bio_text = models.TextField()

    def __str__(self):
        return "Home Page"

