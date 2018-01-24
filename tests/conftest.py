import os

from pytest import fixture

from sqlalchemy.engine import create_engine
from sqlalchemy.pool import NullPool


try:
    database_urls = os.environ['TEST_DATABASE_URLS'].split()
except KeyError:
    database_urls = []


@fixture(scope='function', params=['sqlite://'] + database_urls)
def fx_engine(request):
    url = request.param
    engine = create_engine(url, poolclass=NullPool)
    request.addfinalizer(engine.dispose)
    return engine
