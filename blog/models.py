from django.utils import timezone 
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    slug = models.SlugField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_created',)

    def comment_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content


