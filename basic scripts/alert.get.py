#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.25.3")
zapi.login("Admin", "zabbix")
alert = zapi.alert.get({
 "output": "extend",
 "search": {
  "message": "ssh"
 },
 "actionids": "7",
 "countOutput": "True",
})
print "Numero de vezes que a opcao foi disparada: ", alert

