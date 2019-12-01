#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.25.3")
zapi.login("Admin", "zabbix")
# Obtendo lista de hosts
hosts = zapi.host.get({
 "output": [
  "hostid",
  "name"
 ]
})

# Obtendo lista de enderecos IPs
interfaces = zapi.hostinterface.get ({
 "output": [
  "hostid",
  "ip",
  "type"
 ]
})
for vetor_hosts in hosts:
 for vetor_interfaces in interfaces:
  if vertor_interfaces["hostid"] == vetor_hosts['hostid']:
   print vetor_hosts['hostid'],vetor_hosts['name'],"- IP -",vetor_interfaces["ip"]," - Tipo de interface:", vetor_interfaces["type"]
