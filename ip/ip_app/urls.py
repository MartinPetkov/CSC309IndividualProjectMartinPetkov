from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from ip_app import views


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='signIn')),
    url(r'^signIn/$', views.signIn, name="signIn"),
    url(r'^signUp/$', views.signUp, name="signUp"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^ideasListing/$', views.ideasListing, name="ideasListing"),
    url(r'^userIdeas/$', views.userIdeas, name="userIdeas"),
    url(r'^ideaDetails/(?P<idea_id>\d+)/$', views.ideaDetails, name="ideaDetails"),
    url(r'^submitIdea/$', views.submitIdea, name="submitIdea"),
)
