#!/usr/bin/env python

from __future__ import print_function
import sys
import argparse
from util import parse_msg


parser = argparse.ArgumentParser(description='Parse log lines from STDIN.')
parser.add_argument('-o', '--file', dest='filename', action='store',
                    help='Filename to store metric to.')
parser.add_argument('-r', '--fileflush', dest='flush', action='store',
                    help='Save to disk after this many metric has been '
                         'recieved.')

args = parser.parse_args()

flush_rate = args.flush
try:
    flush_rate = int(flush_rate)
except (ValueError, TypeError):
    flush_rate = 100

if flush_rate < 0 or flush_rate > 10000:
    flush_rate = 100

filename = args.filename
if not filename:
    print('Please supply a filename with --file or see --help for more.')
    sys.exit(1)

with open(filename, 'a') as fh:
    counter = 0
    while 1:
        # Endless loop and read STDIN
        try:
            line = sys.stdin.readline()

        except KeyboardInterrupt:
            break

        if not line:
            break

        for n in parse_msg(line):
            fh.write(','.join(n) + '\n')
            counter += 1

        if counter >= flush_rate:
            counter = 0
            fh.flush()
#
