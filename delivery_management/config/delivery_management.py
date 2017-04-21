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
					"name": "Customer",
					"description": _("Customer"),
				},
				{
					"type": "doctype",
					"name": "Product",
					"description": _("Product"),
				},
				{
					"type": "doctype",
					"name": "User",
					"description": _("User"),
				},
				{
					"type": "doctype",
					"name": "Delivery Request",
					"description": _("Delivery Request"),
				},
				{
					"type": "doctype",
					"name": "Delivery Order",
					"description": _("Delivery Order"),
				},
				{
					"type": "doctype",
					"name": "Upload Delivery Schedule",
					"description": _("Upload Delivery Schedule"),
				},
																
			]
		},

		# {
		# 	"label": _("Reports"),
		# 	"icon": "fa fa-list",
		# 	"items": [
		# 		{
		# 			"type": "report",
		# 			"is_query_report": True,
		# 			"name": "Invoice Details",
		# 			"doctype": "Sales Invoice"
		# 		},
		# 		# {
		# 		# 	"type": "report",
		# 		# 	"is_query_report": True,
		# 		# 	"name": "Clinic Details",
		# 		# 	"doctype": "Clinic"
		# 		# },
		# 		{
		# 			"type": "report",
		# 			"is_query_report": True,
		# 			"name": "Hospital Details",
		# 			"doctype": "Hospital"
		# 		},
		# 		{
		# 			"type": "report",
		# 			"is_query_report": True,
		# 			"name": "Doctor Details",
		# 			"doctype": "Doctor"
		# 		},
		# 		{
		# 			"type": "report",
		# 			"is_query_report": True,
		# 			"name": "Company Details",
		# 			"doctype": "Company"
		# 		},
		# 		{
		# 			"type": "report",
		# 			"is_query_report": True,
		# 			"name": "Surgeon Details",
		# 			"doctype": "Surgeon"
		# 		},
		# 		{
		# 			"type": "report",
		# 			"is_query_report": True,
		# 			"name": "Case Details",
		# 			"doctype": "Case"
		# 		},
		# 		{
		# 			"type": "report",
		# 			"is_query_report": True,
		# 			"name": "Patient Details",
		# 			"doctype": "Patient"
		# 		},
		# 	]
		# },
		# {
		# 	"label": _("Master"),
		# 	"icon": "fa fa-star",
		# 	"items": [
		# 		{
		# 			"type": "doctype",
		# 			"name": "Operation Type",
		# 			"description": _("Operation Type"),
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Procedure Type",
		# 			"description": _("Procedure Type"),
		# 		},
		# 	]
		# },
	]
