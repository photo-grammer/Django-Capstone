from django.urls import path
from . import views

urlpatterns = [
    # Home page URL
    path('', views.home, name='home'),

    # About page URL
    path('about/', views.about, name='about'),

    # Leadership page URL
    path('leadership/', views.leadership, name='leadership'),

    # User registration URL
    path('register/', views.register, name='register'),

    # User login URL
    path('login/', views.login_view, name='login'),

    # Blogs URL
    path('blogs/', views.blogs, name='blogs'),

    # User login URL (alternate)
    path('accounts/login/', views.login_view, name='login'),
]
