from django.urls import path
from . import views
# matcher empty route
urlpatterns = [
    path('', views.home, name='blog-home'),      
    path('about/', views.about, name='blog-about'),      
]