from django.db import models
from sorl.thumbnail import ImageField
class Post(models.Model):
    text = models.CharField( max_length=150, blank=False,null=False)
    image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.text
# Create your models here.
