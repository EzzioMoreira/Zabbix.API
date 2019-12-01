#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.25.3")
zapi.login("Admin", "zabbix")
zapi.hostgroup.massupdate({
  "groups": [
   {
    "groupid": "11"
  }
 ],
  "hosts": [
  {
   "hostid": "10276"
  },
  {
   "hostid": "10278"
  }
 ]
})


