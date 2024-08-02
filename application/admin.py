from django.contrib import admin
from .models import Post, Order, OrderItem, Buyurtma, Product

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'about')
    search_fields = ('title', 'about')

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'created', 'total_price')
#     search_fields = ('id',) 
# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('order', 'post', 'quantity', 'price')
#     search_fields = ('order', 'post')

@admin.register(Buyurtma)
class BuyurtmaAdmin(admin.ModelAdmin):
    list_display = ('ism', 'telefon', 'manzil', 'umumiy_narx', 'mahsulotlar','tolov','dostavka')
    search_fields = ('ism', 'telefon')

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'buyurtma')
#     search_fields = ('name',) 
