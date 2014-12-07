
System Monitoring Over SysLog (SMOSL)
=======================================

ALPHA.! At the moment this is some old code pulled out of the closet and dumped here in the hope it will get structure.

* Monitoring metrics are send through in the message part or a syslog message.
* Metrics are space separated from one another
* Key is separated from value with '=' (equals) no spaces

eg.  ::

    app1:database:open_connections=5 app1:database:last_error="out of memory"

The JSON equivalent would be. ::

    {app1: {database: {open_connections: 5, last_error: "out of memory"}}}

Installation
-------------

::

        cp smosl.py /usr/local/bin/smosl.py
        cp 100-smosl.conf /etc/rsyslog.d/.
        sudo service ryslog restart 

Keys
----

The key contain a hierarchy, sections in the hierarchy are separated from one another with the ':' character.
The key and all it sections are case insensitive and should only consist out of 'a' to 'z', '0' to '9' and the '_' character. 
When key is processed the key will be converted to lower case, any character not in the above listed set will be dropped.

Value Types
-----------

SMOSL has only 3 data types, it is up to the client to force values into one of the following types: Text, Number and Boolean.

Text
^^^^

* Value part must be surrounded by '"' (double quotes).
* Length of string is only limited by syslog implementation.

Example: ::

    metric:name="The string value."

The JSON equivalent would be. ::

    {metric: {hour: "The string value."}}

Number
^^^^^^

* All numbers are converted to a floating point number.
* If conversion failed value is discarded.

Example: ::

    metric:hour=24

The JSON equivalent would be. ::

    {metric: {hour: 24}}

Boolean (True, False, Null, None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* T, F or N Could work nice for boolean and null.
* The lack of a value (a '=' followed by a space) should be treated as a Null.

::

    metric:seg1:seg2=T

The JSON equivalent would be. ::

    {metric: {seg1: {seg2: true}}}
