#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.25.3")
zapi.login("Admin", "zabbix")
hosts = zapi.host.get({
 "output": [
   "hostid",
   "host"
 ],
 "sortfield": "host"

})
for x in hosts:
 print x["hostid"], "- ", x["host"]
