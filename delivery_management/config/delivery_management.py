from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "fa fa-star",
			"items": [
				# {
				# 	"type": "doctype",
				# 	"name": "Delivery Request",
				# 	"description": _("Delivery Request"),
				# },
				# {
				# 	"type": "doctype",
				# 	"name": "Delivery Order",
				# 	"description": _("Delivery Order"),
				# },
				# {
				# 	"type": "doctype",
				# 	"name": "Upload Delivery Schedule",
				# 	"description": _("Upload Delivery Schedule"),
				# },											
			]
		},

		{
			"label": _("Master"),
			"icon": "fa fa-star",
			"items": [
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
					"name": "Delivery Schedule",
					"description": _("Schedule"),
				},
				{
					"type": "doctype",
					"name": "Product",
					"description": _("Product"),
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
			"label": _("Reports"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Delivery Schedule Details",
					"doctype": "Delivery Schedule"
				},
			]
		},
	]
