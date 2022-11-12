from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ calculates subtotal of multiple of the same item """
    return price * quantity
