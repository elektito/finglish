#!/usr/bin/env python3

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup
from pip.req import parse_requirements
from pip.download import PipSession
import os

def get_file_path(name):
    return os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        name))

with open(get_file_path('finglish/version.py')) as f:
    exec(f.read())

# read requirements from requirements.txt
requirements = parse_requirements(get_file_path('requirements.txt'),
                                  session=PipSession())
requirements = [str(r.req) for r in requirements]

setup(
    name = 'finglish',
    py_modules = ['version'],
    packages = ['finglish'],
    install_requires = requirements,
    include_package_data=True,
    version = __version__,
    description = 'Finglish-to-Persian converter.',
    author = 'Mostafa Razavi',
    license = 'MIT',
    author_email = 'mostafa@sepent.com',
    url = 'https://github.com/elektito/finglish',
    download_url = 'https://github.com/elektito/finglish/tarball/' + __version__,
    keywords = ['persian', 'finglish'],
    classifiers = [
        'Programming Language :: Python :: 3'
    ],
    entry_points = {
        'console_scripts': [
            'f2p=finglish.f2p:main',
        ],
    },
)
