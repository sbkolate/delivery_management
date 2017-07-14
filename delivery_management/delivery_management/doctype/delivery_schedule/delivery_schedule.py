# -*- coding: utf-8 -*-
# Copyright (c) 2017, DPI-Sagar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DeliverySchedule(Document):
	pass


def get_indicator(self):
		"""Set indicator for portal"""
		if self.status=="Open" and self.docstatus==0:
			self.indicator_color = "Red"
			self.indicator_title = _("Open")
		elif self.status=="In Transit":
			self.indicator_color = "Yellow"
			self.indicator_title = _("In Transit")
		# elif self.created_by_role=="Doctor":
		# 	self.indicator_color = "green"
		# 	self.indicator_title = _("Doctor")	
		else:
			self.indicator_color = "green"
			self.indicator_title = _("Delivered")