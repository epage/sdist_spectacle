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


from __future__ import with_statement

from distutils.core import Command
import os
import yaml


class sdist_spectacle(Command):

    __version__ = '0.0.11'

    # Brief (40-50 characters) description of the command
    description = "Meego Spectacle File Generator"

    # List of option tuples: long name, short name (None if no short
    # name), and help string.
    __options = [
        ("Name", lambda self: self.distribution.get_name(), "Name"),
        ("Summary", lambda self: self.distribution.get_description(), "Summary"),
        ("Description", lambda self: self.distribution.get_long_description(), "Description"),
        ("Version", lambda self: self.distribution.get_version(), "Version"),
        ("Release", lambda self: None, "Release"),
        ("Group", lambda self: None, "Group"),
        ("Provides", lambda self: None, "Provides"),
        ("License", lambda self: self.distribution.get_license(), "License"),
        ("URL", lambda self: self.distribution.get_url(), "URL"),
        ("PkgBR", lambda self: ["python-dev"], "Packages required in building, or BuildRequires "),
        ("Configure", lambda self: "none", "autogen, configure, reconfigure, none"),
        ("Builder", lambda self: "python", "make, single-make, python, perl, qmake, none"),
        ("Sources", lambda self: ["%s-%s.tar.gz" % (self.Name, self.Version)], "Sources"),
        ("SupportOtherDistros", lambda self: True, "Whether need to check for other distros (besides MeeGo) "),
        ("NoDesktop", lambda self: False, "Whether to install the desktop files in package "),
    ]
    __needListHack = ("Provides", )

    user_options = [
        (option[0], None, option[2])
        for option in __options
    ]
    user_options.extend([
        ('dist-dir=', 'd', "directory to put the source distribution archive(s) in [default: dist]"),
    ])

    def initialize_options(self):
        self.dist_dir = None
        for option in self.__options:
            name = option[0]
            setattr(self, name, None)

    def finalize_options(self):
        self.set_undefined_options('sdist', ('dist_dir', 'dist_dir'))
        for option in self.__options:
            name = option[0]
            get_default = option[1]
            if getattr(self, name) is None:
                setattr(self, name, get_default(self))
        for name in self.__needListHack:
            items = getattr(self, name)
            listOfItems = items.split(",")
            listOfItems = [item.strip() for item in listOfItems]
            setattr(self, name, listOfItems)

    def run(self):
        spectacleContent = {}
        for option in self.__options:
            name = option[0]
            value = getattr(self, name)
            if value is not None:
                spectacleContent[name] = value

        try:
            os.makedirs(self.dist_dir)
        except:
            pass

        spectacleFilename = os.path.join(self.dist_dir, "%s.yaml" % self.Name)
        with open(spectacleFilename, "w") as spectacleFile:
            yaml.dump(spectacleContent, spectacleFile)
