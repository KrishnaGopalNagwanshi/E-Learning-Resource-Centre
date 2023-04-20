from django.urls import path,include
from . import views

app_name = "pdfs"
urlpatterns = [
   
    path('',views.videos_index),
    path('searchvideos/',views.searchvideos,name='searchvideos'),
    path('addvideo/',views.addvideo,name='addvideo'),

    
]