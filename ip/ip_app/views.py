from django.shortcuts import render
from django.http import HttpResponse


def signIn(req):
    return HttpResponse("Sign in page")

def signUp(req):
    return HttpResponse("Sign up page")

def validateCredentials(username, password_hash):
    return True


def ideasListing(req):
    return HttpResponse("Ideas listing page")

def userIdeas(req):
    return HttpResponse("User-submitted ideas")

def ideaDetails(req):
    return HttpResponse("Idea details page")

def submitIdea(req):
    return HttpResponse("Submit idea page")
