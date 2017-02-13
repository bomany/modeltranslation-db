#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='modeltranslation-db',
    version='1.0',
    description='A Database engine for unit testing when using django-modeltranslation',
    # long_description=long_description,
    url='https://github.com/bomany/modeltranslation-db',
    author='Filipe Reis',
    author_email='filipereis10@hotmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Translations :: Unit Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='django-modeltranslation unit testing development',
    packages=['modeltranslation_db', ],
    install_requires=['django', 'django-modeltranslation'],
    zip_safe=False,
)