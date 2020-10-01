from django.conf.urls import url
from demoapp import views
from django.urls import path

app_name = "demoapp"

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('others/', views.others, name = 'others'),
    path('registration/', views.registration, name= 'registration'),
    path('user_login/', views.user_login, name = 'user_login'), 
]