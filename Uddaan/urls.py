"""Uddaan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('a_home',views.a_home,name='a_home'),
    path('student',views.s_list,name='student'),
    path('institute',views.i_list,name='student'),
    path('notice',views.notice,name='notice'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('i_login',views.i_login,name='i_login'),
    path('i_logout',views.i_logout,name='i_logout'),
    path('a_login',views.a_login,name='a_login'),
    path('a_logout',views.a_logout,name='a_logout'),
    path('p_details',views.personal_details,name='p_details'),
    path('c_details',views.communication_details,name='c_details'),
    path('e_details',views.education_details,name='e_details'),
    path('u_document',views.document_upload,name='u_document'),
    path('i_details',views.institute_details,name='i_details'),
    path('i_document',views.i_document_upload,name='i_document'),
    path('profile',views.profile,name='profile'),
    path('i_profile',views.i_profile,name='i_profile'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('council',views.council,name='council'),
    path('marks',views.marks,name='marks')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
