from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('gallery',views.gallery,name='gallery'),
    path('register',views.register,name='register'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)