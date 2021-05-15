#!/usr/bin/env python

# oc_output is generated using the following command. OpenConfig modules are placed in public/
# pyang --plugindir $PYBINDPLUGIN -f pybind --split-class-dir=oc_output --build-rpcs -p public/release/models public/release/models/interfaces/openconfig-interfaces.yang public/release/models/interfaces/openconfig-if-ip.yang

import oc_output
import yaml
from pprint import pprint
from pyangbind.lib.serialise import pybindIETFXMLEncoder

class FilterModule:
    def filters(self):
        return {
            'interface2oc': self.interface2oc
        }
    
    def interface2oc(self, input):
        # debug
        # print(input)
        
        if_model = oc_output.openconfig_interfaces()
        for ifname in input:
            inet = ""
            inet6 = ""
            
            if 'inet' in input[ifname]:
                inet = input[ifname]['inet']
            
            if 'inet6' in input[ifname]:
                inet6 = input[ifname]['inet6']
            
            if_model.interfaces.interface.add(ifname).subinterfaces.subinterface.add(0).ipv4.addresses.address.add(inet)
            if_model.interfaces.interface[ifname].subinterfaces.subinterface[0].ipv6.addresses.address.add(inet6)    
        
        return "<config>" + pybindIETFXMLEncoder.serialise(if_model.interfaces) + "</config>"
