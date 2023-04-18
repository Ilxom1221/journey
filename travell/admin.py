from django.contrib import admin
from .models import Category, Product, Gallaery


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Product)
admin.site.register(Gallaery)