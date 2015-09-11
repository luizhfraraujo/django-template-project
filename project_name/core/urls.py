from django.conf.urls import include, url

urlpatterns = ['{{project_name}}.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),]