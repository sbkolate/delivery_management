from __future__ import unicode_literals
import frappe, os, json

@frappe.whitelist(allow_guest=True)
def ping():
	return "Pong..."

@frappe.whitelist(allow_guest=True)
def get_driver_details(name=None):
	driver = frappe.get_doc("Driver", name)
	driver_details = {
		"ID": driver.name,
		"Full Name": driver.first_name + " " + driver.last_name,
		"Email": driver.email_address,
		"Contact Number": driver.contact_number,
		"Profile Picture": driver.profile_picture,
		"Assigned Vehicle No.": driver.vehicle_no,
	}
	return driver_details