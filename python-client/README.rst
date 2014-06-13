
System Monitoring Over Syslog - Client Module
=============================================

A python client to format `Metrics`_ and send it to syslog. This is useful for sending custom metrics to smosl.
For system metrics see the smosl collectd example.

Smosl uses syslog as the transport for the metrics. You are using syslog already, right? So we ship the metrics via the same channel. 
Often in production syslog is already setup to ship logs to centralised log storage or processing nodes.

Installation
------------

Use pip to install from pypi. ::

    sudo pip install smosl

Use pip to install from source. (Run this command from where code was checked out to.)::

    pip install -U .

usage
-----

The module can be used from within an application to record metrics. eg. ::

    import smosl
    metric = smosl.SmoslMetric()
    # Send one metric.
    metric.send_one('connections', 10)
    # Send several metrics.
    stats = {'connections': 11, 'errors': 3, 'loggedin_users': 9}
    metric.send(**stats)

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

This example sends the *sysctl* to SMOSL works on Linux and Mac. ::

    sysctl -a | sed -e " s/:/=/g" | ./smosl_send -i -t number --path sysctl

Metrics
-------

A key value pair that represent measurement or monitored status.
eg. fanspeed at 78

Further
-------

At https://github.com/martinslabber/smosl there are further examples of using SMOSL with collectd to get overall view of a system.

