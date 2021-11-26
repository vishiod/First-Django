from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shop home"),

    path('about/', views.about_us, name="About Us"),
    path('contact/', views.contact_us, name="Contact Us"),
    path('tracker/', views.tracker, name="Tracker"),
    path('search/', views.search, name="Search"),
    path('product/<int:this_id>', views.product_view, name="Product"),
    path('checkout/', views.checkout, name="Checkout"),
    path('test/', views.test, name="Test"),
]

