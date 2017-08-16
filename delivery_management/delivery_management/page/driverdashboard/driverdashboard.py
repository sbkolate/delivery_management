from __future__ import unicode_literals
import frappe
from frappe.utils import cstr,now,add_days
import json
import datetime


@frappe.whitelist(allow_guest=True)
def get_driver_locations(carrier=None):
	
	driver_locations = frappe.db.sql(""" select 
		concat("Carrier: ",carrier_number, " <br> : ") as carrier_number,
		CASE
		WHEN name
		THEN (select concat(full_name," - ", name) from tabDriver where carrier = `tabCarrier`.name limit 1)         
		ELSE ""
		END AS mydriver,
		user_id,latitude,longitude, 
		driver from `tabCarrier` 
		where name='{0}' """.format(carrier),as_dict=1)

	# import json
	# k = json.loads(driver_locations)
	# print "k",k.carrier_number
	# k[0]["carrier_number"] = "hello"
	# k[0]["carrier_number"] = k[0]["carrier_number"] + k[0]["mydriver"]
	# print "\nnnnn\n",driver_locations
	return driver_locations