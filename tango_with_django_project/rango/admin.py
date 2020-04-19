from django.contrib import admin
from .models import Category, Page, UserProfile

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    
admin.site.register(Category, CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    prepopulated_fileds = {'slug' : ('title',)}
    
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
