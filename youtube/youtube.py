#-*- coding:utf-8 -*-

#Import urlparse in Python 2 or urllib.parse in Python 3

try:
    import urlparse

except ImportError:
    import urllib.parse as urlparse


from docutils import nodes
from docutils.parsers import rst

def nonnegative_int(argument):
  """
  Check for a non-negative int argument; raise ``ValueError`` if not.
  (Directive option conversion function.)
  """
  return int(argument)


class youtube(nodes.General, nodes.Element):
    pass


def is_url(s):

    if s.startswith('http://') or s.startswith('https://'):
        return True

    return False


def get_video_id(url):

    return urlparse.parse_qs(urlparse.urlparse(url).query)['v'][0]


def visit(self, node):

    video_id = node.video_id
    wdt = node['width']
    hgt = node['height']
    url = u'//www.youtube.com/embed/{0}?rel=0'.format(video_id)
    you = u'''<iframe width="{0}" height="{1}" src="{2}" frameborder="0" allowfullscreen="1">&nbsp;</iframe>'''.format(wdt, hgt, url)
    tag = u'<p align="center">{0}</p>'.format(you)

    self.body.append(tag)


def depart(self, node):
    pass


class YoutubeDirective(rst.Directive):

    name = 'youtube'
    node_class = youtube

    has_content = False
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = False
    option_spec = {
      'width': nonnegative_int,
      'height': nonnegative_int,
    }

    def run(self):

        node = self.node_class()

        arg = self.arguments[0]

        if is_url(arg):
          node.video_id = get_video_id(arg)
        else:
          node.video_id = arg

        if 'width' in self.options:
          node['width'] = self.options['width']
	else:
	  node['width'] = 640

        if 'height' in self.options:
          node['height'] = self.options['height']
	else:
	  node['height'] = 360

        return [node]
