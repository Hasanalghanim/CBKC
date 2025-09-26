from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'fighter', 'fight_card', 'published_date')
    search_fields = ('title', 'excerpt')
    prepopulated_fields = {"slug": ("title",)}