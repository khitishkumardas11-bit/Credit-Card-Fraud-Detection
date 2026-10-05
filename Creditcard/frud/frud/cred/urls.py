from django.urls import path
from . import views

urlpatterns=[
   
    path('',views.home),
    path('cfrud/',views.cfrud),
    path('predict/',views.predict, name="predict"),
]

    
