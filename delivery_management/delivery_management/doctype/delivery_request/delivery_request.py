# -*- coding: utf-8 -*-
# Copyright (c) 2015, DPI-Sagar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

import json
from datetime import timedelta

from frappe.utils import flt, time_diff_in_hours, get_datetime, getdate, today, cint, get_datetime_str
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class DeliveryRequest(Document):
	def validate(self):
		pass


# @frappe.whitelist()
# def make_delivery_order():
# 	return "hey there js function called me"
	# def set_missing_values(source, target):
		# doclist = get_mapped_doc("Case", source_name, {
		# 	"Case": {
		# 		"doctype": "Sales Invoice",
		# 		"validation": {
		# 			"docstatus": ["=", 1]
		# 		},
		# 	}
		# }, target_doc, set_missing_values, ignore_permissions=False)


@frappe.whitelist()
def make_delivery_order(source_name, target_doc=None):
	frappe.msgprint("helloooo")
	def set_missing_values(source, target):
		# do_name=frappe.db.get_value("Delivery Requset",{"company_name":source.doctor},"company_name")
		# company_cost_center = frappe.db.get_value("Company",{"company_name":source.doctor},"cost_center")
		# company_income_account = frappe.db.get_value("Company",{"company_name":source.doctor},"default_income_account")
		# company_additional_info = frappe.db.get_value("Company",{"company_name":source.company},"additional_info")
		# target.customer = source.customer
		# target.company = source.company
		# target.shipping_date = today()
		# target.set('items', [])
		# k = target.append('items', {})
		# k.name = source_name
		# k.product_code = source.product_code
		# k.product_name = source.product_name
		# k.description = source.description
		# k.quantity = source.quantity
		
				

	doclist = get_mapped_doc("Delivery Request", source_name, {
			"Delivery Request": {
				"doctype": "Delivery Order",
				"validation": {
					"docstatus": ["=", 0]
				},
			}
		}, target_doc, set_missing_values, ignore_permissions=False)
	return doclist
