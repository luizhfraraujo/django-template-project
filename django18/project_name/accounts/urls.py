from django.conf.urls import include, url,patterns

urlpatterns = patterns('',
    url(r'dashboard/^$', 'project_name.accounts.views.dashboard', name='dashboard'),
    url(r'^$', 'project_name.accounts.views.index', name='index'),
)