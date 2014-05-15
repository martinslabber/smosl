
System Monitoring Over Syslog - Client Module
=============================================

A python client to format `Metrics`_ and send it to syslog. This is useful for sending custom metrics to smosl.
For system metrics see the smosl collectd example.

smosl_send
----------

This utility can be used from the command line or from shell scripts.
It is used to send metric the SMOSL way. This script can also be used in a PIPE and accepts values via STDIN.


PIPE Example
^^^^^^^^^^^^

Adding the *-i* argument to *smosl_send* tells it to listen to STDIN for metric values. If the metric name is given each line shoudl only contain the value.

If metric name is not given the metric name must be send with each value. Eg.  ::
    MemTotal=1017796000
    MemFree=837588000
    Buffers=17512000

This example sends the meminfo of a Linux system to smosl.

::
    cat /proc/meminfo | sed -e " s/://" | awk '{ V=$2; if ($3 == "kB") V=V*1000; print $1"="V}' | smosl_send -t number -i


Metrics
-------

A key value pair that represent measurement or monitored status.
eg. fanspeed at 78


