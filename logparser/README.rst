
A bunch of utility script that read STDIN and save the metric. The scripts work best with a syslog daemon.

.. note::
    
    These scripts have only been tested with rsyslog v7.

Installation
==============

#. Copy the appropriate log handler from this directory to */usr/local/bin* ::
    
    sudo cp smosl2file.py /usr/local/bin/.

#. Setup rsyslog. (copy example file *100-smosl.config* to */etc/rsyslog.d* and edit)

smosl2file
==========

This script reads STDIN and save each metric as a new line in the specified file.
Destination filename must be given with the -o or --file argument.

Reference
=========

`SMOSL <https://pypi.python.org/pypi/smosl>`_

