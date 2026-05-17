from django.urls import path
from .views import register
from .views import login_view
from .views import dashboard
from .views import logout_view

urlpatterns = [
    
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),


]