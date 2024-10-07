from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Musicien, Album, Single, Event, Testimonial, NewsletterSubscriber, ContactInfo

def home(request):
    # Récupérer les 10 premiers musiciens
    musicien = Musicien.objects.all()[:10] 
    context = {
        'artist': musicien
    }
    return render(request, 'index.html', context)

def albums(request):
    # Récupérer tous les albums pour l'affichage
    albums_list = Album.objects.all()
    context = {
        'albums': albums_list
    }
    return render(request, 'albums-store.html', context)

def events(request):
    if request.method == 'POST':
        email = request.POST.get('newsletter_email')
        if email.is_valid():
            # Ajouter à la liste des abonnés à la newsletter
            
            NewsletterSubscriber.objects.get_or_create(email=email)

            # Envoi d'un e-mail de confirmation
            subject = "🎉 Bienvenue dans la famille Yoka !"
    
            # HTML content for the email
            html_message = render_to_string('newsletter_email.html', {'email': email})
            
            send_mail(
                subject,
                '',  
                settings.DEFAULT_FROM_EMAIL,
                [email],
                html_message=html_message,
            )
            return redirect('home')  # Redirige vers la page d'accueil
        else:
            return redirect('home')

    testimonials = Testimonial.objects.all()
    event_list = Event.objects.all()
    context = {
        'event_list': event_list,
        'testimonials': testimonials
    }
    return render(request, 'event.html', context)

def blog(request):
    return render(request, 'blog.html')

def formulaire(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('mail')
        message = request.POST.get('message')

        if name and email and message:
            # Créer le sujet et le message HTML
            subject = f'🎉 Merci de votre message, {name} !'
            html_message = render_to_string('confirmation_email.html', {
                'name': name,
                'message': message,
            })

            # Envoi de l'e-mail de confirmation
            send_mail(
                subject,
                '',  # Laissez ce champ vide car nous utilisons un message HTML
                settings.DEFAULT_FROM_EMAIL,
                [email],
                html_message=html_message,
            )
            return HttpResponse('ok')
        else:
            return redirect('home')

def contact(request):
    # Récupérer les informations de contact
    contact_info = ContactInfo.objects.all()
    context = {
        'info': contact_info,
    }
    return render(request, 'contact.html', context)

def elements(request):
    return render(request, 'elements.html')

def login(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('mail')
        if password and email:
            print(f'Email: {email}, Password: {password}')  # Pour le débogage

    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def music(request):
    # Récupérer tous les singles pour l'affichage
    singles_list = Single.objects.all()
    context = {
        'singles': singles_list
    }
    return render(request, 'music.html', context)
