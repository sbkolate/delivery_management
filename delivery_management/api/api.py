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



@frappe.whitelist(allow_guest=True)
def get_driver_details(name=None):
	driver = frappe.get_doc("Driver", name)
	# if not driver:
	# 	error_msg = {
	# 		"error": "Driver ID" + name +"does not exist..."
	# 	}

	# 	return error_msg

	driver_details = {
		"ID" : driver.name,
		"Full Name": driver.first_name + " " + driver.last_name,
		"Email ": driver.email_address,
		"Contact Number" : driver.contact_number,
		"Assigned Vehicle No.": driver.vehicle_no
		
	}
	return driver_details


@frappe.whitelist(allow_guest=True)
def get_delivery_order_customer_details(name=None):
	delivery_order = frappe.get_doc("Delivery Order", name)
	# if not driver:
	# 	error_msg = {
	# 		"error": "Driver ID" + name +"does not exist..."
	# 	}

	# 	return error_msg

	customer_details = {
		"ID" : delivery_order.name,
		"Full Name": delivery_order.customer
		"Email ": delivery_order.customer.,
		"Contact Number" : driver.contact_number,
		"Assigned Vehicle No.": driver.vehicle_no
		
	}
	return driver_details








# def get_contact_us_api(request):
# 	queryset = ContactUsModel.objects.all()
# 	queryset = serializers.serialize('json', queryset)

# 	to_json = {'queryset' : queryset, }
# 	return HttpResponse(json.dumps(to_json), content_type = 'application/json')

cur_frm.cscript.buyer = function() {
  frappe.geo.doctype.address.address.get_address_display(this.frm, "buyer", "buyer_address");
};

