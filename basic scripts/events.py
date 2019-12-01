#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.25.3")
zapi.login("Admin", "zabbix")
events = zapi.event.get({
 "output": "extend",
 "time_from": "1575223548",#timestamp
 "time_till": "1575212748",#timestamp
 "sortfiel": [
   "clock",
   "eventid",
 ],
 "sortorder": "DESC"
})
print events

