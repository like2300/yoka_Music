# Generated by Django 4.2.16 on 2024-10-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoka', '0014_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='email',
        ),
    ]
