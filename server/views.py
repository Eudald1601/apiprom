from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily

from django.views.decorators.csrf import csrf_exempt
from .utils import JsonCollector
from .models import Querys
import json

peticions = []
# Create your views here.
def home(request):
    query = Querys.objects.all()
    if request.method == 'POST':
        username = request.POST["Username"]
        passwd = request.POST["Password"]
        user = authenticate(request, username= username, password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Loggeado correctamente")
            return render(request, 'home.html', {'username':username})
        else:
            messages.error(request, "Error al loggearse")
            return redirect('home')
    
    return render(request, 'home.html', {'query':query}{'username':username})

@csrf_exempt
def prometheus_server(request):
    
    if request.method == 'POST':
        print("Rebo datos -> ", len(peticions))
        try:
            start_http_server(8004, '0.0.0.0.')
            print("Primera entrada executo el servidor")
            dato = request.body
            print(dato)
        except Exception as err:
            print("Entrades posteriors")
            dato = request.body
            print(dato)
        dato_json = json.loads(dato.decode("utf-8"))
        dato_collect = JsonCollector.JsonCollector(dato_json)
        if len(peticions) == 0:
            REGISTRY.register(dato_collect)
            peticions.append(dato_collect)
            print("Primera entrada =" , len(peticions))
        else:
            print("Entrada num = ", len(peticions))
            
            for p in peticions:
                print(p)
            dato_ante = peticions[len(peticions)-1]
            REGISTRY.unregister(dato_ante)
            REGISTRY.register(dato_collect)
            peticions.append(dato_collect)

    return redirect('home')


def logout_user(request):
    logout(request)
    messages.success(request, "Te has deloggeado")
    return redirect('home')

##def index(request):
##   return render(request, 'index.html')