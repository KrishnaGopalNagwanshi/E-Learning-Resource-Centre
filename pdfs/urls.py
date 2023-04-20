from django.urls import path,include
from . import views

app_name = 'pdfs'
urlpatterns = [
   
    path('',views.pdfs_index),
    path('searchpdf/',views.searchpdf,name='searchpdf'),
    path('addpdf/',views.addpdf,name='addpdf'),
    

    
]