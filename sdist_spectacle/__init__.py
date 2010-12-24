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
        ("name", lambda self: self.distribution.get_name(), "Name"),
        ("summary", lambda self: self.distribution.get_description(), "Summary"),
        ("description", lambda self: self.distribution.get_long_description(), "Description"),
        ("version", lambda self: self.distribution.get_version(), "Version"),
        ("release", lambda self: 0, "Release"),
        ("group", lambda self: "", "Group"),
        ("license", lambda self: self.distribution.get_license(), "License"),
        ("url", lambda self: self.distribution.get_url(), "URL"),
        ("pkgBR", lambda self: ["python-dev"], "Packages required in building, or BuildRequires "),
        ("configure", lambda self: "none", "autogen, configure, reconfigure, none"),
        ("builder", lambda self: "python", "make, single-make, python, perl, qmake, none"),
        ("sources", lambda self: ["%s-%s.tar.gz" % (self.name, self.version)], "Sources"),
        ("supportOtherDistros", lambda self: True, "Whether need to check for other distros (besides MeeGo) "),
        ("noDesktop", lambda self: False, "Whether to install the desktop files in package "),
    ]

    user_options = [
        (option[0], None, option[2])
        for option in __options
    ]

    def initialize_options(self):
        self.dist_dir = None
        for option in self.__options:
            name = option[0]
            setattr(self, name, None)

    def finalize_options(self):
        if self.dist_dir is None:
            self.dist_dir = "dist"
        for option in self.__options:
            name = option[0]
            get_default = option[1]
            if getattr(self, name) is None:
                setattr(self, name, get_default(self))

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

        spectacleFilename = os.path.join(self.dist_dir, "%s.yaml" % self.name)
        with open(spectacleFilename, "w") as spectacleFile:
            yaml.dump(spectacleContent, spectacleFile)
