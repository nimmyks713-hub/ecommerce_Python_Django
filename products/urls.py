from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns=[
    path("signup/",views.signup,name='signup'),
    path("login/",auth_views.LoginView.as_view(template_name='products/login.html'),name='login'),
    path("",views.productlist,name="productlist"),
    path("<int:product_id>/", views.productdetail, name="productdetail"),
    path("aboutus/",views.aboutus,name='aboutus'),
    path("contactus/",views.contactus,name="contactus"),
]