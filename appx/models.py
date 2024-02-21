from django.db import models
from autoslug import AutoSlugField


class blogx(models.Model):
    blog_id = models.IntegerField(primary_key=True, null=False)
    blog_name = models.CharField(max_length=100)
    blog_code = models.TextField(max_length=10000)
    blog_desc = models.TextField(max_length=10000)
    

    slugx = AutoSlugField(populate_from='blog_name',unique=True, null=True , default=None )

class comment(models.Model):
    cum_id = models.ForeignKey(blogx,on_delete=models.CASCADE)
    text = models.TextField(max_length=200)


