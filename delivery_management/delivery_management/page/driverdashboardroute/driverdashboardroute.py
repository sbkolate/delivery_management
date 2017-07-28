from __future__ import unicode_literals
import frappe
from frappe.utils import cstr,now,add_days
import json
import datetime


@frappe.whitelist(allow_guest=True)
def get_driver_route():
	driver_locations = frappe.db.sql(""" select driver_user_id,driver, delivery_note_no,start_lat,start_long,stop_lat,stop_long  from `tabDelivery Schedule`""".format(),as_dict=1)

	return driver_locations