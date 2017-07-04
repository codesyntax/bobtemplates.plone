# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import os

version = '1.0.6.dev0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='bobtemplates.plone',
    version=version,
    description="Templates for Plone projects.",
    long_description=(read('README.rst') + '\n' +
                      read('docs', 'CONTRIBUTORS.rst') +
                      read('docs', 'CHANGES.rst')),
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='web plone zope skeleton project',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/plone/bobtemplates.plone',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'mr.bob',
        #    'pyreadline',
    ],
    extras_require={
        'test': [
            'nose',
            'nose-selecttests',
            'scripttest',
            'six',
            'unittest2',
        ]
    },
    entry_points={},
)
