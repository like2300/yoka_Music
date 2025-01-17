# Generated by Django 4.2.16 on 2024-10-07 19:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yoka', '0017_testimonial_date_post_alter_testimonial_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, default='Album inconnu', max_length=200)),
                ('date_sortie', models.DateField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, upload_to='media/images_album/')),
                ('description', models.TextField(blank=True, default='Musique disponible sur Yoka')),
                ('prix', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('artiste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='yoka.musicien')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, default='Non spécifié', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_address', models.CharField(default='local', max_length=200, null=True)),
                ('phone', models.CharField(default='country number', max_length=200, null=True)),
                ('mail', models.EmailField(default='mail ...', max_length=200, null=True)),
                ('social_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yoka.sociallink')),
            ],
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, default='Musique disponible sur Yoka', max_length=200)),
                ('fichier_audio', models.FileField(blank=True, upload_to='media/audio_singles/')),
                ('date_sortie', models.DateField(blank=True, null=True)),
                ('prix', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('artiste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='singles', to='yoka.musicien')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.RemoveField(
            model_name='event',
            name='place',
        ),
        migrations.RemoveField(
            model_name='music',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='music',
            name='date_sortie',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='name',
        ),
        migrations.AddField(
            model_name='event',
            name='lieu',
            field=models.CharField(blank=True, default='Lieu inconnu', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='nom',
            field=models.CharField(blank=True, default='Événement inconnu', max_length=200),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='nom',
            field=models.CharField(blank=True, default='Utilisateur', max_length=100),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='date_post',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='message',
            field=models.TextField(blank=True, default='Message de témoignage'),
        ),
        migrations.DeleteModel(
            name='Contact_info',
        ),
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='yoka.album'),
        ),
    ]
