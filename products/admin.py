from django.contrib import admin

from .models import Product
from .models import Comment
from .models import ProductImage
from .models import Category



class ProductsImageInline(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'date', 'category', 'author']
    inlines = [ProductsImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
admin.site.register(ProductImage)
admin.site.register(Category)