# Generated by Django 4.2.16 on 2024-10-06 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yoka', '0010_remove_musicien_link_socials_alter_music_titre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_adress', models.CharField(default='local', max_length=200, null=True)),
                ('phone', models.CharField(default='country number', max_length=200, null=True)),
                ('mail', models.CharField(default='mail ...', max_length=200, null=True)),
                ('social_Contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yoka.sociallink')),
            ],
        ),
    ]
