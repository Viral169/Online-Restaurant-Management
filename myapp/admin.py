from django.contrib import admin
from myapp.models import Category, profile, Food, Cart, OrderDetail, Delivery_boy_profile, Delivery_order


class user(admin.ModelAdmin):
    list_display = ['id', 'user', 'mobile']


class food_display(admin.ModelAdmin):
    list_display = ['id', 'food_name', 'food_category']


class cart_display(admin.ModelAdmin):
    list_display = [ 'id','email', 'food', 'image', 'quantity', 'price']


class order_display(admin.ModelAdmin):
    list_display = ['id', 'user', 'food_name', 'image','qty', 'price', 'status', 'ordered_date']


class D_boy_profile(admin.ModelAdmin):
    list_display = ['id', 'user', 'mobile']

# Register your models here.


admin.site.site_header = "Marigold Resturent & Banquet | Admin"
admin.site.register(profile, user)
admin.site.register(Category)
admin.site.register(Food, food_display)
admin.site.register(Cart, cart_display)
admin.site.register(OrderDetail,order_display)
admin.site.register(Delivery_boy_profile, D_boy_profile)
admin.site.register(Delivery_order)
