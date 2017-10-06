# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Delivery Management",
			"color": "#0080ff",
			"icon": "fa fa-th",
			"icon": "fa fa-car",
			"type": "module",
			"label": _("Delivery Management")
		},
		{
			"module_name": "Reports Module",
			"color": "#0f9155",
			"icon": "fa fa-report",
			"type": "module",
			"label": _("Reports Module")
		},

		{
			"module_name": "Carrier",
			"_doctype": "Carrier",
			"color": "#0f9155",
			"icon": "fa fa-truck",
			"type": "link",
			"link": "List/Carrier"
		},

		{
			"module_name": "Driver",
			"_doctype": "Driver",
			"color": "#cb3fcd",
			"icon": "fa fa-user-circle-o",
			"type": "link",
			"link": "List/Driver"
		},
		{
			"module_name": "User",
			"_doctype": "User",
			"color": "#600080",
			"icon": "fa fa-user",
			"type": "link",
			"link": "List/User"
		},
		{
			"module_name": "Delivery Schedule",
			"_doctype": "Delivery Schedule",
			"color": "#a20c0c",
			"icon": "fa fa-calendar",
			"type": "link",
			"link": "List/Delivery Schedule"
		},
		{
			"module_name": "Upload Delivery Schedule",
			"_doctype": "Upload Delivery Schedule",
			"color": "#03A9F4",
			"icon": "fa fa-upload",
			"type": "link",
			"link": "List/Upload Delivery Schedule"
		},
		{
			"module_name": "Upload Customer",
			"_doctype": "Upload Customer",
			"color": "#03A9F4",
			"icon": "fa fa-upload",
			"type": "link",
			"link": "List/Upload Customer"
		},
		{
			"module_name": "Upload Customer",
			"_doctype": "Upload Customer",
			"color": "#03A9F4",
			"icon": "fa fa-upload",
			"type": "link",
			"link": "List/Upload Customer"
		},
		{
			"module_name": "Driver Dashboard",
			"color": "#ecd843",
			"icon": "fa fa-th",
			"icon": "fa fa-map-marker",
			"type": "page",
			"link": "driverdashboard",
			"label": _("Driver Dashboard")
		},
		{
			"module_name": "Driver Route Dashboard",
			"color": "#ffa414",
			"icon": "fa fa-th",
			"icon": "fa fa-map-pin",
			"type": "page",
			"link": "driverdashboardroute",
			"label": _("Driver Route Dashboard")
		},
		{
			"module_name": "Delivery Schedule Detail",
			"color": "#561494",
			"icon": "fa fa-th",
			"icon": "fa fa-bar",
			"type": "page",
			"link": "query-report/Delivery Schedule Detail",
			"label": _("Delivery Schedule Report")
		},
	]
