from __future__ import unicode_literals
import frappe
from frappe.utils import cstr,now,add_days
import json
import datetime


@frappe.whitelist(allow_guest=True)
def get_driver_locations():
	driver_locations = frappe.db.sql(""" select concat("Carrier: ",carrier_number, " <br> Driver: ",driver) as carrier_number,driver,user_id,latitude,longitude from `tabCarrier` where disabled=0 """.format(),as_dict=1)

	return driver_locations