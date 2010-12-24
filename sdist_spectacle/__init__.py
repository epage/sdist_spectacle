"""
sdist_spectacle

Script to add 'sdist_spectacle' source package distribution command to 'distutils'.
This command builds '.dsc, .changes, .tar.gz' packages suitable for
installation on the Maemo platform by the Maemo autobuilder or the community
obs.

Author: eopage@byu.net
License: GPL 3.0

(Based on 'sdist_maemo'.)
"""


from distutils.core import Command
from distutils.file_util import copy_file
from distutils.dir_util import copy_tree, remove_tree
import time
import os
import yaml


class sdist_spectacle(Command):

    __version__ = '0.0.11'

    # Brief (40-50 characters) description of the command
    description = "Meego Spectacle File Generator"

    # List of option tuples: long name, short name (None if no short
    # name), and help string.
    user_options = [
    ]

    def initialize_options (self):
		pass

    def finalize_options (self):
		pass

    def run (self):
		pass
