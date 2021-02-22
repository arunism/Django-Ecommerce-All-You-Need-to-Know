from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return round(float(value * arg), 2)

@register.filter
def last_value(value):
    return value[-1]
