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

	def before_insert(self):
		self.create_user()
	
	def set_full_name(self):
		if not self.last_name:
			self.full_name = self.first_name
		else:
			self.full_name = self.first_name + " " + self.last_name

	

	def after_insert(self):
		self.add_driver_restriction()
		if not self.user_id:
			self.user_id = self.email_address

	def create_user(self):
		# self.set_full_name()
		if self.email_address:
			user = frappe.db.get_value("User", self.email_address, "name")
			if not user:
				user_doc = frappe.new_doc("User")
				user_doc.email = self.email_address
				if not self.last_name:
					user_doc.first_name = self.first_name
				else:
					user_doc.first_name = self.first_name + " " + self.last_name
				# user_doc.last_name = self.last_name
				user_doc.user_type = "System User"
				user_doc.flags.ignore_permissions = True
				user_doc.enabled = 1
				user_doc.user_type = "System User"
				user_doc.language = "en"
				user_doc.send_welcome_email = 1
				# user_doc.add_roles('Doctor')
				user_doc.insert()
				user_doc.add_roles('Driver')	
				user_doc.save()

	def add_driver_restriction(self):
		if self.email_address:
			frappe.permissions.add_user_permission("Driver", self.name, self.email_address, with_message=True)

