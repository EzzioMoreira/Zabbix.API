#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.25.3")
zapi.login("Admin", "zabbix")
history = zapi.history.get({
  "itemids": [
   29262 
  ],
  "history": 0,
  "output": "extend",
  "time_from": "1575216457",
  "time_till": "1575216457"
})
for x in history:
 print x["clock"], "- ", x["value"]
