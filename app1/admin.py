from django.contrib import admin
from app1.models import Contact, Newsletter

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['subject', 'name', 'email']
    list_filter = ['email']
    search_fields = ['name', 'message']

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['__str__']
