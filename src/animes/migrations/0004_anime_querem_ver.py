# Generated by Django 3.1.5 on 2021-01-21 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_perfil_total_favoritos'),
        ('animes', '0003_auto_20210121_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='querem_ver',
            field=models.ManyToManyField(blank=True, related_name='usuarios_querem_ver', to='perfis.Perfil'),
        ),
    ]
