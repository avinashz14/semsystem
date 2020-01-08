from django.urls import path
from . import views
from django.contrib.auth.views import LoginView , LogoutView

urlpatterns= [
    
    path('login/',  LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change_pass/', views.change_password, name='change_password'),
    
] 