# Generated by Django 4.2.16 on 2024-10-04 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yoka', '0005_alter_music_musiciens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='musiciens',
            field=models.ForeignKey(blank=True, default='inconnu', on_delete=django.db.models.deletion.CASCADE, to='yoka.musiciens'),
        ),
    ]
