from django.conf.urls import patterns, url
from PwdManager import views

urlpatterns = [
    url(r'^signup/',views.signup,name='signup'),
    url(r'^login/',views.login,name='login'),
    url(r'^accounts/',views.accounts,name='accounts'),
    url(r'^updateaccounts/',views.updateaccounts,name='accounts'),
]
