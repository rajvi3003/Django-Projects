from django.db import models

# Create your models here.

class testupload(models.Model):

    filex = models.FileField(upload_to ='test')

    def __str__(self):
        return "hi"
