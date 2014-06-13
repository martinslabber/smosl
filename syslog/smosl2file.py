#!/usr/bin/python

import re
import sys
import shlex
import time
import datetime


def convert_enddate_to_seconds(ts):
    """Takes ISO 8601 format(string) and converts into epoch time."""
    dt = datetime.datetime.strptime(ts[:-7], '%Y-%m-%dT%H:%M:%S.%f') + \
        datetime.timedelta(hours=int(ts[-5:-3]),
                           minutes=int(ts[-2:])) * int(ts[-6:-5] + '1')
    seconds = time.mktime(dt.timetuple()) + dt.microsecond / 1000000.0
    return seconds


def parse_msg(inmsg):
    metrics = shlex.split(unicode(inmsg))
    if metrics:
        try:
            mtime = convert_enddate_to_seconds(metrics[0])
            # TODO(MS): Convert to timestamp UTC.
            host = re.sub('[^a-z0-9_.]+', '', metrics[1].lower())
            for metric in metrics[3:]:
                if '=' in metric:
                    key, value = metric.split('=', 1)
                    key = re.sub('[^a-z0-9_:]+', '', key.lower())
                    yield (host + ':' + key, mtime, value)
                else:
                    print 'ERROR', metric, inmsg
        except ValueError:
            return


def save(fh, metric_key, metric_time, metric_value):
    fh.write(",".join(map(str,
                          [metric_time, metric_key, metric_value])) + '\n')


fh = open('/tmp/metric_data.csv', 'a')
fh.write('# Started\n')
fh.flush()
counter = 0
while 1:
    try:
        line = sys.stdin.readline()

    except KeyboardInterrupt:
        break

    if not line:
        break

    for n in parse_msg(line):
        save(fh, *n)
        counter += 1

    if counter > 1:
        counter = 0
        fh.flush()

fh.close()
#
