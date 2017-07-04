# Copyright (c) 2013, DPI-Sagar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	columns = get_colums()
	data = get_data(filters)

	return columns, data

def  get_colums():
	columns = ["Delivery Note No:Data:120"]+["Date:Date:80"]+ ["Trip:Data:60"]+ ["Lorry No:Link/Delivery Schedule:90"]\
	+["Driver:Link/Driver:100"]+["Contact Name:Data:100"]+ ["Contact No:Data:80"]+["Customer Address:Data:150"]\
	+["Pin Code:Int:60"]+["Remarks:Data:100"]+["Delivery Schedule:Link/Delivery Schedule:100"]

	return columns

def get_data(filters):
	date = filters.get("date")
	if filters.get("date"):
		print "\n\ndate",date
		dl = frappe.db.sql("""select delivery_note_no,date,
		trip,lorry_no,driver,customer_ref,contact_no,address,pin_code,remarks, name 
		from `tabDelivery Schedule`
		where date = '{0}' 
		ORDER BY modified desc""".format(date),as_list=1,debug=1)
	else:
		dl = frappe.db.sql("""select delivery_note_no,date,
				trip,lorry_no,driver,customer_ref,contact_no,address,pin_code,remarks,name 
				from `tabDelivery Schedule` 
				ORDER BY driver,trip""",as_list=1,debug=1)
	return dl
