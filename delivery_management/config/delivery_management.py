from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Delivery Schedule",
					"description": _("Schedule"),
				},
				{
					"type": "doctype",
					"name": "Carrier",
					"description": _("Carrier"),
				},
				{
					"type": "doctype",
					"name": "Driver",
					"description": _("Driver"),
				},
				{
					"type": "doctype",
					"name": "Return Delivery",
					"description": _("Return Delivery"),
				},				
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer"),
				},
				{
					"type": "doctype",
					"name": "User",
					"description": _("User"),
				},
			]
		},

		

		{
			"label": _("Tools"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Upload Customer",
					"description": _("Upload Customer"),
				},
				{
					"type": "doctype",
					"name": "Upload Delivery Schedule",
					"description": _("Upload Delivery Schedule"),
				},
			]
		},
		{
			"label": _("Reports & Dashboard"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Delivery Schedule Tracking",
					"doctype": "Delivery Schedule"
				},
				# {
				# 	"type": "report",
				# 	"is_query_report": True,
				# 	"name": "Driver Trip Details",
				# 	"doctype": "Delivery Schedule"
				# },
				{
					"type": "report",
					"is_query_report": True,
					"name": "Delivery Schedule Detail",
					"doctype": "Delivery Schedule"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Driver Details",
					"doctype": "Driver"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Delivery Schedule Report",
					"doctype": "Delivery Schedule"
				},
				{
					"type": "page",
					"name": "driverdashboard",
					"label": _("Driver Dashboard"),
					"icon": "fa fa-bar-chart",
				},

				{
					"type": "page",
					"name": "driverdashboardroute",
					"label": _("Driver Route Dashboard"),
					"icon": "fa fa-bar-chart",
				},
			]
		},
		{
			"label": _("App Page"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "About",
					"description": _("About"),
				},

			]
		},
	]
