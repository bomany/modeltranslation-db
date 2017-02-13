===================
ModelTranslation DB
===================

A simple package made to allow django to run tests while having `django-modeltranslation <https://github.com/deschler/django-modeltranslation>`_ installed.

**Do not use this for production. It's use is purely for tests.**

Usage
=====
To use this package, simply create a new settings file
for use in tests and switch the database engine to this one.

**Example**:
::

    DATABASES = {
    'default': {
        'ENGINE': 'modeltranslation_db.backends.mysql',
        'NAME': 'DATABASE_NAME',
        'HOST': 'localhost',
        }
    }

Install
=======
To install just run pip like this
::
	pip install -e git+git@github.com:bomany/modeltranslation-db.git#egg=modeltranslation-db