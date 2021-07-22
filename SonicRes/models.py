from django.db import models

# Create your models here.

class testupload(models.Model):

    title = models.CharField(max_length=1000)
    shortUrl = models.URLField(max_length = 200)
    filex = models.FileField(upload_to ='test')

    def __str__(self):
        return str(self.filex)
