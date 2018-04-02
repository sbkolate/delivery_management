# Copyright (c) 2013, DPI and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns = get_colums()
	# validate_filters(filters)
	data = get_data(filters)
	return columns, data

# def validate_filters(filters):
# 	if filters.from_date > filters.to_date:
# 		frappe.throw(_("From Date must be before To Date"))


def  get_colums():
	columns =["Id:Link/Delivery Schedule:95"]+["Date:Data:95"]+["Driver Id:Link/Driver:120"]+["Driver:data:120"]+["Customer:Link/Customer:120"]+["Address:data:200"]+["Mobile No:Data:120"]+["Contact No:Data:120"]\
						 +["D/O No:data:80"]+["Trip:Data:60"]+["Lorry No:Link/Carrier"]+["Is Return:data:100"]+["Remark:data:250"]
	return columns


def get_data(filters):
	# date = filters.get("from_date")
	filter_condition = ""
	# filter_condition += " where date = '" + filters.get("from_date") + "'"
	# if filters.get("from_date"):
	# 	filter_condition += " where date BETWEEN '"+ filters.get("from_date")+"'AND'"+filters.get("to_date")+"'"
	if filters.get("from_date"):
		filter_condition += " where date = '" + filters.get("from_date") + "'"
	
	if filters.get("carrier"):
		filter_condition += " and carrier = '" + filters.get("carrier") +"'"
		print("################")
		print(filter_condition)

	if filters.get("delivery_note_no") or filters.get("carrier"):
		filter_condition += " and delivery_note_no = '" + filters.get("delivery_note_no") +"'"
	# 	print("################")
	# 	print(filter_condition)

	elif filters.get("carrier"):
		filter_condition += " where carrier = '" + filters.get("carrier") + "'"
	
	elif filters.get("delivery_note_no"):
		filter_condition += " where delivery_note_no = '" + filters.get("delivery_note_no") + "'"
	
	dl = frappe.db.sql("""select 
		name,DATE_FORMAT(date,"%d-%m-%Y"),driver,driver_full_name,
		customer_ref,
		CONCAT(address_line_1,' ',address_line_2,' ',address_line_3)AS Address,mobile_no,
		contact_no,delivery_note_no,trip,carrier,is_return,remarks
		from `tabDelivery Schedule`
		{0} 
		 ORDER BY driver,trip,modified desc""".format(filter_condition),as_list=1,debug=1)
	return dl
