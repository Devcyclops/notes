from django.db import models

# Create your models here.

class Note(models.Model):
    saved_note = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.note

