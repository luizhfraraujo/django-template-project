from django.conf.urls import include, url,patterns

urlpatterns = patterns('',
    url(r'^$', 'project_name.accounts.views.dashboard', name='dashboard'),
)