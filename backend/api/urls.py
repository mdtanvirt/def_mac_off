from django.urls import path
from . import views

urlpatterns = [
    path('products', views.product_list, name='product'),
    path('product/<int:pk>', views.product_details, name='product_details'),
    path('orders/', views.order_list, name='orders')
]
