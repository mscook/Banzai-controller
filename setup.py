################################################################################
# This is a setuptools setup file. For more info please see:
#   http://peak.telecommunity.com/DevCenter/setuptools
#
# TODO: Check that matplotlib is downloaded/installed
# TODO: Check that long_description works
#           * is pkgutil in base __init__ required?
# TODO: Include doc/datafiles!
#           * using setuptools-git
#               see: http://pypi.python.org/pypi/setuptools-git/
# TODO: Classifiers see: http://pypi.python.org/pypi?%3Aaction=list_classifiers
#
################################################################################

from setuptools import setup, find_packages
from subprocess import Popen, PIPE


def call_git_describe(abbrev=4):
    """
    Gets the current annotated tag of the git repo

    Based on: https://gist.github.com/300803

    A tag is defined using: git tag -a -m 'Tagging release 1.0' v1.0
    """
    try:
        p = Popen(['git', 'describe', '--abbrev=%d' % abbrev],
                  stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        line = p.stdout.readlines()[0]
        return line.strip()

    except:
        raise ValueError("Cannot find the version number. Add it manually!")


def build_sphinx():
    """
    Build the documentation using sphinx

    TODO: Add this method
    """
    pass


def check_installed():
    """
    Test to see if the depenancies are already met
    
    This should specifically check the presence of NGS tools
    
    TODO: Add this method
    """
    pass


setup(
    name             = 'Banzai-controller',
    version          = call_git_describe(),
    description      = 'Banzai - Next Generation Sequencing Pipeline Tool '+\
                        '- controller appliance'
    long_description = open('README.rst').read(),
    author           = 'Mitchell Jon Stanton-Cook',
    author_email     = 'm.stantoncook@gmail.com',
    url              = 'http://smms-steel.biosci.uq.edu.au',
    packages         = find_packages(),
    include_package_data = True,
    exclude_package_data = {'': ['.gitignore',],},
    license          = 'Educational Community License, Version 2.0',
    classifiers      = ["Development Status :: 3 - Alpha",
                        "Environment :: Console",
                        "Natural Language :: English",
                        "Programming Language :: Python :: 2.6"
                        "Topic :: Scientific/Engineering :: Bio-Informatics"
                        ],
    zip_safe         = False,
    install_requires = ['biopython>=1.58', 'Fabric>=1.3.4', 'matplotlib>=1.1.0'],
    )
