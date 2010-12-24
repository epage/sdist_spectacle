#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob,os
from distutils.core import setup
from sdist_spectacle import sdist_spectacle


for fpath in glob.glob('*/*.py[c|o]'):
    os.remove(fpath)


setup(
    name='python-sdist-spectacle',
    version=sdist_spectacle.__version__,
    license='GNU GPLv3',
    description='A distutil extension to build spectacle files for Meego.',
    long_description="A distutil extension to build spectacle files to be used in building srpm's",
    author='Ed Page',
    author_email='eopage@byu.net',
    maintainer=u'Ed Page',
    maintainer_email='eopage@byu.net',
    url='http://www.khertan.net/sdist_spectacle',
    requires=['python','setuptools', 'python-yaml'],
    packages= ['sdist_spectacle',],
    cmdclass={'sdist_spectacle': sdist_spectacle},
    options = {
        'sdist_spectacle': {
            'buildversion':'1',
            'depends':'python2.5, python-setuptools',
            'XSBC_Bugtracker':'http://khertan.net/sdict_maemo:bugs',
            'XB_Maemo_Display_Name':'Python sdist_spectacle',
            'XB_Maemo_Icon_26':'',
            'changelog':"""
* Fix path of file created
""".strip(),
            'copyright':'gpl'
        },
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
    ],
)

