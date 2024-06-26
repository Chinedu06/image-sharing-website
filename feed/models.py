from django.db import models


from sorl.thumbnail import ImageField

# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length = 140, blank = False, null = False)
    image = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.text