#!/usr/bin/env python

import sys
import redis
from util import parse_msg


def save(db, metric_host, metric_key, metric_time, metric_value):
    db.hset(metric_host + ':' + metric_key, metric_time, metric_value)

db = redis.Redis(db=9)

while 1:
    try:
        line = sys.stdin.readline()

    except KeyboardInterrupt:
        break

    if not line:
        break

    for n in parse_msg(line):
        save(db, *n)
