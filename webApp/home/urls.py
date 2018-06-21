from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    # /home/
    url(r'^$', views.home, name='home'),

    # /home/logedin/
    url(r'^logedin/$', views.logedin, name='logedin'),

    # /home/contactus/
    url(r'^contactus/$', views.contactus, name='contactus'),

    # /home/about/
    url(r'^about/$', views.about, name='about'),

    # /home/logedin/ADDMissing
    url(r'^logedin/addmissing/$', views.mprofilecreate, name='addMissing'),

    # /home/logedin/ADDFound
    url(r'^logedin/addfound/$', views.fprofilecreate, name='addFound'),

    # /home/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /home/login/
    url(r'^login/$', views.log_in, name='login'),

    # /home/logedin/MissingProfiles/
    url(r'^logedin/missingprofiles/$', views.MissingProfiles, name='MissingProfiles'),

    # /home/logedin/FoundProfiles/
    url(r'^logedin/foundprofiles/$', views.FoundProfiles, name='FoundProfiles'),

    # /home/MissingProfiles/MissingPerson_ID/
    # MissingPerson_ID --> pk
    url(r'^logedin/missingprofiles/(?P<pk>[0-9]+)/$', views.missingDetails, name='missingDetails'),

    # /home/foundProfiles/FoundPerson_ID/
    # FoundPerson_ID --> pk
    url(r'^logedin/foundprofiles/(?P<pk>[0-9]+)/$', views.foundDetails, name='foundDetails'),
]
