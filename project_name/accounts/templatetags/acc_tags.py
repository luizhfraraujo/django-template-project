from django.template import Library

register = Library()

@register.filter(name='addcssclass')
def addcssclass(field, css):
   return field.as_widget(attrs={"class":css})