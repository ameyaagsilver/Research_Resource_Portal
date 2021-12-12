"""RESEARCH_RESOURCE_PORTAL URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from testDB import views as v1
from LOGIN import views as v2
from USERVIEW import views as v3
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
# from RESEARCH_RESOURCE_PORTAL import settings
import RESEARCH_RESOURCE_PORTAL.settings as settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.insertRecord),
    path('home/', v2.home, name="home"),
    path('books-media-list-view/', v3.resources, name="books-media-list-view"),
    path('signin/', v2.signin, name="signin"),
    path('signup/', v2.signup, name="signup"),
    path('services/', v2.services, name="services"),
    path('logout/', v2.logout, name="logout"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
