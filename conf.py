from datetime import datetime


extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'PARMES'
year = datetime.now().year
copyright = u'%d PARMES team' % year

exclude_patterns = ['_build']

latex_documents = [
('solfec/user', 'solfec_user.tex', u'Solfec User Manual', u'Solfec team', 'manual'),
('solfec/theory', 'solfec_theory.tex', u'Solfec Theory Manual', u'Solfec team', 'manual'),
]

html_theme = 'alabaster'
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}
html_theme_options = {
    'description': "Parallel mechanics and particulate media software blog",
    'github_user': 'parmes',
    'github_repo': 'parmes.github.io',
    'fixed_sidebar': True,
}
