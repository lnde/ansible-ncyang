#!/usr/bin/env python

# This is an example that demonstrates how to map a YAML structure from
# Ansible onto a OpenConfig YANG model.
# 
# Example of input YAML document:
# ---
# interfaces:
#  Loopback100:
#    inet: 192.0.2.2/32
#    inet6: 2001:db8::2/128
#  Loopback101:
#    inet: 10.99.0.2/32
#    inet6: 2021::2/128

# oc_output is generated using the following command. OpenConfig modules are placed in public/
# pyang --plugindir $PYBINDPLUGIN -f pybind --split-class-dir=oc_output --build-rpcs -p public/release/models public/release/models/interfaces/openconfig-interfaces.yang public/release/models/interfaces/openconfig-if-ip.yang

from oc_output import openconfig_interfaces
from pyangbind.lib.serialise import pybindIETFXMLEncoder

class FilterModule:
    def filters(self):
        return {
            'interface2oc': self.interface2oc
        }

    def interface2oc(self, input):
        # debug
        # print(input)

        if_model = openconfig_interfaces()
        for ifname in input:
            inet = ""
            if 'inet' in input[ifname]:
                inet = input[ifname]['inet']

            inet6 = ""
            if 'inet6' in input[ifname]:
                inet6 = input[ifname]['inet6']

            if_model.interfaces.interface.add(ifname).subinterfaces.subinterface.add(0).ipv4.addresses.address.add(inet)
            if_model.interfaces.interface[ifname].subinterfaces.subinterface[0].ipv6.addresses.address.add(inet6)    

        return "<config>" + pybindIETFXMLEncoder.serialise(if_model.interfaces) + "</config>"
