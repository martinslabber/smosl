#!/usr/bin/env python

import re
import shlex

msg='app1:database:open_connections=5 app1:database:last_error="out of memory"'

def parse_msg(inmsg):
    metrics = shlex.split(unicode(inmsg))
    for metric in metrics:
        key, value = metric.split('=', 1)
        key = re.sub('[^a-z0-9_:]+', '', key.lower())
        yield (key, value)

for k,v in parse_msg(msg):
    print k, '=', v
#
