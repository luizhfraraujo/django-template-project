from django.conf.urls import include, url
from {{project_name}}.accounts.forms import MyAuthenticationForm

urlpatterns = [
    url(r'^$', '{{project_name}}.accounts.views.dashboard', name='dashboard'),
    url(r'^login/$', 'django.contrib.auth.views.login', 
    	{'template_name': 'accounts/login.html'}, name='login'),
    #{'template_name': 'accounts/login.html', 'authentication_form':MyAuthenticationForm}, name='login'),
    url(r'^sair/$', 'django.contrib.auth.views.logout', 
    	{'next_page': 'accounts:login'}, name='logout'),
    url(r'^criar-conta/$', '{{project_name}}.accounts.views.register', name='register'),
    url(r'^criar-conta/$', '{{project_name}}.accounts.views.register', name='register'),
    url(r'^perfil/(?P<user>[\w_-]+)$', '{{project_name}}.accounts.views.profile', name='profile'),
    url(r'^editar/$', '{{project_name}}.accounts.views.edit_account', name='edit_account'),
    url(r'^alterar-senha/$', '{{project_name}}.accounts.views.edit_password', name='edit_password'),
    url(r'^nova-senha/$', '{{project_name}}.accounts.views.password_reset', name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', '{{project_name}}.accounts.views.password_reset_confirm', 
        name='password_reset_confirm'),

    ]