from django import template
from django.conf import settings
from {{project_name}}.core.models import Configuration

register = template.Library()

# settings value
@register.simple_tag
def settings_value(name):
	return getattr(settings, name, "")