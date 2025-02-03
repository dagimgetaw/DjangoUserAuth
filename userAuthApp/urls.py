from django.urls import path
from .views import home, register, user_login, user_logout

urlpatterns = [
    path('', home, name='home'),  # FIXED: Removed leading '/'
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
]
