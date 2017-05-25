import frappe
from frappe.model.mapper import get_mapped_doc
from frappe import throw, _

@frappe.whitelist()
def set_contact_full_name(doc, method):
	if not doc.last_name:
		doc.full_name = doc.first_name
	else:
		doc.full_name = doc.first_name + " " + doc.last_name