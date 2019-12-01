#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.25.3")
zapi.login("Admin", "zabbix")
zapi.host.massadd({
 "hosts": [
  {
   "hostid": 10271
  },
  {
   "hostid": 10276
  }
 ],
 "templates": [
  {
   "templateid": 10131
  }
 ]
}) 
