from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', '{{project_name}}.core.views.index', name='index'),
    url(r'^contato/$', '{{project_name}}.core.views.contact', name='contact'),
    ]