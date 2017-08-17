from __future__ import unicode_literals
import frappe, os, json, json
from frappe import _

@frappe.whitelist(allow_guest=True)
def update_location_for_carrier(name=None,lat=None,lon=None):
	carrier = frappe.get_doc("Carrier", name)
	if carrier.name:
		carrier.flags.ignore_permissions = True
		carrier.latitude = lat
		carrier.longitude = lon
		carrier.save(ignore_permissions=True)
		frappe.db.commit()
		return "Location updated for the carrier " + carrier.name
