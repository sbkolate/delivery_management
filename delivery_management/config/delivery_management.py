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
	]
