
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.functions import FunctionElement

from .sqltypes import UtcDateTime


class utcnow(FunctionElement):
    """UTCNOW() expression for multiple dialects."""
    type = UtcDateTime()


@compiles(utcnow)
def default_sql_utcnow(element, compiler, **kw):
    """Assume, by default, time zones work correctly.

    Note:
        This is a valid assumption for PostgreSQL and Oracle.
    """
    return 'CURRENT_TIMESTAMP'


@compiles(utcnow, 'mysql')
def mysql_sql_utcnow(element, compiler, **kw):
    """MySQL returns now as localtime, so we convert to UTC.

    Warning:
        MySQL does not support the use of functions for sqlalchemy
        `server_default=` values. The utcnow function must be used as
        `default=` when interacting with a MySQL server.
    """
    return "CONVERT_TZ(CURRENT_TIMESTAMP, @@session.time_zone, '+00:00')"


@compiles(utcnow, 'sqlite')
def sqlite_sql_utcnow(element, compiler, **kw):
    """SQLite DATETIME('NOW') returns a correct `datetime.datetime` but does not
    add milliseconds to it.

    Directly call STRFTIME with the final %f modifier in order to get those.
    """
    return r"(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))"


@compiles(utcnow, 'mssql')
def mssql_sql_utcnow(element, compiler, **kw):
    """MS SQL provides a function for the UTC datetime."""
    return 'GETUTCDATE()'
