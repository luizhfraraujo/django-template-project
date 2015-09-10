from django.conf.urls import include, url,patterns

urlpatterns = patterns('',
    url(r'^$', 'project_name.accounts.views.dashboard', name='dashboard'),
    url(r'^login/$', 'project_name.accounts.views.login', name='login'),
    url(r'^criar-conta/$', 'project_name.accounts.views.register', name='register'),
)