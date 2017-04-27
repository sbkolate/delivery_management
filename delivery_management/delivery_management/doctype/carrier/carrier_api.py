from __future__ import unicode_literals
import frappe, os, json


@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

@frappe.whitelist(allow_guest=True)
def update_carrier_location(name=None, lat=None, lon=None):
	carrier = frappe.get_doc("Carrier", name)
	if carrier.name:
		carrier.latitude = lat
		carrier.longitude = lon
		carrier.save(ignore_permissions=True)
		return "Location updated for Carrier " + carrier.name 