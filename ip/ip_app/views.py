from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext, loader
from django.contrib import messages

import logging
import hashlib
import re

from ip_app.models import *


def signIn(req):
    if req.method == 'POST':
        # Login logic goes here
        user_email = req.POST.get('email')
        user_password_hash = hashlib.sha224(req.POST.get('password')).hexdigest()

        if validateCredentials(user_email, user_password_hash):
            req.session['logged_in_user_id'] = User.objects.get(email=user_email).user_id
            return redirect('ip_app:ideasListing', permanent=True)
        else:
            return render(req, 'ip_app/sign_in.html', {'invalid_credentials': True})
    else:
        return render(req, 'ip_app/sign_in.html')


def signUp(req):
    if req.method == 'POST':
        # Sign Up logic goes here
        user_email = req.POST.get('email')
        user_password_hash = hashlib.sha224(req.POST.get('password')).hexdigest()
        user_first_name = req.POST.get('first_name')
        user_last_name = req.POST.get('last_name')

        if(userExists(user_email)):
            return render(req, 'ip_app/sign_up.html', {'user_exists': True})
        else:
            u = User(email=user_email, password=user_password_hash, first_name=user_first_name, last_name=user_last_name)
            u.save()
            messages.success(req, 'Account created!')
            return redirect('ip_app:signIn', permanent=True)

    else:
        return render(req, 'ip_app/sign_up.html')



def logout(req):
    # Logout logic goes here
    return HttpResponseRedirect('/ip_app/')

def userExists(email):
    return User.objects.filter(email=email).count() > 0

def validateCredentials(email, password_hash):
    return User.objects.filter(email=email, password=password_hash).count() > 0


def ideasListing(req):
    response = {}

    all_ideas = Idea.objects.order_by('title')
    results = [idea for idea in all_ideas]
    response['results'] = results
    response['message'] = 'Successfully retrieved ideas listing'

    return render(req, 'ip_app/ideas_listing.html', {'all_ideas': all_ideas})


def userIdeas(req):
    # Get user ideas here
    logged_in_user_id = req.session.get('logged_in_user_id')
    user_ideas = Idea.objects.filter(submittor_id=logged_in_user_id).order_by('title')
    return render(req, 'ip_app/user_ideas.html', {'user_ideas': user_ideas})


def ideaDetails(req, idea_id):
    idea = Idea.objects.filter(idea_id=idea_id)
    return render(req, 'ip_app/idea_details.html', {'idea': idea[0]})


def submitIdea(req):
    if req.method == 'POST':
        # Logic for submitting an idea goes here
        idea_submittor_id = req.session.get('logged_in_user_id')
        idea_submittor = User.objects.get(user_id=idea_submittor_id)

        idea_title = req.POST.get('title')
        idea_industry = req.POST.get('industry')
        idea_description = req.POST.get('description')
        idea_keywords = re.sub(' *, *', ',', req.POST.get('keywords')).strip(',')
        idea_rating = 0

        if not idea_submittor_id \
            or not idea_title \
            or not idea_industry \
            or not idea_description \
            or not idea_keywords:

            return render(req, 'ip_app/submit_idea.html', {'field_missing': True})
        else:
            idea = Idea(submittor_id=idea_submittor, title=idea_title, industry=idea_industry, description=idea_description, keywords=idea_keywords, rating=idea_rating)
            idea.save()

            return render(req, 'ip_app/submit_idea.html', {'success_submit': True})

    else:
        return render(req, 'ip_app/submit_idea.html')


def likeIdea(req, idea_id):
    logged_in_user_id = req.session.get('logged_in_user_id')
    return HttpResponse("gooby pls")
