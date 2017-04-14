from __future__ import unicode_literals
import frappe, os, json
from frappe.utils import cstr
from unidecode import unidecode


@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

@frappe.whitelist(allow_guest=True)
def update_location_for_carrier(name=None,lat=None,lon=None):
	carrier = frappe.get_doc("Carrier", name)
	if carrier.name:
		carrier.flags.ignore_permissions = True
		carrier.latitude = lat
		carrier.longitude = lon
		carrier.save(ignore_permissions=True)
		return "Location updated for the carrier " + carrier.name
	# else : 
	# 	return "Record does not exist"
	
	

@frappe.whitelist(allow_guest=True)
def update_location_for_delivery_order(name=None, carrier=None, lat=None, lon=None):
	delvery_order = frappe.get_doc("Delivery Order", name)
	if delvery_order:
		delvery_order.flags.ignore_permissions = True
		delvery_order.carrier = carrier
		delvery_order.latitude = lat
		delvery_order.longssitude = lon
		delvery_order.save(ignore_permissions=True)
	return "Location updated for the Delivery Order " + delvery_order.name + " and Carrier " + delvery_order.carrier