#! /usr/bin/env python3

import os

try:
    from setuptools import find_packages, setup
except AttributeError:
    from setuptools import find_packages, setup

NAME = 'OASYS1-srwlib'
VERSION = '1.0.3'
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
)

PACKAGES = find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests'))

PACKAGE_DATA = {
}

NAMESPACE_PACAKGES = []

ENTRY_POINTS = {
}

import site, shutil, sys


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
              #          py_modules = PY_MODULES,
              setup_requires = SETUP_REQUIRES,
              install_requires = INSTALL_REQUIRES,
              #extras_require = EXTRAS_REQUIRE,
              #dependency_links = DEPENDENCY_LINKS,
              entry_points = ENTRY_POINTS,
              namespace_packages=NAMESPACE_PACAKGES,
              include_package_data = True,
              zip_safe = False,
              )

    if is_beta: raise NotImplementedError("This version of OASYS1-srwlib doesn't work with Oasys1 beta.\nPlease install OASYS1 final release: http://www.elettra.eu/oasys.html")

    try:
        is_install = False

        for arg in sys.argv:
            if arg == 'install': is_install = True

        if is_install:
            print("COPYING SRWLIB files")

            site_packages_dir = None

            for directory in site.getsitepackages():
                if os.path.exists(directory + "/oasys") or os.path.exists(directory + "/OASYS1.egg-link"):
                    site_packages_dir = directory
                    break

            if not site_packages_dir is None:
                shutil.copyfile("lib/srwl_bl.py", site_packages_dir + "/srwl_bl.py")
                shutil.copyfile("lib/srwl_uti_cryst.py", site_packages_dir + "/srwl_uti_cryst.py")
                shutil.copyfile("lib/srwl_uti_mag.py", site_packages_dir + "/srwl_uti_mag.py")
                shutil.copyfile("lib/srwl_uti_smp.py", site_packages_dir + "/srwl_uti_smp.py")
                shutil.copyfile("lib/srwl_uti_src.py", site_packages_dir + "/srwl_uti_src.py")
                shutil.copyfile("lib/srwl_uti_und.py", site_packages_dir + "/srwl_uti_und.py")
                shutil.copyfile("lib/srwlib.py", site_packages_dir + "/srwlib.py")
                shutil.copyfile("lib/uti_io.py", site_packages_dir + "/uti_io.py")
                shutil.copyfile("lib/uti_math.py", site_packages_dir + "/uti_math.py")
                shutil.copyfile("lib/uti_parse.py", site_packages_dir + "/uti_parse.py")
                shutil.copyfile("lib/uti_plot_com.py", site_packages_dir + "/uti_plot_com.py")
                shutil.copyfile("lib/uti_plot_matplotlib.py", site_packages_dir + "/uti_plot_matplotlib.py")
                shutil.copyfile("lib/uti_plot.py", site_packages_dir + "/uti_plot.py")
                shutil.copyfile("lib/" + str(sys.platform) + "/srwlpy.so", site_packages_dir + "/srwlpy.so")
        else:
            print("SRWLIB not copied")

    except Exception as exception:
        print(str(exception))
