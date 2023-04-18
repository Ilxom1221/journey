from django.contrib import admin
from .models import Category, Product, Gallaery
from django.utils.safestring import mark_safe


# Register your models here.

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallaery
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    prepopulated_fields = {'slug': ('title',)}





@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'created_at', 'get_photo')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title',)
    inlines = [GalleryInline]

    def get_photo(self, obj):
        if obj.images:
            try:
                return mark_safe(f'<img src="{obj.images.all()[0]}" width="75">')
            except:
                return '-'
        else:
            return '-'

    get_photo.short_description = 'Изображение'


admin.site.register(Gallaery)