from django.db import models

# Create your models here.
class Editor(models.model):
    editor_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.editor_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['editor_name']