from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from models import *

class MemberForm(forms.Form):
    email = forms.EmailField() 

def signup(request):
    form = MemberForm(request.POST)
    if not form.is_valid():
        return render_to_response('index.html', {'form': form, 'dude':'OMGOMGOMGOMOMGp'})
    email = form.cleaned_data['email']
    Member(email=email).save()
    return HttpResponseRedirect('/signup_thanks')

class PilotForm(forms.ModelForm):
    class Meta:
        model = PilotRecommendation

def pilot_recommendation(request):
    if request.method == 'GET':
        form = PilotForm()
        return render_to_response('pilot_recommendation.html', {'form': form})
    form = PilotForm(request.POST, request.FILES)
    if not form.is_valid():
        return render_to_response('pilot_recommendation.html', {'form': form})
    form.save()
    return HttpResponseRedirect('/pilot_recommend_thanks')
