from django.conf.urls import patterns, include, url
from django.contrib import admin
from PwdManager import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pwdmanager/',include('PwdManager.urls')),
]
