
System Monitoring Over SysLog (SMOSL)
=======================================

ALPHA.! At the moment this is some old code pulled out of the closet and dumped here in the hope it will get structure.


* Monitoring metrics are send through in the message part or a syslog message.
* Metrics are space separated from one another
* Strings values are always wrapped with '"' (double quotes)
* Boolean True is 1, False is 0
* Null (None) is null
* Key is made up of sections separated with ':' (colon)
* Key an value is separated with '=' (equals) no spaces
* Keys are case insensitive. Keys are parsed to lower-case.
* Keys can contain characters a-z 0-9 _ all other characters will be striped

eg. ::

    app1:database:open_connections=5 app1:database:last_error="out of memory"

Installation
-------------

::

        cp smosl.py /usr/local/bin/smosl.py
        cp 100-smosl.conf /etc/rsyslog.d/.
        sudo service ryslog restart 

Value Types
-------------

String - Text
^^^^^^^^^^^^^^^^

* Value part must be surrounded by "="
* Length of string is only limited by syslog implementation.

Example: ::

    metric:name="The string value."

Number
^^^^^^^

* All numbers are converted to a floating point number.
* If conversion failed value is discarded.

Example: ::

    metric:name=24

Boolean (True, False, Null, None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Value is an 0 or 1
* + or - or ? Could work nice for boolean and null.
* T or F or N Could work nice for boolean and null.
* Some problems arrised with Booleans. Propse the new syntax.

::
    metric:seg1:seg2=0&

