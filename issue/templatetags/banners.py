import re
import random
from django import template
from django.template import Template, Context

register = template.Library()



class BannerNode(template.Node):
  
  def __init__(self, pos, w, h):
    self.pos = pos
    self.width = w
    self.height = h
    
  def render(self, context):
    raw_template = """
      <!-- {{ width }}x{{ height }} banner at position "{{ pos }}" in zone "{{ zone }}" -->
      <iframe width="{{ width }}" height="{{ height }}" src="http://ad.doubleclick.net/adi/bzj.sportsbizdaily/{{ zone }};pos={{ pos }};sz={{ width }}x{{ height }};ord={{ ord }}?" MARGINWIDTH="0" MARGINHEIGHT="0" HSPACE="0" VSPACE="0" FRAMEBORDER="0" SCROLLING="no" BORDERCOLOR="#000000">
  		</iframe>      	
    """
    t = Template(raw_template)
    c = Context({
      'width': self.width,
      'height': self.height,
      'pos': self.pos,
      'zone': 'main',
      'ord': random.randrange(100000,999999),
    })
    return t.render(c)
    
@register.tag
def banner(parser, token):
  matches = re.match(r"\w+\s+(?P<pos>\w+)\s+(?P<width>\d+)x(?P<height>\d+)",  token.contents)
  return BannerNode(matches.group('pos'), matches.group('width'), matches.group('height'))
  
  
#  <iframe width="#arguments.width#" height="#arguments.height#" src="http<cfif cgi.https eq "on">s</cfif>://ad.doubleclick.net/adi/bzj.sportsbizdaily/#adDepartment#;pos=#arguments.pos#;sz=#arguments.width#x#arguments.height#;ord=#random_shimmy#?" MARGINWIDTH="0" MARGINHEIGHT="0" HSPACE="0" VSPACE="0" FRAMEBORDER="0" SCROLLING="no" BORDERCOLOR="##000000">
#	</iframe>  