from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
import os

# Create your models here.
class Product(models.Model):
    Title = models.CharField(max_length=250)
    Slug = models.SlugField(unique=True)

    Prix1 = models.CharField(max_length=100, blank=True, null=True)
    Prix2 = models.CharField(max_length=100, blank=True, null=True)

    os_choice = (
                ('PLAYSTATION', 'PLAYSTATION'),
                ('NINTENDO', 'NINTENDO'),
                ('XBOX', 'XBOX'),
                ('FIGURINE', 'FIGURINE'),
                ('EXPOSITION', 'EXPOSITION'),
                ('ENCHER', 'ENCHER'),
    )
    Category = MultiSelectField(choices=os_choice)

    Description = RichTextField(blank=True, null=True)

    Img = models.ImageField(upload_to='pics')

    Img1 = models.ImageField(upload_to='pics', blank=True, null=True)
    Img2 = models.ImageField(upload_to='pics', blank=True, null=True)
    Img3 = models.ImageField(upload_to='pics', blank=True, null=True)

    def __str__(self):
        return self.Title

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Img = models.ImageField(upload_to='contactPics', blank=True, null=True)
    Message = models.TextField()

    def __str__(self):
        return self.Name

class News(models.Model):
    Title = models.CharField(max_length=250)
    Slug = models.SlugField(unique=True)

    Description = RichTextField(blank=True, null=True)

    link = models.URLField(max_length=200, blank=True, null=True)

    Img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Title

class Story(models.Model):
    Title = models.CharField(max_length=250)
    Img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Title