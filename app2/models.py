from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}. {self.name}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='app2/', default='app2/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # tag
    category = models.ManyToManyField(Category)
    views_count = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ['created_at']
        # verbose_name = 'pppost'
        # verbose_name_plural = 'postssss'

    def __str__(self):
        return f"{self.id}. {self.title}"
