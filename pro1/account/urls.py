from django.urls import path
from . import views

app_name = 'account'

urlpatterns=[
    path('',views.user_register,name='user_register'),
]