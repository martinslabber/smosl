########
#
# Use this file with collectd.
#

"""
# Copy this file to: /usr/local/.../smosl_collectd
sudo pip install collectd
sudo pip install smosl
# Add the following to Collectd Config
LoadPlugin python

<Plugin python>
    ModulePath "/usr/local/.../smosl_collectd"
    LogTraces true
    # Interactive true
    Import "smosl_collectd"
</Plugin>
"""

import smosl
import collectd

metric = smosl.SmoslMetric(path='collectd')
metric.send_on_change(**{"startup": 'nod'})


def write(vl, data=None):
    name_segments = []
    for item in [vl.plugin, getattr(vl, 'plugin_instance', None),
                 vl.type, getattr(vl, 'type_instance', None)]:
        if item:
            item = str(item).lower().replace('-', '_')
            if item not in name_segments:
                name_segments.append(item)

    name = ":".join(name_segments)
    if name == 'load':
        send_data = {name + ':1': vl.values[0],
                     name + ':5': vl.values[1],
                     name + ':15': vl.values[2]}
    else:
        send_data = {name: vl.values[0]}
    metric.send_on_change(**send_data)

collectd.register_write(write)
