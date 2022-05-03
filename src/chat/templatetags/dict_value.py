from django import template

register = template.Library()


@register.filter(name='dict_value')
def get_value_from_key(dictionary, key):
    return dictionary.get(key)
