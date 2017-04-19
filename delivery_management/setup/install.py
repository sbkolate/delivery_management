from __future__ import unicode_literals
import frappe, os, json
from frappe.utils import cstr
from unidecode import unidecode


@frappe.whitelist(allow_guest=True)
def create_new_role(self):
	if 
	role_doc = frappe.new_doc("Role")
	role_doc.role_name = "Delivery Manager"
	role_doc.desk_access = 1
	role_doc.save(ignore_permissions=True)
