"""
example_setup.py

Example use of 'sdist_spectacle' command.

Author: eopage@byu.net

24 December 2010

License: GPLv3
"""


from sdist_spectacle import sdist_spectacle
from distutils.core import setup


setup(
    name="example",
    scripts=['example'],
    version='0.0.1',
    maintainer="Ed Page",
    maintainer_email="eopage@byu.net",
    description="An example.",
    long_description="An example packed with sdist_spectacle",
    data_files = [('share/applications/hildon', ['example.desktop'])],
    cmdclass={'sdist_spectacle': sdist_spectacle}
)

