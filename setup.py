# Can't hit Django by importing json_fields or we hit ImportError on settings

import os
version = '0.0'
with open(os.path.join('json_field', '__init__.py')) as f:
    for l in f.readlines():
        if l.startswith('__version__'):
            version = l.rsplit('=', 1)[1].strip()

from distutils.core import setup

description = 'Generic JSON model and form fields.'

try:
    with open('README.rst') as f:
        long_description = f.read()
except IOError:
    long_description = description

setup(
    name = 'django-json-field',
    version = version,
    description = description,
    author = 'Derek Schaefer',
    author_email = 'derek.schaefer@gmail.com',
    url = 'https://github.com/derek-schaefer/django-json-field',
    long_description = long_description,
    packages = ['json_field'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
