# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Delivery Management",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Delivery Management")
		},
		{
			"module_name": "Carrier",
			"_doctype": "Carrier",
			"color": "#4ad0df",
			"icon": "fa fa-truck",
			"type": "link",
			"link": "List/Carrier"
		},
		{
			"module_name": "Driver",
			"_doctype": "Driver",
			"color": "red",
			"icon": "fa fa-id-card-o",
			"type": "link",
			"link": "List/Driver"
		},
		{
			"module_name": "Product",
			"_doctype": "Product",
			"color": "red",
			"icon": "fa fa-product-hunt",
			"type": "link",
			"link": "List/Product"
		},
		{
			"module_name": "Delivery Order",
			"_doctype": "Delivery Order",
			"color": "green",
			"icon": "fa fa-first-order",
			"type": "link",
			"link": "List/Delivery Order"
		},
		{
			"module_name": "Delivery Request",
			"_doctype": "Delivery Request",
			"color": "blue",
			"icon": "fa fa-first-order",
			"type": "link",
			"link": "List/Delivery Request"
		},
		{
			"module_name": "Delivery Request Item ",
			"_doctype": "Delivery Request Item",
			"color": "blue",
			"icon": "fa fa-product-hunt",
			"type": "link",
			"link": "List/Delivery Request Item"
		},
		{
			"module_name": "Delivery Order Item",
			"_doctype": "Delivery Order Item",
			"color": "blue",
			"icon": "fa fa-product-hunt",
			"type": "link",
			"link": "List/Delivery Order Item"
		},
	]
