from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('about',views.home1),
    path('vision',views.abd),
    path('program',views.abe),

]