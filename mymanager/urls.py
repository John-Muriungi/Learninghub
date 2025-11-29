"""
URL configuration for learninghub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from mymanager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('trainers/', views.trainers, name='trainers'),
    path('courses/', views.courses, name='courses'),
    path('announcements/', views.announcements, name='announcements'),
    path('add_trainer/', views.add_trainer, name='add_trainer'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_announcement/', views.add_announcement, name='add_announcement'),
    path('delete_announcement/<int:id>/',
         views.delete_announcement, name='delete_announcement'),
    path('delete_trainer/<int:id>/', views.delete_trainer, name='delete_trainer'),
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),
]
