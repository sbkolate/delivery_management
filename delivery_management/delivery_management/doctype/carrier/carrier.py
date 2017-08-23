# -*- coding: utf-8 -*-
# Copyright (c) 2015, DPI-Sagar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.desk.reportview import get_match_cond, get_filters_cond
from frappe.utils import nowdate
from collections import defaultdict

class Carrier(Document):
	def validate(self):
		self.carrier_no = self.carrier_number

def get_carrier(doctype, txt, searchfield, start, page_len, filters):
	conditions = []
	return frappe.db.sql("""select name,type,registration_year, 
		CASE
		when 1=1
		then (select full_name from tabDriver where carrier = tabCarrier.name limit 1)
		ELSE
		""
		END AS driver,
		CASE
		when 1=1
		then (select user_id from tabDriver where carrier = tabCarrier.name limit 1)
		ELSE
		""
		END AS user_id
		from `tabCarrier`
		where 
			({key} like %(txt)s
				or name like %(txt)s 
				or type like %(txt)s
				or driver like %(txt)s 
				or user_id like %(txt)s)
			{fcond} {mcond}
		order by
			idx desc,
			name
		limit %(start)s, %(page_len)s""".format(**{
			'key': searchfield,
			'fcond': get_filters_cond(doctype, filters, conditions),
			'mcond': get_match_cond(doctype)
		}), {
			'txt': "%%%s%%" % txt,
			'_txt': txt.replace("%", ""),
			'start': start,
			'page_len': page_len
		})