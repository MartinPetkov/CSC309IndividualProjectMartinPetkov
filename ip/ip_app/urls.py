from django.conf.urls import patterns, url

from ip_app import views


urlpatterns = patterns('',
    url(r'^$', views.signIn, name="signIn"),
    url(r'^signIn/$', views.signIn, name="signIn"),
    url(r'^signUp/$', views.signUp, name="signUp"),
    url(r'^ideasListing/$', views.ideasListing, name="ideasListing"),
    url(r'^userIdeas/$', views.userIdeas, name="userIdeas"),
    url(r'^ideaDetails/$', views.ideaDetails, name="ideaDetails"),
    url(r'^submitIdea/$', views.submitIdea, name="submitIdea"),
)
