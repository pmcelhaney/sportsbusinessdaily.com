import re
from django import template

register = template.Library()



class BannerNode(template.Node):
  
  def __init__(self, w, h):
    self.width = w
    self.height = h
    
  def render(self, context):
    return "[banner: %sx%s]" % (self.width, self.height)
    
@register.tag
def banner(parser, token):
  matches = re.match(r".+ (?P<width>\d+)x(?P<height>\d+)",  token.contents)
  return BannerNode(matches.group('width'), matches.group('height'))
  
  
#  <iframe width="#arguments.width#" height="#arguments.height#" src="http<cfif cgi.https eq "on">s</cfif>://ad.doubleclick.net/adi/bzj.sportsbizdaily/#adDepartment#;pos=#arguments.pos#;sz=#arguments.width#x#arguments.height#;ord=#random_shimmy#?" MARGINWIDTH="0" MARGINHEIGHT="0" HSPACE="0" VSPACE="0" FRAMEBORDER="0" SCROLLING="no" BORDERCOLOR="##000000">
#	</iframe>  