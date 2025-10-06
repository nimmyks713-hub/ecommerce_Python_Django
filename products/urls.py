from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns=[
    path("signup/",views.signup,name='signup'),
    path("login/",auth_views.LoginView.as_view(template_name='products/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path("",views.productlist,name="productlist"),
    path("<int:product_id>/", views.productdetail, name="productdetail"),
    path("aboutus/",views.aboutus,name='aboutus'),
    path("contactus/",views.contactus,name="contactus"),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
]