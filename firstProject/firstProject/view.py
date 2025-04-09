from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from channels.db import database_sync_to_async
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required

from django.shortcuts import render
from .models.Activity import Activity
from .views.ActivityForm import AnswerForm, ActivityForm

def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'activity_list.html', {'activities': activities})


def juego_escribir(request):
    return render(request, 'juego_escribir.html')


def activity_detail(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    
    if activity.name.lower() == "vocales":  # Cambié "abecedario" por "vocales"
        return render(request, 'vocales_game.html')
    elif activity.name.lower() == "juego_escribir":  # Corregido "else if" por "elif"
        return render(request, 'juego_escribir.html')
    
    return render(request, 'activity_detail.html', {'activity': activity})



def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('activity_list')  
    else:
        form = ActivityForm()
    return render(request, 'create_activity.html', {'form': form})


def count_game(request):
    return render(request, 'count_game.html')

def formar_palabra(request):
    return render(request, 'formar_palabra.html')


def juego_relacionar(request):
    actividades = Activity.objects.all().order_by('?')
    return render(request, 'relacionar_game.html', {'actividades': actividades})

