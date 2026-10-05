from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cfrud/', views.cfrud, name='cfrud'),
    path('predict/', views.predict, name='predict'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

    
