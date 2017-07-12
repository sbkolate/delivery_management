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
	columns = columns = ["Delivery Note No:Link/Delivery Schedule:80"]+["Date:Date:95"]+ ["Customer Ref:Data:60"]+ ["Delivery Note:90"]\
	+["Lorry No:100"]+["Driver:Link/Driver:100"]+["Trip:Data:100"]+ ["Contact Person Name:Data:80"]+["Address Line 1:Data:150"]\
	+["Address Line 2:60"]+["Address Line 3:60"]+["Pin Code:60"]+["Contact No:60"]+["Mobile No:60"]+["Email:60"]+["Remark:60"]
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
	
	dl = frappe.db.sql("""select name,date,customer_ref,delivery_note_no,lorry_no,driver,trip,
		contact_person_name,address_line_1,address_line_2,address_line_3,pin_code,contact_no,mobile_no,email,remarks
		from `tabDelivery Schedule`
		{0} 
		 ORDER BY driver,trip,modified desc""".format(filter_condition),as_list=1)
	print("@@@@@@@@############@@@@@@@@@@@@")
	print type(dl)
	print(dl)

	
	k=""
	t=""
	for i in dl:
		print i[5]
		if k!= i[5]:
			dl.insert(dl.index(i),["<b>Date</b>",i[1],"Trip No",i[6],"Lorry No",i[4],"","","","","","","","",])

		k = i[5]

	# for i in dl:
	# 	if i[0] == "<b>Date</b>":
			
	# 		dl.insert((dl.index(i)+1),["","","","","","","","","","","","","","","","","",""])
	if dl:
		k = dl[0][6]
	for i in dl:
		print i[6]
		if k!= i[6]:
			dl.insert(dl.index(i),["","","","","","","Trip No",i[6],"","","","","","","",""])

		k = i[6]
		



	

	return dl
