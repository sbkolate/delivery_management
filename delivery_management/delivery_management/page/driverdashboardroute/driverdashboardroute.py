from __future__ import unicode_literals
import frappe
from frappe.utils import cstr,now,add_days
import json
import datetime


@frappe.whitelist(allow_guest=True)
def get_driver_route(delivery_schedule=None):
	driver_locations = frappe.db.sql("""select driver_user_id,driver, 
		delivery_note_no,start_lat,start_long,stop_lat,stop_long,driving_path 
		from `tabDelivery Schedule`
		where name = '{0}'""".format(delivery_schedule),as_dict=1)

	return driver_locations