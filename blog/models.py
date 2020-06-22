from django.db import models


class BlogPage(models.Model):
    title = models.CharField(max_length=100)
    blog_title = models.CharField(max_length=450)
    blog_date = models.DateField()
    blog_description = models.TextField()


