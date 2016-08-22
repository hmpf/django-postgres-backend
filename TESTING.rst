=======
Testing
=======

Database
--------

1. Create a Postgresql database with an owner that has ``CREATEDB`` set.
2. Set the environment variable ``DATABASE_URL`` to point to the database and user. It should start simply with "postgres://"

Testing with Tox
----------------

Make sure ``tox`` is version 2.3.1 or newer.

Run ``tox``. You might want to only run the environment you need, for instance
by ``tox -e py27-django18`` for Python 2.7 and Django 1.8, To test other python
versions these need to already exist on your system.

Testing without Tox
-------------------

If you don't use ``tox``, make a virtualenv and use pip to install the
requirements::

   pip install -r requirements/base.txt
   pip install -r requirements/test.txt

Run ``python runtests.py``, this'll use the python in your path.