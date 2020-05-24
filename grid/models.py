from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Editor(models.Model):
    editor_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.editor_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['editor_name']

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name 

class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name

class Image(models.Model):
    img = ImageField(blank=True, manual_crop="")
    img_name = models.CharField(max_length= 30)
    img_description = models.TextField()
    editor = models.ForeignKey(Editor)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete() 