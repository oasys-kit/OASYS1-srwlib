#! /usr/bin/env python3

import os

try:
    from setuptools import find_packages, setup
except AttributeError:
    from setuptools import find_packages, setup

NAME = 'OASYS1-srwlib'
VERSION = '1.0.12'
ISRELEASED = False

DESCRIPTION = 'PRECOMPILED SRW LIBRARY FOR OASYS (DARWIN AND LINUX)'
README_FILE = os.path.join(os.path.dirname(__file__), 'README.txt')
LONG_DESCRIPTION = open(README_FILE).read()
AUTHOR = 'Luca Rebuffi'
AUTHOR_EMAIL = 'luca.rebuffi@elettra.eu'
URL = 'https://github.com/lucarebuffi/OASYS1-srwlib'
DOWNLOAD_URL = 'https://github.com/lucarebuffi/OASYS1-srwlib'
LICENSE = 'GPLv3'

KEYWORDS = (
    'X-ray optics',
    'simulator',
)

CLASSIFIERS = (
    'Development Status :: 5 - Production/Stable',
    'Environment :: X11 Applications :: Qt',
    'Environment :: Console',
    'Environment :: Plugins',
    'Programming Language :: Python :: 3',
    'Intended Audience :: Science/Research',
)

SETUP_REQUIRES = (
    'setuptools',
)

INSTALL_REQUIRES = (
    'six',
)

PACKAGES = find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests'))

PACKAGE_DATA = {}

PY_MODULES= [
"srwl_bl",
"srwl_uti_cryst",
"srwl_uti_mag",
"srwl_uti_smp",
"srwl_uti_src",
"srwl_uti_und",
"srwlib",
"srwlpy_switcher",
"uti_io",
"uti_math",
"uti_parse",
"uti_plot",
"uti_plot_com",
"uti_plot_matplotlib",    
]

NAMESPACE_PACAKGES = []

ENTRY_POINTS = {
}


if __name__ == '__main__':
    is_beta = False

    try:
        import PyMca5, PyQt4

        is_beta = True
    except:
        setup(
              name = NAME,
              version = VERSION,
              description = DESCRIPTION,
              long_description = LONG_DESCRIPTION,
              author = AUTHOR,
              author_email = AUTHOR_EMAIL,
              url = URL,
              download_url = DOWNLOAD_URL,
              license = LICENSE,
              keywords = KEYWORDS,
              classifiers = CLASSIFIERS,
              packages = PACKAGES,
              package_data = PACKAGE_DATA,
              py_modules = PY_MODULES,
              setup_requires = SETUP_REQUIRES,
              install_requires = INSTALL_REQUIRES,
              entry_points = ENTRY_POINTS,
              namespace_packages=NAMESPACE_PACAKGES,
              include_package_data = True,
              zip_safe = False,
              )

    if is_beta: raise NotImplementedError("This version of OASYS1-srwlib doesn't work with Oasys1 beta.\nPlease install OASYS1 final release: http://www.elettra.eu/oasys.html")
