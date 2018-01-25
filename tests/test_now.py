import datetime

from pytest import yield_fixture

from sqlalchemy import Column, MetaData, Table, select

from sqlalchemy_utc import UtcDateTime, utc, utcnow


TABLE = Table(
    'test_table', MetaData(),
    Column('time', UtcDateTime, default=utcnow()))


@yield_fixture
def fx_connection(fx_engine):
    connection = fx_engine.connect()
    try:
        transaction = connection.begin()
        try:
            TABLE.create(connection)
            yield connection
        finally:
            transaction.rollback()
    finally:
        connection.close()


def test_utcnow_timezone(fx_connection):
    fx_connection.execute(TABLE.insert(), [{}])
    rows = fx_connection.execute(select([TABLE])).fetchall()
    server_now = rows[0].time
    local_now = datetime.datetime.now(utc)
    assert server_now.tzinfo is not None
    assert abs(server_now - local_now) < datetime.timedelta(seconds=30)
