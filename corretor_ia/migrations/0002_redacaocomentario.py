# Generated by Django 5.0.6 on 2024-06-01 15:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corretor_ia', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RedacaoComentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(verbose_name='Comentário')),
                ('avaliacoes', models.ManyToManyField(null=True, related_name='favoritos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]