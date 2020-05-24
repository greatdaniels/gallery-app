from django.test import TestCase
from .models import Editor, Category, Location

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
