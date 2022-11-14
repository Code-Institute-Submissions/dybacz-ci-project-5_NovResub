from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ calculates subtotal of multiple of the same item """
    return price * quantity


@register.filter
def multiply(value, arg):
    """ multiplies value by argument """
    return value * arg
