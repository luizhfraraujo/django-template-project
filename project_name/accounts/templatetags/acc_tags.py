from django.template import Library
from django import template

register = Library()

@register.filter(name='addcssclass')
def addcssclass(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter
def get_type(value):
	t = type(value)
	return t.__module__ + "." + t.__name__