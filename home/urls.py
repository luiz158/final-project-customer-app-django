from django.urls import path
from .views import home, logout_f

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_f, name='logout')
]