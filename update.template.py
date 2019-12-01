#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.25.3")
zapi.login("Admin", "zabbix")
zapi.template.update({
 "templateid": "10111",
 "name": "Template alterado 1",
 "description": "Descricao para template alterado 1"
})

