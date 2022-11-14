from django import template


register = template.Library()


@register.filter
def multiply(value, arg):
    """ multiplies value by argument """
    return value * arg
