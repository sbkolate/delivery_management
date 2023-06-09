# Copyright (c) 2013, DPI-Sagar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	columns = get_colums()
	data = get_data()
	return columns, data


def  get_colums():
	columns = ["Driver Id:Link/Driver:120"]+["Driver Name:Data:120"]+["Talkie Number/Contact Number:Data:80"]+["Email Address:Data:150"]+["Driving License Number:Data:100"]+["Carrier:Link/Carrier:100"]
	

	return columns

def get_data():
	dl = frappe.db.sql("""select name,full_name,contact_number,email_address,license_number,carrier
				from `tabDriver` 
				ORDER BY user_id""",as_list=1,debug=1)
	return dl