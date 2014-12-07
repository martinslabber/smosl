
from smosl import SmoslMetric


class TestSMOSL(object):

    def setup(self):
        # Monkey patch the _send method to get the message that will be send
        # via syslog.
        self.smosl = SmoslMetric()
        self.test_result = ''

        def _send(b):
            self.test_result = b
        self.smosl._send = _send

    def test_01_send_one(self):
        self.smosl.send_one('one', 1)
        assert self.test_result == 'one=1'
        self.smosl.send_one('one', 'just one')
        assert self.test_result == 'one="just one"'
        self.smosl.send_one('one', True)
        assert self.test_result == 'one=T'
        self.smosl.send_one('one', None)
        assert self.test_result == 'one=N'

    def test_02_send(self):
        self.smosl.send(**{'one': 1})
        assert self.test_result == 'one=1'
        self.smosl.send(one=1)
        assert self.test_result == 'one=1'

    def test_03_send_on_change(self):
        self.smosl.send_on_change(**{'one': 1})
        assert self.test_result == 'one=1'
        self.smosl.send_on_change(one=1)
        assert self.test_result == 'one=1'
        self.smosl.send_on_change(one=2)
        assert self.test_result == 'one=2'
        self.test_result = '-'
        self.smosl.send_on_change(one=2)
        assert self.test_result == '-'
        self.smosl.send_on_change(one=2)
        assert self.test_result == '-'
        self.smosl.send_on_change(one=3)
        assert self.test_result == 'one=3'
