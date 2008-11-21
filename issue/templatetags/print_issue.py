from django import template

register = template.Library()

@register.filter
def hard_indent(value):
  return value.replace('<p>', '<p><span class="hard-indent"/>')

class CounterNode(template.Node):
  
  def __init__(self):
    self.count = 0
    
  def render(self, context):
    self.count += 1
    return self.count
    
@register.tag
def counter(parser, token):
  return CounterNode()