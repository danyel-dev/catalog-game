from django import template


register = template.Library()

@register.filter(name='first_lyric')
def first_lyric(name):
    return name[0]
