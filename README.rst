SQLAlchemy-Utc
==============

.. image:: https://badge.fury.io/py/SQLAlchemy-Utc.svg?
   :target: https://pypi.python.org/pypi/SQLAlchemy-Utc
.. image:: https://travis-ci.org/spoqa/sqlalchemy-utc.svg?branch=master
   :target: https://travis-ci.org/spoqa/sqlalchemy-utc
.. image:: https://codecov.io/github/spoqa/sqlalchemy-utc/coverage.svg?branch=master
   :target: https://codecov.io/github/spoqa/sqlalchemy-utc?branch=master

This package provides a drop-in replacement of SQLAlchemy's built-in `DateTime`_
type with ``timezone=True`` option enabled.  Although SQLAlchemy's built-in
``DateTime`` type provides ``timezone=True`` option, since some vendors like
SQLite and MySQL don't provide ``timestamptz`` data type, the option doesn't
make any effect on these vendors.

``UtcDateTime`` type is equivalent to the built-in ``DateTime`` with
``timezone=True`` option enabled on vendors that support ``timestamptz``
e.g. PostgreSQL, but on SQLite or MySQL, it shifts all ``datetime.datetime``
values to UTC offset before store them, and returns always aware
``datetime.datetime`` values through result sets.

Long story short, ``UtcDateTime`` does:

- take only aware ``datetime.datetime``,
- return only aware ``datetime.datetime``,
- never take or return naive ``datetime.datetime``,
- ensure timestamps in database always to be encoded in UTC, and
- work as you'd expect.

Written by `Hong Minhee`_ at Spoqa_, and distributed under MIT license.

.. _DateTime: http://docs.sqlalchemy.org/en/latest/core/type_basics.html#sqlalchemy.types.DateTime
.. _Hong Minhee: https://hongminhee.org/
.. _Spoqa: http://www.spoqa.com/
