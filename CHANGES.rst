Changelog
=========

0.14.0
------

Released on September 24, 2021.

- Add cache_ok flag on ``UtcDateTime`` to supress Pandas warnings.
  [`#14`_ by derekderie]

.. _#14: https://github.com/spoqa/sqlalchemy-utc/pull/14


0.13.0
------

Released on September 24, 2021.

- Add milliseconds to SQLite datetimes.  [`#12`_ by Giovanni Santini]
- Add support for newer python versions. (3.7, 3.8, 3.9)
  [`#12`_ by Giovanni Santini]

.. _#12: https://github.com/spoqa/sqlalchemy-utc/pull/12


0.12.0
------

Released on May 7, 2021.

- Add `py.typed` file to the package to be compatible with PEP-561.
  [`#10`_ by Dima Boger]

.. _#10: https://github.com/spoqa/sqlalchemy-utc/pull/10


0.11.0
------

Released on November 13, 2020.

- Ensured always returning the datetime with UTC timezone.
  [`#8`_ by Eduard Christian Dumitrescu]

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
