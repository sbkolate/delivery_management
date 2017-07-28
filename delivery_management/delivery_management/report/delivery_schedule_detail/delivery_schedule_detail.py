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
	# columns = columns = ["Delivery Note No:Link/Delivery Schedule:80"]+["Date:Date:95"]+ ["Customer Ref:Data:60"]+ ["Delivery Note:90"]\
	# +["Lorry No:100"]+["Driver:Link/Driver:100"]+["Trip:Data:100"]+ ["Contact Person Name:Data:80"]+["Address:Data:150"]\
	# +["Pin Code:60"]+["Contact No:60"]+["Mobile No:60"]+["Email:60"]+["Remark:60"]
	# return columns

	columns = columns =["Date.:90"]+["Driver:60"]+["Customer:80"]+["Address:Data:150"]+["Contact No:60"]\
						 +["D/O No.:90"]+["Remark:60"]#+["Trip:60"]+["Lorry No:60"]
	return columns

def get_data(filters):
	date = filters.get("date")
	filter_condition = ""
	if filters.get("date"):
		filter_condition += " where date = '" + filters.get("date") + "'"
	if filters.get("driver") and filters.get("date"):
		filter_condition += " and driver = '" + filters.get("driver") +"'"
	elif filters.get("driver"):
		filter_condition += " where driver = '" + filters.get("driver") + "'"
	
	dl = frappe.db.sql("""select date,driver,customer_ref,CONCAT(address_line_1,' ',address_line_2,' ',address_line_3)AS Address,contact_no,delivery_note_no,remarks,trip,lorry_no
		from `tabDelivery Schedule`
		{0} 
		 ORDER BY driver,trip,modified desc""".format(filter_condition),as_list=1)
	
	k=""
	t=""
	for i in dl:
		# print i[1]
		if k!= i[1]:
			dl.insert(dl.index(i),["<b>Date</b>",i[0],"Trip No",i[7],"Lorry No",i[8],"",i[7],""])

		k = i[1]

	
	if dl:
		k = dl[1][7]
	for i in range(1, len(dl)):
		if k!= dl[i][7]:
			k = dl[i][7]
			dl.insert(dl.index(dl[i]),["","","Trip No",dl[i][7],"","","","","","","",""])
		else:
			k = dl[i][7]
	return dl
