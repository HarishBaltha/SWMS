"""SWMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from Sahara import views
from SWMS import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sing,name="sing"),
    path('ckick/',views.click,name="click"),
    path('company/',views.company,name="company"),
    path('awards/',views.awards,name="awards"),
    path('click1/',views.awards1,name="click1"),
    path('awards2/', views.awards2, name="awards2"),
    path('awards3/', views.awards3, name="awards3"),
    path('awards4/', views.awards4, name="awards4"),
    path('line/', views.line, name="line"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)