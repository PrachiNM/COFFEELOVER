from django.urls import path
from . import views

urlpatterns=[
    path("signup", views.signup, name="signup"),
    path("thankyou", views.thankyou, name="thankyou"),
    path("login", views.login, name='login'),
    path('register_user', views.register_user, name='register_user')
]