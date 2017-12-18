# Copyright (c) 2013, DPI and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns = get_colums()
	validate_filters(filters)
	data = get_data(filters)
	return columns, data

def validate_filters(filters):
	if filters.from_date > filters.to_date:
		frappe.throw(_("From Date must be before To Date"))


def  get_colums():
	columns =["Date:Data:95"]+["Email:data:130"]+["Lorry No:Link/Carrier"]+["Trip No:Data:60"]+["D/O No:data:80"]+["Start Time:Time:90"]+["Stop Time:Time:90"]+["Trip Duration:Time:90"]+["Status:Select:100"]+["Driver:data:120"]+["Driver Id:Link/Driver:60"]+["Delivery Schedule:data:120"]+["Customer:Link/Customer:120"]+["Address:data:200"]+["Mobile No:Data:120"]+["Contact No:Data:120"]\
						 +["Is Return:data:100"]+["Remark:data:250"]
	return columns


def get_data(filters):
	# date = filters.get("from_date")
	filter_condition = ""
	# filter_condition += " where date = '" + filters.get("from_date") + "'"
	if filters.get("from_date"):
		filter_condition += " where date BETWEEN '"+ filters.get("from_date")+"'AND'"+filters.get("to_date")+"'"


	dl = frappe.db.sql("""select 
		DATE_FORMAT(date,"%d-%m-%Y"),email,carrier,trip,delivery_note_no,
		TIME_FORMAT(start_time,"%H:%m"),
		TIME_FORMAT(stop_time,"%H:%m"),
		TIMEDIFF(start_time-stop_time,"%H:%m:%s")status,driver_full_name,driver,name,
		customer_ref,
		CONCAT(address_line_1,' ',address_line_2,' ',address_line_3)AS Address,mobile_no,
		contact_no,is_return,remarks
		from `tabDelivery Schedule`
		{0} 
		 ORDER BY driver,trip,modified desc""".format(filter_condition),as_list=1,debug=1)
	return dl
