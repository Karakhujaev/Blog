from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title',  'category', 'date']
    search_fields = ['title', 'category']
    list_filter = ['title']

admin.site.register(Post, PostAdmin)

