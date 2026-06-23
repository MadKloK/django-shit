from django.contrib import admin
from app1.models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['subject', 'name', 'email']
    list_filter = ['email']
    search_fields = ['name', 'message']
