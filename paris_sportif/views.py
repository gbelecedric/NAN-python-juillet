from .models import *
from django.core.paginator import Paginator

from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
import requests
from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect
import datetime



from django.conf import settings



from django.contrib.auth import logout

def logout_views(request):
    logout(request)
    return render(request, 'form.html',)




def index(request):
    template_name="index.html"
    user = request.user

    m = match.objects.all()
    paginator = Paginator(m, 3)
    page = request.GET.get('page')
    me=paginator.get_page(page)




    context = {

               'match': m,
               'p':me,
               }



    return render(request, template_name, context)

    return render(request,template_name)
def post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwprd_confirme = request.POST.get('password_confirme')
        solde = request.POST.get('solde')
        solde="1000"
        user = User.objects.filter(username=username)
        if (username or email or password or passwprd_confirme) == "":
            message_error = "veuillez remplir tous les champs!!!!"
            template_name = "form.html"
            return render(request, template_name, {'error': message_error})
        elif password != passwprd_confirme:
            message_error = "veuillez entrer le meme password"
            template_name = "form.html"
            return render(request, template_name, {'error': message_error})
        elif user:
            message_error = "Pseudo deja utiliser essayer un autre svp"
            template_name = "form.html"
            return render(request, template_name, {'error': message_error})
        else:
            user = User.objects.create_user(username=username, last_name=str(solde), password=password,email=email)
            user.save()
            return HttpResponseRedirect('login/')
    template_name = "form.html"
    return render(request, template_name)






def my_bet(request):
    if not request.user.is_authenticated:
        access = "PETIT VISIEUX"

        return render(request, 'form.html', {'access': access})
    else:


        user = request.user
        users = int(user.last_name)



    template_name = "my_bet.html"
    return render(request,template_name,{'session':user,'session_solde':users})

def auth(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:



            login(request, user)

            return HttpResponseRedirect('account/')
        else:
            message_error="Username ou  Password incoorect"
            template_name = "login.html"
            return render(request, template_name, {'error': message_error})




    template_name = "login.html"

    """user=User.objects.all()
    print(user)"""
    return render(request,template_name)
def scores(request):
    template_name = "resultat.html"
    return render(request,template_name)
def depot_post(request):
    template_name = "depot.html"
    return render(request,template_name)
def retrait_post(request):
    if not request.user.is_authenticated:
        access = "PETIT VISIEUX"

        return render(request, 'form.html', {'access': access})
    else:
        user = request.user

        m = match.objects.all()


        users = int(user.last_name)

        context = {'session': user,
               'session_solde': users,
               'match': m
                   }

    template_name = "retrait.html"
    return render(request,template_name,context)

def connecting(request):
    if not request.user.is_authenticated:
        access="acces restrint aux connectés"

        return render(request, 'form.html',{'access':access})
    else:


        user=request.user



        m = match.objects.all()
        users = int(user.last_name)

        context = {'session': user,
               'session_solde': users,
               'match': m

               }
    template_name = "my_count.html"
    return render(request,template_name,context)



"""
# Create your views here.
#ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://api.ipstack.com/"160.154.136.86"?access_key=edb006c51301d91450fe20236357e019')
    geodata = response.json()

    if request.method =="POST":

        first_name = request.POST['nom']
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwprd_confirm = request.POST['password_confirm']
        user=User.objects.filter(username=username)
        if (username or first_name or password or passwprd_confirm )=="":
            message_error="veuillez remplir tous les champs!!!!"
            template_name = "form.html"
            return render(request, template_name, {'error': message_error})
        elif password != passwprd_confirm:
            message_error="veuillez entrer le meme password"
            template_name = "form.html"
            return render(request, template_name, {'error': message_error})
        elif user:
            message_error="Pseudo deja utiliser"
            template_name = "form.html"
            return render(request, template_name, {'error': message_error})
        else:

def post(request):

            user = User.objects.create_user(username=username, first_name=first_name,password=password)
            user.save()


            return HttpResponseRedirect( 'login/')
    template_name = "form.html"
    return render(request, template_name,{'ip': geodata['ip'],
        'ville': geodata['city'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],})
"""