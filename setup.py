#!/usr/bin/env python
from setuptools import setup
import sys

version = '2.0.4'
classifiers = ["Development Status :: 5 - Production/Stable",
               "Environment :: Plugins",
               "Intended Audience :: Developers",
               "Programming Language :: Python",
               "Programming Language :: Python :: 2.7",
               "Programming Language :: Python :: 3",
               "Programming Language :: Python :: 3.4",
               "Programming Language :: Python :: Implementation :: PyPy",
               "License :: OSI Approved :: Apache Software License",
               "Topic :: Software Development :: Testing"]

setup(name='codecov',
      version=version,
      description="Hosted coverage reports for Github, Bitbucket and Gitlab",
      long_description=None,
      classifiers=classifiers,
      keywords='coverage codecov code python java scala php',
      author='@codecov',
      author_email='hello@codecov.io',
      url='http://github.com/codecov/codecov-python',
      license='http://www.apache.org/licenses/LICENSE-2.0',
      packages=['codecov'],
      include_package_data=True,
      zip_safe=True,
      install_requires=["requests>=2.0.0", "coverage"],
      tests_require=["unittest2"],
      entry_points={'console_scripts': ['codecov=codecov:main']})
