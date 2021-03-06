# Generated by Django 3.1.5 on 2021-02-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0004_anime_querem_ver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='nota',
        ),
        migrations.AddField(
            model_name='anime',
            name='ano_inicio',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='anime',
            name='ano_termino',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='anime',
            name='autor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='anime',
            name='c_indicativa',
            field=models.CharField(blank=True, choices=[('L', 'L'), ('10', '10'), ('12', '12'), ('14', '14'), ('16', '16'), ('18', '18')], max_length=25),
        ),
        migrations.AddField(
            model_name='anime',
            name='categorias',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='anime',
            name='nota_imdb',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='anime',
            name='num_ep',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='anime',
            name='tempo_medio_ep',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
