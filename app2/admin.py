from django.contrib import admin
from app2.models import Post

# Register your models here.

@admin.register(Post)
class App2Admin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    empty_value_display = 'this is empty'
    # fields = ['title', 'status']
    list_display = ['__str__', 'author', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'author', 'created_at']
    search_fields = ['title', 'content']
    ordering = ['created_at']
