from django.test import TestCase
from .models import Editor, Category, Location, Image

# Create your tests here.
class EditorTestClass(TestCase):
    def setUp(self):
        self.james = Editor(editor_name = 'James', email = 'james@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.james = Editor(editor_name = 'James', email = 'james@gmail.com')
        self.james.save_editor()

        self.new_location = Location(name = 'Nakuru')
        self.new_location.save()

        self.new_category = Category(name = 'Business')
        self.new_category.save()

        self.new_image= Image(img_name = 'img1',img_description = 'Testing',editor = self.james, category = self.new_category, location = self.new_location)
        self.new_image.save()

    # def test_instance(self):
    #     self.assertTrue(isinstance(self.new_image, Image))

    # def test_save_method(self):
    #     self.new_image.save_photo()
    #     photos = Image.objects.all()
    #     self.assertTrue(len(photos) > 0)

    def tearDown(self):
        Editor.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()