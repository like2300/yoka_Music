# Generated by Django 4.2.16 on 2024-10-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoka', '0011_contact_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Musique disponible sur Yoka', max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('place', models.CharField(blank=True, default='Musique disponible sur Yoka', max_length=200)),
                ('description', models.TextField(blank=True, default='Musique disponible sur Yoka')),
                ('image', models.ImageField(blank=True, upload_to='media/images_event/')),
            ],
        ),
    ]