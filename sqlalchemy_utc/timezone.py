import datetime


class Utc(datetime.tzinfo):

    __slots__ = ()

    zero = datetime.timedelta(0)

    def utcoffset(self, _):
        return self.zero

    def dst(self, _):
        return self.zero

    def tzname(self, _):
        return 'UTC'


try:
    utc = datetime.timezone.utc
except AttributeError:
    utc = Utc()
