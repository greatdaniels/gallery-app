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

        self.new_location = Location(location_name = 'Nakuru')
        self.new_location.save()

        self.new_category = Category(name = 'Business')
        self.new_category.save()

        self.new_image= Image(img_name = 'img1',img_description = 'Testing',editor = self.james, category = self.new_category, location = self.new_location)
        self.new_image.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_method(self):
        self.new_image.save_image()
        photos = Image.objects.all()
        self.assertTrue(len(photos) > 0)

    def test_get_image_by_id(self):
        self.new_image.save_image()
        photo = Image.get_image_by_id(self.new_image.id)
        self.assertNotEqual(self.new_image, photo)

    def test_search_image_by_category(self):
        photos = Image.search_by_category("Business")
        self.assertTrue(len(photos) > 0)

    def tearDown(self):
        Editor.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

class LocationTestClass(TestCase):
    '''
    Test case for the Location class and it's behaviours.
    '''

    # Set up method
    def setUp(self):
        '''
        Method that will run before any test case under this class
        '''
        self.new_location = Location(location_name = "Nairobi")

    def tearDown(self):
        Location.objects.all().delete()

    # Testing instance
    def test_instance(self):
        '''
        Test to confirm that the object is being instantiated correctly.
        '''
        self.assertTrue(isinstance(self.new_location, Location))


    # Testing save method
    def test_save_method(self):
        '''
        Method to check whether the locations are getting saved.
        '''
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class categoryTestClass(TestCase):
    '''
    A class that tests the category model behaviour
    '''
    def setUp(self):
        '''
        Creating a new instance
        '''
        self.category = Category(name = 'food')
        self.category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))


    def test_save_method(self):
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)