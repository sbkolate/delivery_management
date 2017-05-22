# -*- coding: utf-8 -*-
# Copyright (c) 2015, DPI-Sagar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
# from frappe import throw, _

class Driver(Document):
	def validate(self):
		self.set_full_name()

	def set_full_name(self):
		if not self.last_name:
			self.full_name = self.first_name
		else:
			self.full_name = self.first_name + " " + self.last_name