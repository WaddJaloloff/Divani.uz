from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:post_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('remove_from_cart/<int:post_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('order/', views.order, name='order'),
    path('place_order/', views.place_order, name='place_order'),
]