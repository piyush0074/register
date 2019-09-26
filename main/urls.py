"""log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
#from django.conf.urls import patterns, include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings


from django.contrib.auth.views import LoginView




#app_name='main'

urlpatterns = [
	path("register/",views.register, name="register here"),
	path("",views.home,name="home"),
	path("accounts/profile/",views.home),
	path("home/",views.home,name="home"),
	path('security/', include('django_mfa.urls')),
	path('setting/',views.setting,name='setting'),

	path('tinymce/', include('tinymce.urls')),
	path("login/",views.login,name="main page"),
	
	path("logout/",views.logout_user,name="log out"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
