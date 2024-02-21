from django.contrib import admin
from django.urls import path
from appx.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('page/',page, name='page'),
    path('post/',post, name='post'),
    path('post/<slug:slug>',post, name='post'),
    path('register/',register_page, name='register_page'),
    path('login/',login_page , name='login_page'),
    path('logout/',logout_page , name='logout_page'),
    path('post_user/',post_user , name='post_user')
]
