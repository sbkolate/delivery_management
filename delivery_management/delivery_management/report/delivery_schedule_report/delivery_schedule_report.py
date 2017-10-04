# Copyright (c) 2013, DPI and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	columns = get_colums()
	data = get_data(filters)
	return columns, data

def  get_colums():
	columns =["Date:Data:95"]+["Driver:data:120"]+["Customer:data:120"]+["Address:data:200"]+["Contact No:Data:90"]\
						 +["D/O No:data:80"]+["Remark:data:250"]+["Trip:Data:60"]#+["Lorry No:60"] + ["name:Data:120"]
	return columns


def get_data(filters):
	date = filters.get("date")
	filter_condition = ""
	if filters.get("date"):
		filter_condition += " where date = '" + filters.get("date") + "'"


	dl = frappe.db.sql("""select 
		DATE_FORMAT(date,"%d-%m-%Y"),driver_full_name,
		customer_ref,
		CONCAT(address_line_1,' ',address_line_2,' ',address_line_3)AS Address,
		contact_no,delivery_note_no,
		remarks,trip,
		carrier, name
		from `tabDelivery Schedule`
		{0} 
		 ORDER BY driver,trip,modified desc""".format(filter_condition),as_list=1,debug=1)
	return dl
