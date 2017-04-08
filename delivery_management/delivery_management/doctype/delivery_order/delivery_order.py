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
		doc = frappe.get_doc("Delivery Order", "DO-0001")
		for i in doc.product_item:
			print frappe.get_value(i)
		

@frappe.whitelist()
def make_delivery_note(source_name, target_doc=None):
	def set_missing_values(source, target):
		# target.ignore_pricing_rule = 1
		target.run_method("set_missing_values")
		# target.run_method("calculate_taxes_and_totals")

	def update_item(source_doc, target_doc, source_parent):
		# target_doc.base_amount = (flt(source_doc.qty) - flt(source_doc.delivered_qty)) * \
		# 	flt(source_doc.base_rate)
		# target_doc.amount = (flt(source_doc.qty) - flt(source_doc.delivered_qty)) * \
		# 	flt(source_doc.rate)
		target_doc.qty = flt(source_doc.qty) - flt(source_doc.delivered_qty)

	doclist = get_mapped_doc("Delivery Order", source_name, 	{
		"Delivery Order": {
			"doctype": "Delivery Note",
			"validation": {
				"docstatus": ["=", 1]
			}
		},
		"Delivery Order Item": {
			"doctype": "Delivery Note Item",
			"field_map": {
				"name": "si_detail",
				"parent": "against_delivery_request",
				"serial_no": "serial_no",
				"delivery_order": "against_delivery_order",
				"so_detail": "so_detail"
			},
			"postprocess": update_item,
			"condition": lambda doc: doc.delivered_by_supplier!=1
		},
		# "Sales Taxes and Charges": {
		# 	"doctype": "Sales Taxes and Charges",
		# 	"add_if_empty": True
		# },
		# "Sales Team": {
		# 	"doctype": "Sales Team",
		# 	"field_map": {
		# 		"incentives": "incentives"
		# 	},
		# 	"add_if_empty": True
		# }
	}, target_doc, set_missing_values)

	return doclist