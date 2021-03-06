# Generated by Django 3.1.5 on 2021-01-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_perfil_total_favoritos'),
        ('animes', '0002_anime_assistido_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='favorito_por',
            field=models.ManyToManyField(blank=True, related_name='usuarios_favoritaram', to='perfis.Perfil'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='assistido_por',
            field=models.ManyToManyField(blank=True, related_name='usuarios_assistiram', to='perfis.Perfil'),
        ),
    ]
