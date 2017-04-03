# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Delivery Management",
			"color": "#669999",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Delivery Management")
		},
		{
			"module_name": "Upload Delivery Schedule",
			"color": "#669999",
			"icon": "fa fa-upload",
			"type": "module",
			"label": _("Upload Delivery Schedule")
		},
		{
			"module_name": "Carrier",
			"_doctype": "Carrier",
			"color": "#607D8B",
			"icon": "fa fa-truck",
			"type": "link",
			"link": "List/Carrier"
		},
		{
			"module_name": "Driver",
			"_doctype": "Driver",
			"color": "#99994d",
			"icon": "fa fa-user",
			"type": "link",
			"link": "List/Driver"
		},
		{
			"module_name": "Product",
			"_doctype": "Product",
			"color": "#ffbf80",
			"icon": "fa fa-product-hunt",
			"type": "link",
			"link": "List/Product"
		},
		{
			"module_name": "Delivery Order",
			"_doctype": "Delivery Order",
			"color": "#009999",
			"icon": "fa fa-file-text-o",
			"type": "link",
			"link": "List/Delivery Order"
		},
		{
			"module_name": "Delivery Request",
			"_doctype": "Delivery Request",
			"color": "#cc9900",
			"icon": "fa fa-file-o",
			"type": "link",
			"link": "List/Delivery Request"
		},
		{
			"module_name": "Delivery Request Item ",
			"_doctype": "Delivery Request Item",
			"color": "#ffcc66",
			"icon": "fa fa-product-hunt",
			"type": "link",
			"link": "List/Delivery Request Item"
		},
		{
			"module_name": "Delivery Order Item",
			"_doctype": "Delivery Order Item",
			"color": "#ffdb4d",
			"icon": "fa fa-product-hunt",
			"type": "link",
			"link": "List/Delivery Order Item"
		},
	]
