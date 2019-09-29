from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('details/<int:product_id>/', views.details, name="details"),

    path('addProduct/', views.addProduct, name='addProduct'),
    path('deleteProduct/<int:product_id>/', views.deleteProduct, name='deleteProduct')
]