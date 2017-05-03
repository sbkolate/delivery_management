from __future__ import unicode_literals
import frappe, os, json


@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

@frappe.whitelist(allow_guest=True)
def update_location_for_delivery_order(name=None, carrier=None, lat=None, lon=None):
	delivery_order = frappe.get_doc("Delivery Order", name)
	if delivery_order:
		delivery_order.flags.ignore_permissions = True
		delivery_order.carrier = carrier
		delivery_order.latitude = lat
		delivery_order.longssitude = lon
		delivery_order.save(ignore_permissions=True)
	return "Location updated for the Delivery Order " + delivery_order.name + " and Carrier " + delivery_order.carrier


@frappe.whitelist(allow_guest=True)
def get_delivery_order_customer_details(name=None):
	delivery_order = frappe.get_doc("Delivery Order", name)
	customer = frappe.get_doc("Customer", delivery_order.customer)
	# address = frappe.get_doc("Address", delivery_order.customer_address)
	customer_details = {
		"id" : delivery_order.name,
		"customer_name": delivery_order.customer,
		"customer_address" : delivery_order.customer_address,
		"address": delivery_order.address_display,
		"shipping_address_name": delivery_order.shipping_address_name,
		"shipping_address": delivery_order.shipping_address_display,
		"contact_person" : delivery_order.contact_person,
		"mobile_number": delivery_order.mobile_no,
		"driver":delivery_order.transporter_name,
		"carrier": delivery_order.vehicle_no,
		"carrier_dispatch_details":delivery_order.dispatch_date,
	}
	return customer_details