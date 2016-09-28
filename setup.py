#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as README_FILE:
    long_description = README_FILE.read()

setup(
    name='django-postgres-backend',
    version='0.1',
    packages=['dpb.postgres_sequencesafe'],
    package_dir = {'': 'src',},
    include_package_data=True,
    zip_safe=False,
    platforms=['any'],
    description='Postgres backend that introspects sequence names',
    author_email='hanne.moa@uninett.no',
    url='https://github.com/hmpf/django-postgres-backend',
    author='Hanne Moa',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
