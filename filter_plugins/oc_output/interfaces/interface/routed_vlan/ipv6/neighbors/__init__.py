# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

from . import neighbor
class neighbors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/routed-vlan/ipv6/neighbors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for list of IPv6 neighbors
  """
  __slots__ = ('_path_helper', '_extmethods', '__neighbor',)

  _yang_name = 'neighbors'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__neighbor = YANGDynClass(base=YANGListType("ip",neighbor.neighbor, yang_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['interfaces', 'interface', 'routed-vlan', 'ipv6', 'neighbors']

  def _get_neighbor(self):
    """
    Getter method for neighbor, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/neighbors/neighbor (list)

    YANG Description: List of IPv6 neighbors
    """
    return self.__neighbor
      
  def _set_neighbor(self, v, load=False):
    """
    Setter method for neighbor, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/neighbors/neighbor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor() directly.

    YANG Description: List of IPv6 neighbors
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ip",neighbor.neighbor, yang_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip",neighbor.neighbor, yang_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)""",
        })

    self.__neighbor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor(self):
    self.__neighbor = YANGDynClass(base=YANGListType("ip",neighbor.neighbor, yang_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)

  neighbor = __builtin__.property(_get_neighbor, _set_neighbor)


  _pyangbind_elements = OrderedDict([('neighbor', neighbor), ])


