from django.urls import path
from . import views

urlpatterns = [
    # Path for user registration (to be filled later)
    path('register/', views.register, name='register'),

    # Path for user login (to be filled later)
    path('login/', views.user_login, name='login'),

    # Path for user logout (to be filled later)
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
]

