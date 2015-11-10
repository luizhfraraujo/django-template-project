# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(verbose_name='Sobre', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(verbose_name='Endereço', max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address_city',
            field=models.CharField(verbose_name='Cidade', max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address_complement',
            field=models.CharField(verbose_name='Complemento', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address_district',
            field=models.CharField(verbose_name='Bairro', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address_number',
            field=models.IntegerField(blank=True, verbose_name='Número', default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.CharField(verbose_name='Facebook', max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_developer',
            field=models.BooleanField(verbose_name='É Desenvolvedor?', default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_suport',
            field=models.BooleanField(verbose_name='É Suporte?', default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin',
            field=models.CharField(verbose_name='Linkedin', max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mini_about',
            field=models.CharField(verbose_name='Mini descrição', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_area_code',
            field=models.CharField(verbose_name='DDD', blank=True, max_length=3, default='000'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_numer',
            field=models.CharField(verbose_name='Telefone', max_length=9, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(verbose_name='Profissão', max_length=70, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.CharField(verbose_name='Twitter', max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.CharField(verbose_name='CEP', max_length=9, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(verbose_name='Nome', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(verbose_name='Usuário', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário não pode conter espaços. Pode conter letras, digitos ou os seguintes caracteres: @ . + - _', 'invalid')]),
        ),
    ]
