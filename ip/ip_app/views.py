from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext, loader

from ip_app.models import *


def signIn(req):
    return render(req, 'ip_app/sign_in.html')

def signUp(req):
    return render(req, 'ip_app/sign_up.html')

def login(req):
    # Login logic goes here
    return render(req, 'ip_app/ideas_listing.html')

def logout(req):
    # Logout logic goes here
    return HttpResponseRedirect('/ip_app/')

def validateCredentials(username, password_hash):
    return True


def ideasListing(req):
    response = {}

    all_ideas = Idea.objects.order_by('title')
    results = [idea for idea in all_ideas]
    response['results'] = results
    response['message'] = 'Successfully retrieved ideas listing'

    return render(req, 'ip_app/ideas_listing.html', {'all_ideas': all_ideas})


def userIdeas(req):
    # Get user ideas here
    # user_id = get from sessin? idk
    user_ideas = Idea.objects.filter(submittor_id=1).order_by('title')
    return render(req, 'ip_app/user_ideas.html', {'user_ideas': user_ideas})


def ideaDetails(req, idea_id):
    idea = Idea.objects.filter(idea_id=idea_id)
    return render(req, 'ip_app/idea_details.html', {'idea': idea[0]})


def submitIdea(req):
    return render(req, 'ip_app/submit_idea.html')
