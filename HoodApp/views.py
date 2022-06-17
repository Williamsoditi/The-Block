import profile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, Http404
from . models import *
from django.contrib.auth.models import User



# Create your views here.
@csrf_exempt
def index(request):    
    current_user = request.user
    # profile.user = current_user

    return render(request,'home.html')
