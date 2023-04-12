from django.db import models

# Create your models here.

class Tag(models.Model) :
    name = models.CharField(max_length=50)


class Post(models.Model) :
         title = models.CharField(max_length=100)
         content = models.TextField(blank=True)
         #post_image
         # autor
         tags = models.ManyToManyField(Tag blank=true)
