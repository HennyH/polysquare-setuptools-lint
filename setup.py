# /setup.py
#
# Installation and setup script for polysquare-setuptools-lint
#
# See /LICENCE.md for Copyright information
"""Installation and setup script for polysquare-setuptools-lint."""

try:
    from polysquare_setuptools_lint import (PolysquareLintCommand,
                                            can_run_frosted)
    _CMDCLASS = {
        "polysquarelint": PolysquareLintCommand
    }

    if can_run_frosted():
        _ADDITIONAL_LINTERS = ["frosted"]

except ImportError:
    _CMDCLASS = dict()
    _ADDITIONAL_LINTERS = list()


from setuptools import find_packages
from setuptools import setup


setup(name="polysquare-setuptools-lint",
      version="0.0.13",
      description="""Provides a 'polysquarelint' command for setuptools""",
      long_description_markdown_filename="README.md",
      author="Sam Spilsbury",
      author_email="smspillaz@gmail.com",
      url="http://github.com/polysquare/polysquare-setuptools-lint",
      classifiers=["Development Status :: 3 - Alpha",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.1",
                   "Programming Language :: Python :: 3.2",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   "Intended Audience :: Developers",
                   "Topic :: Software Development :: Build Tools",
                   "License :: OSI Approved :: MIT License"],
      license="MIT",
      keywords="development linters",
      packages=find_packages(exclude=["test"]),
      cmdclass=_CMDCLASS,
      install_requires=[
          "setuptools",
          "jobstamps>=0.0.4",
          "parmap",
          "pep8",
          "dodgy",
          "mccabe",
          "pep257",
          "pyflakes",
          "pylint",
          "pylint-common",
          "pyroma",
          "vulture",
          "prospector>=0.10.1",
          "flake8==2.3.0",
          "flake8-blind-except",
          "flake8-docstrings",
          "flake8-double-quotes",
          "flake8-import-order",
          "flake8-todo",
          "six"
      ] + _ADDITIONAL_LINTERS,
      extras_require={
          "green": [
              "mock",
              "nose",
              "nose-parameterized",
              "setuptools-green",
              "testtools"
          ],
          "upload": ["setuptools-markdown"]
      },
      entry_points={
          "distutils.commands": [
              ("polysquarelint=polysquare_setuptools_lint:"
               "PolysquareLintCommand"),
          ]
      },
      zip_safe=True,
      include_package_data=True)
