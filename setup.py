from __future__ import print_function

import io
import sys
import os.path
from setuptools import setup, find_packages

readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')
changelog_path = os.path.join(os.path.dirname(__file__), 'CHANGELOG')

readme = io.open(readme_path, encoding='utf-8').read()
changelog = io.open(changelog_path, encoding='utf-8').read()

long_description = readme + '\n\n' + changelog


setup(
    name='pdbpp',
    version='0.9.2',
    author='Antonio Cuni',
    author_email='anto.cuni@gmail.com',
    packages=find_packages(exclude=['testing',]),
    url='http://github.com/antocuni/pdb',
    license='BSD',
    platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
    description='pdb++, a drop-in replacement for pdb',
    long_description=long_description,
    keywords='pdb debugger tab color completion',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    install_requires=[
        "fancycompleter>=0.8",
        "wmctrl",
        "pygments",
    ],
    extras_require={
        'funcsigs': ["funcsigs"],
    },
    include_package_data=True,
)
