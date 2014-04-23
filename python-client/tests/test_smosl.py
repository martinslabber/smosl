
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
        assert self.test_result == 'one=1'
        self.smosl.send_one('one', None)
        assert self.test_result == 'one=null'
