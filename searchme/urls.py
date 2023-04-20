"""searchme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('register/',views.register,name='register'),
    path('login_in/',views.login_in,name='login_in'),
    path('logout_call/',views.logout_call,name='logout_call'),
    path('search1/',views.search1,name='search1'),
    path('links/',include('links.urls')),
    path('pdfs/',include('pdfs.urls')),
    path('videos/',include('videos.urls')),
    path('gsearch/',views.gsearch,name='gsearch'),
    path('myadmin/',views.myadmin,name='myadmin'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('userhome/',views.userhome,name='userhome'),
    path('recent/',views.recent,name='recent'),
    path('clear/',views.clear,name='clear'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
