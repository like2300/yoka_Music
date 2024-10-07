from django.db import models
from django.utils import timezone

DEFAULT_MESSAGE = 'Musique disponible sur Yoka'
DEFAULT_TAILLE = 200
PATH_IMAGES = 'media/'

class Musicien(models.Model):
    nom = models.CharField(max_length=DEFAULT_TAILLE, default='Musicien disponible sur Yoka', blank=True)
    bio = models.TextField(default=DEFAULT_MESSAGE, blank=True)
    date_de_naissance = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to=f'{PATH_IMAGES}images_musiciens/', blank=True)

    def __str__(self):
        return self.nom

class SocialLink(models.Model):
    musician = models.ForeignKey(Musicien, related_name='social_links', on_delete=models.CASCADE)
    name = models.CharField(max_length=DEFAULT_TAILLE)
    url = models.URLField()

    def __str__(self):
        return f'{self.name} - {self.url}'

class ContactInfo(models.Model):
    local_address = models.CharField(max_length=DEFAULT_TAILLE, null=True, default='local')
    phone = models.CharField(max_length=DEFAULT_TAILLE, null=True, default='country number')
    mail = models.EmailField(max_length=DEFAULT_TAILLE, null=True, default='mail ...')  # Utiliser EmailField pour l'email
    social_contact = models.ForeignKey(SocialLink, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Yoka -- [info]'

class Album(models.Model):
    nom = models.CharField(max_length=DEFAULT_TAILLE, default='Album inconnu', blank=True)
    artiste = models.ForeignKey(Musicien, on_delete=models.CASCADE, related_name='albums')
    date_sortie = models.DateField(blank=True, null=True)
    cover = models.ImageField(upload_to=f'{PATH_IMAGES}images_album/', blank=True)
    description = models.TextField(default=DEFAULT_MESSAGE, blank=True)
    prix = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.nom} par {self.artiste}'

class Single(models.Model):
    titre = models.CharField(max_length=DEFAULT_TAILLE, default=DEFAULT_MESSAGE, blank=True)
    artiste = models.ForeignKey(Musicien, on_delete=models.CASCADE, related_name='singles')
    fichier_audio = models.FileField(upload_to=f'{PATH_IMAGES}audio_singles/', blank=True)
    date_sortie = models.DateField(blank=True, null=True)
    prix = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.titre} - {self.artiste}'

class Music(models.Model):
    titre = models.CharField(max_length=DEFAULT_TAILLE, default=DEFAULT_MESSAGE, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musics', null=True)
    musicien = models.ForeignKey(Musicien, on_delete=models.CASCADE, blank=True, null=True)
    fichier_audio = models.FileField(upload_to=f'{PATH_IMAGES}audio_musiciens/', blank=True)
    transcription = models.TextField(default=DEFAULT_MESSAGE, blank=True)
    date_publication = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return f'[{self.titre}] - {self.musicien}'

class Event(models.Model):
    nom = models.CharField(max_length=DEFAULT_TAILLE, default='Événement inconnu', blank=True)
    date = models.DateField(blank=True, null=True)
    lieu = models.CharField(max_length=DEFAULT_TAILLE, default='Lieu inconnu', blank=True)
    description = models.TextField(default=DEFAULT_MESSAGE, blank=True)
    image = models.ImageField(upload_to=f'{PATH_IMAGES}images_event/', blank=True)

    def __str__(self):
        return f'{self.nom} - {self.date}'

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Testimonial(models.Model):
    nom = models.CharField(max_length=100, blank=True, default='Utilisateur')
    message = models.TextField(blank=True, default='Message de témoignage')
    date_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Témoignage de {self.nom}'

class Categorie(models.Model):
    nom = models.CharField(max_length=100, blank=True, default='Non spécifié')

    def __str__(self):
        return self.nom
