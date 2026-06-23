from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image
    # author
    # tag
    # category
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
