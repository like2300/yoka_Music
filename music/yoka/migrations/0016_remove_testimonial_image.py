# Generated by Django 4.2.16 on 2024-10-06 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yoka', '0015_newslettersubscriber_remove_testimonial_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='image',
        ),
    ]