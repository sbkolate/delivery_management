# -*- coding: utf-8 -*-
# Copyright (c) 2015, DPI-Sagar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

import json
from datetime import timedelta
# from erpnext.controllers.queries import get_match_cond
from frappe.utils import flt, time_diff_in_hours, get_datetime, getdate, today, cint, get_datetime_str
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class DeliveryOrder(Document):
	
	def validate(self):
		pass
		

# @frappe.whitelist()
# def make_delivery_note(source_name, target_doc=None, ignore_permissions=False):
# 	def set_missing_values(source, target):
# 		name=frappe.db.get_value("Delivery Order",{"customer_name":source.customer},"customer_name")
# 		target.customer = source.customer
# 		target.company = source.company
# 		target.shipping_date = today()
# 		target.shipping_address = source.address
# 		target.set('product_item', [])
	
# 		for item in source.product_item:
			# task_map = {
			# 	"product_code": item.product_code,
			# 	"product_name": item.product_name
			# 	"description" = item.description
			# 	"quantity" = item.quantity
			# }
			# target.append("product_item", task_map)
	# 		product_code = item.product_code
	# 		product_name = item.product_name
	# 		description = item.description
	# 		quantity = item.quantity
	# 		target.append('product_item', 
	# 			{"product_code":product_code, "product_name":product_name,
	# 			"description":description, "quantity":quantity})						


		# def update_item(source_doc, target_doc, source_parent):
		# 	target_doc.qty = flt(source_doc.qty) - flt(source_doc.delivered_qty)


		# doclist = get_mapped_doc("Delivery Order", source_name, 	{
		# 	"Delivery Order": {
		# 		"doctype": "Delivery Note",
		# 		"validation": {
		# 			"docstatus": ["=", 0]
		# 		}
		# 	},
		# 	"Delivery Order Item": {
		# 		"doctype": "Delivery Note Item",
		# 		"add_if_empty": True,
		# 	},
		
		# }, target_doc, set_missing_values, ignore_permissions=False)

	# return doclist