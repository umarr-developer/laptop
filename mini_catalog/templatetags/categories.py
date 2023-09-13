from django import template
from mini_catalog.models import Categories

register = template.Library()

@register.simple_tag()
def get_categories():
    return Categories.objects.all()
