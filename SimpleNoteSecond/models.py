from django.db import models

class SimpleNoteSecond(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=100)
    date_created = models.IntegerField()


    def __str__(self):
        return self.title
