from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'content', 'created_at', 'updated_at']
    list_display_links = ['title']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']

    
admin.site.register(Article, ArticleAdmin)