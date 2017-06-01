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
	if doc.company_name:
		doc.customer_name = doc.company_name
	doc.save(ignore_permissions=True)
	# if not doc.address_title or not doc.address_line_1 or not doc.city:
	# 	frappe.msgprint("Address Title, Address Line 1 and City are mandatory")

	# existing_address_title = frappe.db.get_value("Address", doc.address_title)
	# if existing_address_title == doc.address_title:
	# 	frappe.msgprint("Duplicate entry for {0} " + doc.address_title + " Address Title must be unique")
	if doc.address_line_1:
		address_doc = frappe.new_doc("Address")
		address_doc.address_title = doc.customer_name
		address_doc.address_line1 = doc.address_line_1
		address_doc.address_line2 = doc.address_line_2
		address_doc.address_line_3 = doc.address_line_3
		address_doc.city = doc.city
		address_doc.pincode = doc.pin_code
		address_doc.email_id = doc.email
		address_doc.mobile_no = doc.mobile_no
		address_doc.phone = doc.phone
		address_doc.fax = doc.fax

		customer_link = {
			"doctype": "Dynamic Link",
			"link_doctype": "Customer",
			"link_name": doc.name,
			"link_title": doc.customer_name,
			}
		address_doc.append("links", customer_link)
		address_doc.save(ignore_permissions=True)
		# frappe.msgprint("Address is created for " + address_doc.address_title)

	# existing_first_name = frappe.db.get_value("Contact", doc.first_name)
	# if existing_first_name == doc.first_name:
	# 	frappe.msgprint("Duplicate entry for {0} " + doc.first_name + " Contact Person's first name must be unique")
		
	
@frappe.whitelist()
def create_delivery_contact(doc, method):
	if doc.contact_person_name:
		contact_doc = frappe.new_doc("Contact")
		contact_doc.first_name = doc.contact_person_name
		contact_doc.last_name = " "
		contact_doc.email_id = doc.email
		contact_doc.status = "Passive"
		contact_doc.phone = doc.phone
		contact_doc.mobile_no = doc.mobile_no

		customer_link = {
			{"doctype": "Dynamic Link",
			"link_doctype": "Delivery Schedule",
			"link_name": doc.name,
			"link_title": doc.customer_name,
			},
			{"doctype": "Dynamic Link",
			"link_doctype": "Customer",
			"link_name": doc.customer_ref,
			}
			}
		contact_doc.append("links", customer_link)
		contact_doc.save(ignore_permissions=True)

		if doc.address_line_1:
			address_doc = frappe.new_doc("Address")
			address_doc.address_title = doc.contact_name
			address_doc.address_line1 = doc.address_line_1
			address_doc.address_line2 = doc.address_line_2
			address_doc.address_line3 = doc.address_line_3
			address_doc.city = "Singapore"
			address_doc.pincode = doc.pin_code
			address_doc.email_id = doc.email
			address_doc.mobile_no = doc.mobile_no

			customer_link = {
				{
					"doctype": "Dynamic Link",
					"link_doctype": "Delivery Schedule",
					"link_name": doc.name,
					"link_title": doc.customer_name,
				},
				{
					"doctype": "Dynamic Link",
					"link_doctype": "Customer",
					"link_name": doc.customer_ref,
				}
				}

			address_doc.append("links", customer_link)
			address_doc.save(ignore_permissions=True)
		# frappe.msgprint("Contact is created " + contact_doc.first_name)


