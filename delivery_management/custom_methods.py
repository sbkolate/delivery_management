import frappe
from frappe.model.mapper import get_mapped_doc
from frappe import throw, _

@frappe.whitelist()
def set_contact_full_name(doc, method):
	if not doc.last_name:
		doc.full_name = doc.first_name
	else:
		doc.full_name = doc.first_name + " " + doc.last_name

@frappe.whitelist()
def create_address(doc, method):
	if not doc.address_title or not doc.address_line_1 or not doc.city:
		frappe.throw("Address Title, Address Line 1 and City are mandatory fields, Please fill all mandatory fields.")

	existing_address_title = frappe.db.get_value("Address", doc.address_title)
	if existing_address_title == doc.address_title:
		frappe.throw("Duplicate entry for {0} " + doc.address_title + " Address Title must be unique")
	
	if doc.address_title and doc.address_line_1 and doc.city:
		address_doc = frappe.new_doc("Address")
		address_doc.address_title = doc.address_title
		address_doc.address_line1 = doc.address_line_1
		address_doc.address_line2 = doc.address_line_2
		address_doc.address_line3 = doc.address_line_3
		address_doc.city = doc.city
		address_doc.pincode = doc.pin_code
		address_doc.save(ignore_permissions=True)
		return frappe.msgprint("Address is created for " + address_doc.address_title)

@frappe.whitelist()
def create_contact(doc, method):
	if not doc.first_name:
		frappe.throw("First Name is a mandatory field, Please fill the mandatory field.")

	existing_first_name = frappe.db.get_value("Contact", doc.first_name)
	if existing_first_name == doc.first_name:
		frappe.throw("Duplicate entry for {0} " + doc.first_name + " Contact Person's first name must be unique")
		
	if doc.first_name:
		contact_doc = frappe.new_doc("Contact")
		contact_doc.first_name = doc.first_name
		contact_doc.last_name = doc.last_name
		contact_doc.email_id = doc.email_address
		contact_doc.status = "Passive"
		contact_doc.phone = doc.phone
		contact_doc.mobile_no = doc.mobile_no
		contact_doc.save(ignore_permissions=True)
		return frappe.msgprint("Contact is created " + contact_doc.first_name)