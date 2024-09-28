"""
URL configuration for hms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log, name='login'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('logout/', views.lout, name='logout'),
    path('food/', views.food, name='food'),
    path('foodetail/<int:pk>', views.foodetail, name='foodetail'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('show_cart/', views.show_cart, name='show_cart'),
    path('plus_cart/', views.plus_cart, name='plus_cart'),
    path('minus_cart/', views.minus_cart, name='minus_cart'),
    path('remove_cart', views.remove_cart, name='remove_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('order/', views.order, name='order'),
    path('delete_order/<id>/', views.delete_order, name='delete_order'),
    path('delivery_boy_signup', views.delivery_boy_signup,name='delivery_boy_signup'),
    path('delivery_boy_login', views.delivery_boy_login, name='delivery_boy_login'),
    path('delivery_home_page', views.delivery_home_page, name='delivery_home_page'),

    # Password reset urls
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="password_reset.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"), name='password_reset_complete'),
]
