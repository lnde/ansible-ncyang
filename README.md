# Ansible NETCONF/YANG Example

This collection demonstrates two different ways of using NETCONF/YANG with
Ansible. One way using "templated XML" and the other using generated Python
classes that are built from YANG models.

Included is a very simple YAML inventory that we'll map onto the
`openconfig-interfaces` model and then serialised to XML, which is finally
transferred to the device using NETCONF.

To transform our simple YAML inventory in this example to OpenConfig we're
using a custom filter located in `filter_plugins/`.

## Tested with Ansible

This collection has been tested against following Ansible version: **2.10.2**.

## External requirements

It's possible to run the included playbooks without any network devices and
you'll see the generated config that would be deployed.

In order to generate the Python classes in `filter_plugins/oc_output` you'll
need `pyang` and a recent version `pyangbind`. Included in this repository are
classes generated from OpenConfig dated 2021-05-14. You will need to have the
same or compatible models on the Cisco IOS XR device you're running this
playbook against.

https://github.com/robshakir/pyangbind > 0.8.1

Requires the following collections if you intend to run against devices:
* `community.yang` is required for the `pb-netconf_info` playbook.
* `junipernetworks.junos` is required for the `pb-juniper` playbook.

## Included content

### Filter plugins

`filter_plugins/oc_intf.py` transforms our YAML inventory to OpenConfig.

## Using the playbooks

If you're only interested to see the techniques or you don't have any network
devices. You can still run these as-is and see the generated XML that would be
deployed using NETCONF.

If you are going to run these against actual devices you'll have to modify the
following:

- If you're going to run these playbooks you'll need one Juniper router and one
  Cisco IOS XR router, called `juniper-r1` and `cisco-r1` in the inventory.
- Modify the inventory in `environments/dev/hosts.yml` with their credentials.
- Modify `environments/dev/host_vars/*.yml`
- Look at ansible.cfg and make any additional changes as per required for your environment.

In order for Ansible to find the `oc_output` Python module we need to add the
`filter_plugins/` folder to the search path.

```
$ export PYTHONPATH=`pwd`/filter_plugins
```

### Display NETCONF schemas and download models from hosts

```
$ ansible-playbook pb-netconf_info.yml
```

### Deploy config to IOS XR using OpenConfig

```
$ ansible-playbook pb-cisco.yml
```

### Deploy config as templated XML over NETCONF

```
$ ansible-playbook pb-juniper.yml
```

## Roadmap

This is provided as an example and is not intended to be maintained or
developed further.

I might add an example using gNMI, only time will tell.

## Licensing

Copyright (c) 2021 Andreas Lundin, lunde@dreamhosted.se

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
