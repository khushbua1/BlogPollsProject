from django.contrib import admin
from .models import Post, Tag, Category

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug',)
	search_fields = ('title',)

admin.site.register(Post, PostAdmin)

class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug',)
	search_fields = ('name',)

admin.site.register(Tag, TagAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug',)
	search_fields = ('title',)

admin.site.register(Category, CategoryAdmin)