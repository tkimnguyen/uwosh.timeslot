# -*- coding: utf-8 -*-
"""
This module contains the tool of uwosh.timeslot
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.5.2-csdad'

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    )

tests_require=['zope.testing']

setup(name='uwosh.timeslot',
      version=version,
      description="A Plone scheduling product",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='scheduling',
      author='T. Kim Nguyen',
      author_email='nguyen@uwosh.edu',
      url='http://www.uwosh.edu/ploneprojects/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uwosh', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'uwosh.timeslot.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*- 
      
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
