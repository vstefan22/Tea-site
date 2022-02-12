from multiprocessing import context
from optparse import Option
import queue
from django.urls import reverse
from django.shortcuts import redirect, render
from . models import Caj
from django.conf import settings
from django.core.mail import send_mail
from .forms import CheckBox




# Create your views here.
def index(request):
    cajevi = Caj.objects.order_by('date_added')
    context = {'cajevi':cajevi}
    return render(request, 'Cajevi/index.html', context)

def meni(request):
    cajevi = Caj.objects.order_by('date_added')
    context = {'cajevi':cajevi}
    return render(request, 'Cajevi/meni.html', context)

def caj(request, pk):
    caj = Caj.objects.get(id=pk)
    x=caj.date_added
    y=x.strftime('%d-%m-%Y')
    date=y
    context = {'caj': caj, 'date':date}
    return render(request, 'Cajevi/caj.html', context)

def search(request):
    if request.method == "GET":
        search = request.GET.get('search')
        cajevi = Caj.objects.all().filter(name=search)
        context = {'cajevi': cajevi}
        return render(request, 'Cajevi/search.html', context)

def o_nama(request):
    return render(request, 'Cajevi/onama.html')

def informacije(request):
    return render(request, 'Cajevi/informacije.html')

def narudzba(request):
    cajevi = ['Nana', 'Kamilica', 'Herbal']
    # Geting users opitions
    if request.method == 'POST':
        naruceni = []
        cajevi_s = request.POST.getlist('cajevi')
        if cajevi_s==['Nana']:
            naruceni.append(cajevi_s)
        if cajevi_s==['Kamilica']:
            naruceni.append(cajevi_s)
        if cajevi_s==['Herbal']:
            naruceni.append(cajevi_s)
        if cajevi_s==['Nana', 'Herbal']:
            naruceni.append(cajevi_s)
        if cajevi_s==['Kamilica', 'Herbal']:
            naruceni.append(cajevi_s)
        if cajevi_s==['Kamilica', 'Nana']:
            naruceni.append(cajevi_s)
        if cajevi_s==['Kamilica', 'Nana', 'Herbal']:
            naruceni.append(cajevi_s)

        # Send mail 

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        adresa = request.POST['adresa'] 
        grad = request.POST['grad'] 
        postanski_broj = request.POST['postanski-broj']
        str_naruceni = str(naruceni)

        send_mail(
           
            'NOVA NARUDZBA CAJA!', # Subject
            name + ' je narucio/la caj na adresu: ' + adresa + '.' 
             '\nPoslato sa: ' + email +
             '\nBroj telefona: ' + phone + 
             '\nGrad: ' + grad + 
             '\nPostanski broj: ' + postanski_broj +
             '\nNaruceni cajevi su: ' + str_naruceni,
            
          
            # Message
            email, # From email
            ['stefwolf22@gmail.com'], # To email
        )
    return render(request, 'Cajevi/narudzba.html')


# Error handeling 
'''def error_404(request, exception):
    return render(request, 'Cajevi/404.html')

def error_500(request):
    return render(request, 'Cajevi/500.html')

def error_400(request, exception):
    return render(request, 'Cajevi/400.html')
    '''

