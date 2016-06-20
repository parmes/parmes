from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.abspath('.'))
extensions = ['youtube', 'ablog', 'sphinx.ext.mathjax']
numfig = True
import ablog
blog_path = 'blog'

templates_path = ['_templates', ablog.get_html_templates_path()]
source_suffix = '.rst'
master_doc = 'index'

project = u'PARMES'
year = datetime.now().year
copyright = u'%d PARMES team' % year

exclude_patterns = ['_build']

latex_documents = [
('solfec/user', 'solfec_user.tex', u'Solfec User Manual', u'Solfec team', 'manual'),
('solfec/xdmf', 'solfec_xdmf.tex', u'Solfec XMDF export', u'Solfec team', 'manual'),
]

html_theme = 'alabaster'
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'recentposts.html',
	'tagcloud.html',
        'categories.html',
        'archives.html',
        'donate.html',
    ]
}
html_theme_options = {
    'description': "Parallel mechanics and particulate media software blog",
    'github_user': 'parmes',
    'github_repo': 'parmes',
    'fixed_sidebar': False,
}
