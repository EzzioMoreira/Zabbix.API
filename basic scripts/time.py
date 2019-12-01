#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.25.3")
zapi.login("Admin", "zabbix")
print time.mktime(time.strptime('30/12/2019 14:04:56', '%d/%m%Y%H:%M:%S'))



