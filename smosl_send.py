#!/usr/bin/env python

import zlib
import logging
import logging.handlers


class SmoslMetric(object):

    def __init__(self, server=None, port=None, path=None):
        self._path = []
        self._address = '/dev/log'
        self._change_detection = {}
        if server:
            self._address = (server, port or 514)

        self._logger = logging.getLogger('smosl')
        self._setup_logger()
        if path:
            self.path = path

    def _setup_logger(self):
        """Configure the python logger."""
        self._logger.setLevel(logging.INFO)

        ## Attach Syslog as a handler
        syslog_handler = logging.handlers.SysLogHandler(address=self._address)
        syslog_handler.setLevel(logging.INFO)
        syslog_handler.setFormatter(logging.Formatter('metric: %(message)s'))
        self._logger.addHandler(syslog_handler)

    def _send(self, msg):
        """Send the message to syslog."""
        self._logger.info(msg)
        print msg

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if not value:
            self._path = []
        elif isinstance(value, list):
            self._path = value
        else:
            self._path = str(value).split(":")

    def send_one(self, metric_name, metric_value):
        """Send one metric value."""
        return self.send(**{metric_name: metric_value})

    def send(self, **kwargs):
        """Send to syslog."""
        msg = []
        for kwkey, value in kwargs.iteritems():
            key = ":".join(self._path + [kwkey])
            if value is None:
                msg.append('{0}=null'.format(key))
            elif isinstance(value, str):
                msg.append('{0}="{1}"'.format(key, str(value)))
            elif isinstance(value, bool):
                msg.append('{0}={1}'.format(key, int(value)))
            elif isinstance(value, int) or isinstance(value, float):
                msg.append('{0}={1}'.format(key, value))
            else:
                raise ValueError('Cannot interprete {0} of type {1}'.
                                 format(value, type(value)))
        self._send(' '.join(msg))

    def send_on_change(self, **kwargs):
        """Keep track of metrics and values. Send if there was a change."""
        send_update = {}
        for kwkey, value in kwargs.iteritems():
            akey = zlib.adler32(str(kwkey))
            aval = zlib.adler32(str(value))
            if self._change_detection.get(akey) != aval:
                self._change_detection[akey] = aval
                send_update[kwkey] = value
        if send_update:
            self.send(**send_update)

    def flush_on_change(self):
        """Flush the on chnage detection storage.

        It is good to this periodicaly in you system to send metric
        even if it has not changed.

        """
        self._change_detection = {}


def arg_parse():
    """
    Not implimented but something like this.
    -h, --help Print help and exit
    -V, --version Print version and exit
    -n, --name=STRING Name of the metric
    -v, --value=STRING Value of the metric
    -t, --type=STRING Either string|int|float|boolean
    -h, --host=STRING host to send to
    -p, --port=INT port to use
    -t, --tcp use tcp not udp.
    -d, --device=STRING use device other than /dev/log - Cannot use with -p or -h
    """
    pass

if __name__ == "__main__":
    metric = SmoslMetric(path='powerstation:reactor:turbine', server='192.168.10.70')
    metric.send(rpm=3003, l='hjjk')
    metric.send_one("monkey:man:and:the:spider", 'sleep tuli')
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tulis', 'chicken': True})
    metric.send_on_change(**{"monkey:man:and:the:spider": 'sleep tuli'})
