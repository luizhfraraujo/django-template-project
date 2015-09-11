from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', '{{project_name}}.accounts.views.dashboard', name='dashboard'),
    url(r'^login/$', 'django.contrib.auth.views.login', 
    	{'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', 'django.contrib.auth.views.logout', 
    	{'next_page': 'accounts:login'}, name='logout'),
    url(r'^criar-conta/$', '{{project_name}}.accounts.views.register', name='register'),
    url(r'^perfil/(?P<user>[\w_-]+)$', '{{project_name}}.accounts.views.profile', name='profile'),]