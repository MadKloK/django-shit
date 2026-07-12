from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from app2.models import Post, Category, Comment

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Post)
class App2Admin(SummernoteModelAdmin):
    date_hierarchy = 'published_at'
    empty_value_display = 'this is empty'
    # fields = ['title', 'status']
    list_display = ['__str__', 'author', 'status', 'login_required', 'created_at', 'updated_at']
    list_filter = ['status', 'author', 'created_at']
    search_fields = ['title', 'content']
    ordering = ['created_at']
    summernote_fields = ['content']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    # fields = ['title', 'status']
    list_display = ['__str__', 'approved', 'created_at', 'updated_at']
    list_filter = ['approved', 'created_at']
    search_fields = ['name', 'message']
    ordering = ['-created_at']