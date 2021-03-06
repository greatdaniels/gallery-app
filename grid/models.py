from django.db import models

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

    def save_category(self):
        '''
        Method to save the category name
        '''
        return self.save()

class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        '''
        A method that saves the location name
        '''
        return self.save()

class Image(models.Model):
    img_name = models.CharField(max_length= 30)
    img_description = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    img = models.ImageField(upload_to = 'images/', default = '')

    def save_image(self):
        return self.save()

    def delete_image(self):
        self.delete() 

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        '''
        A method to get a photo bases on the id
        '''
        return cls.objects.filter(id = id).all()

    @classmethod
    def search_by_category(cls,search):
        images = Image.objects.filter(category__name__icontains=search)
        return images

    