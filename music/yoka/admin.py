from django.contrib import admin
from .models import Musicien, SocialLink, ContactInfo, Music, Event, Testimonial, NewsletterSubscriber

class Musicienstab(admin.ModelAdmin):
    list_display = ['nom', 'bio', 'date_de_naissance']

class Musictab(admin.ModelAdmin):
    list_display = ['titre', 'musicien', 'date_publication']

class Eventtab(admin.ModelAdmin):
    list_display = ['nom', 'date', 'lieu']  # Corrigé pour correspondre aux champs du modèle

class NewsletterSubscribertab(admin.ModelAdmin):
    list_display = ['email']

class Testimonialtab(admin.ModelAdmin):
    list_display = ['nom', 'date_post']  # Corrigé pour correspondre aux champs du modèle

# Enregistrement des modèles dans l'admin
admin.site.register(Musicien, Musicienstab)
admin.site.register(SocialLink)
admin.site.register(ContactInfo)
admin.site.register(Music, Musictab)
admin.site.register(Event, Eventtab)
admin.site.register(Testimonial, Testimonialtab)
admin.site.register(NewsletterSubscriber, NewsletterSubscribertab)
