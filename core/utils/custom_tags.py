from django import template

register = template.Library()

@register.filter(name = 'discount')
def discount(value, arg):
    try:
        return int(value) - int(value)*int(arg)/100
    except (ValueError, ZeroDivisionError):
        return None
