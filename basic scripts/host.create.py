#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.25.3")
zapi.login("Admin", "zabbix")
hostcreated = zapi.host.create({
  "host": "CursoAPI3",
  "status": 1,
  "interfaces": [
   {
    "type": 1,
    "main": 1,
    "useip": 1,
    "ip": "192.168.25.3",
    "dns": "",
    "port": 10050
   }
 ],
 "groups": [
  {
    "groupid": 2
  }
 ],
 "templates": [
 {
    "templatesid": 10001
 }
 ]
})
print "ID do host criado: ", hostcreated["hostids"][0]
