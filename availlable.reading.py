#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.25.3")
zapi.login("Admin", "zabbix")
reading = zapi.host.isreadable([
  10267,
  10268
 ])
if reading:
 print reading, "- Host(s) disponíveis para leitura."
else:
 print reading, "- Host(s) nao disponiveis para leitura."

