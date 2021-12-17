from django.conf.urls import include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from testDB import views as v1
from LOGIN import views as loginVIEW
from USERVIEW import views as userVIEW
from REPORTS import views as reportVIEW
from ADMINVIEW import views as adminVIEW
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
import RESEARCH_RESOURCE_PORTAL.settings as settings

urlpatterns = [
    # ADMIN paths included
    path('admin/', admin.site.urls),
    path('', loginVIEW.home, name=""),

    # LOGIN paths included
    path('home/', loginVIEW.home, name="home"),
    path('generic-resources-list-view/', loginVIEW.resources,
         name="generic-resources-list-view"),
    path('signin/', loginVIEW.signin, name="signin"),
    path('signup/', loginVIEW.signup, name="signup"),
    path('services/', loginVIEW.services, name="services"),
    path('logout/', loginVIEW.logout, name="logout"),

    # USERVIEW paths included
    path('user/', include('USERVIEW.urls')),

    # ADMINVIEW app paths
    path('issue-resource/', adminVIEW.issueResource, name="issue-resource"),
    path('borrowed-resources/', adminVIEW.borrowedResources,
         name="borrowed-resources"),
     path('return-resource/', adminVIEW.returnResource, name="return-resource"),

    # REPORT app paths
    path('downloadLogs', reportVIEW.downloadLogs, name="downloadLogs")

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
