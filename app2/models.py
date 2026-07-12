from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='app2/', default='app2/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # foreign key created indexes by default ! + id creates it too
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    views_count = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_required = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    published_at = models.DateTimeField(null=True, db_index=True)

    class Meta:
        ordering = ['-created_at']
        # verbose_name = 'pppost'
        # verbose_name_plural = 'postssss'

        # -----
        # its good to have a ['published_at', 'status'] index as we query those a lot !
        # -----

    def __str__(self):
        return f"{self.id}. {self.title}"

    def get_absolute_url(self):
        return reverse('app2:single', kwargs={'pid': self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} -> {self.subject}'
