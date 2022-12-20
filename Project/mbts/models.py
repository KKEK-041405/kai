from django.db import models
from sorl.thumbnail import ImageField
from mysite import settings

class Post(models.Model):
    pinno = models.CharField( max_length=12, blank=False,null=True)
    image = models.ImageField((""), upload_to=settings.MEDIA_ROOT, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.pinno