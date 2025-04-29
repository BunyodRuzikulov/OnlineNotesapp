"""
URL configuration for yozuvlar project.

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
from notes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth/', views.auth_view, name='auth'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_note, name='create_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('view/<int:note_id>/', views.view_note, name='view_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('categories/', views.categories, name='categories'),
    path('delete_folder/<int:folder_id>/', views.delete_folder, name='delete_folder'),
    path('assign_note/<int:note_id>/<int:folder_id>/', views.assign_note_to_folder, name='assign_note'),
    path('archive/', views.archive, name='archive'),
    path('restore/<int:note_id>/', views.restore_note, name='restore_note'),
    path('delete_permanently/<int:note_id>/', views.delete_permanently, name='delete_permanently'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)