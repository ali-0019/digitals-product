from django.contrib import admin

from .models import Category, File, Product 
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent','title','is_enable','created_time']
    list_filter = ['is_enable', 'parent']
    search_fields = ['title']
    
    
class FileInLineAdmin(admin.StackedInline):
    model = File
    fields = ['title','file_type','file','is_enable']
    extre = 0
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','is_enable','created_time']
    list_filter = ['is_enable']
    search_fields = ['title']
    inlines = [FileInLineAdmin]
    filter_horizontal = ['Categories']