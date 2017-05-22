#-*- coding:utf-8 -*-
u'''
Execute the specified python code and insert the output into the document"""

usage:

First of all, add `runpy` to sphinx extension list in conf.py

.. code-block:: python

   extensions = ['runpy']


then use `youtube` directive.

You can then include a python code to be run as follows

.. code-block:: rst

   .. runpy::
    
     python code to be run


finally, build your sphinx project.

.. code-block:: sh

   $ make html

'''

__version__ = '0.1.0'
__author__ = 'Michael Mrozek, Alex Forencich'
__license__ = 'N/A'

def setup(app):

    from . import runpy

    app.add_directive('runpy', runpy.RunpyDirective)
