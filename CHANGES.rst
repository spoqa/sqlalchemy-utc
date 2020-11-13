Changelog
=========

0.11.0
------

Released on November 13, 2020.

- Ensured always returning the datetime with UTC timezone.
  [`#8_` by Eduard Christian Dumitrescu]

.. _#8: https://github.com/spoqa/sqlalchemy-utc/pull/8


0.10.0
------

Released on January 25, 2018.

- Dropped support of older Python versions: 2.6, 3.2, and 3.3.
  [`#2`_ by George Leslie-Waksman]
- Added ``sqlalchemy_utc.utcnow()`` function as an alternative to
  ``sqlalchemy.sql.functions.now()`` for generating ``UtcDateTime`` values
  on the database server.  [`#4`_ by George Leslie-Waksman]

.. _#2: https://github.com/spoqa/sqlalchemy-utc/pull/2
.. _#4: https://github.com/spoqa/sqlalchemy-utc/pull/4


0.9.0
-----

First version.  Released on June 22, 2016.
