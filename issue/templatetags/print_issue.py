from django import template

register = template.Library()

@register.filter
def hard_indent(value):
    return "[HARD INDENT] "+ value
