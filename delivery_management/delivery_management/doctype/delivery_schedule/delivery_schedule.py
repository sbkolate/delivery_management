# -*- coding: utf-8 -*-
# Copyright (c) 2017, DPI-Sagar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json
from frappe import _
from frappe.model.document import Document
from frappe.desk.form.load import get_attachments
from frappe.core.doctype.communication.email import make

class DeliverySchedule(Document):
	def validate(self):
		if self.lorry_no:
			if not self.carrier:
				self.carrier = self.lorry_no

		carrier_trip = "{0} - {1}".format(self.carrier,self.trip)
		self.carrier_trip = carrier_trip
			
		k = frappe.db.get_value("Driver", {"carrier": self.carrier})
		if k:
			self.driver = k
			self.driver_full_name = frappe.db.get_value("Driver", {"carrier": self.carrier}, "full_name")
			self.driver_user_id = frappe.db.get_value("Driver", {"carrier": self.carrier}, "user_id")

		if self.mobile_no:
			if self.mobile_no[:3] == "+65" or self.mobile_no[:3] == "+91" :
				pass
			else:
				self.mobile_no = "+65"+self.mobile_no



		if self.contact_no:
			if self.contact_no[:3] == "+65" or self.contact_no[:3] == "+91" :
				pass
			else:
				self.contact_no = "+65"+self.contact_no

	def get_attachments(self):
		attachments = [d.name for d in get_attachments(self.doctype, self.name)]
		attachments.append(frappe.attach_print(self.doctype, self.name, doc=self))
		return attachments

	def send_email(self, recipients, sender, subject, message, attachments):
		make(subject = subject, content=message,recipients=recipients,
			sender=sender,attachments = attachments, send_email=True,
		     	doctype=self.doctype, name=self.name)["name"]

		frappe.msgprint(_("Email sent to Customer {0}").format(recipients))


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



			