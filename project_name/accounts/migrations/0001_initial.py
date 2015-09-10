# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings
import django.contrib.auth.models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Usuário', validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário só pode conter letras, digitos ou os seguintes caracteres: @/./+/-/_', 'invalid')])),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail', unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='É da equipe?')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('user_image', models.ImageField(upload_to='accounts/images', verbose_name='Imagem', null=True, blank=True)),
                ('groups', models.ManyToManyField(related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', blank=True, verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', blank=True, verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserPasswordReset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('key', models.CharField(max_length=100, verbose_name='Chave', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Confirmado?')),
                ('user', models.ForeignKey(related_name='resets', verbose_name='Usuário', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Novas Senhas',
                'ordering': ['-created_at'],
                'verbose_name': 'Nova Senha',
            },
        ),
    ]
