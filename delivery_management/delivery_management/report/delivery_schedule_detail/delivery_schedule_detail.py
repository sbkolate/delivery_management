# Copyright (c) 2013, DPI-Sagar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, cstr, date_diff, flt, formatdate, getdate, get_link_to_form

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

	columns =["Date:Data:95"]+["Driver:data:120"]\
			+["Customer:Link/Customer:120"]+["Address:data:200"]\
			+["Contact Person Name:Data:130"]+["Mobile No:Data:130"]\
			+["D/O No:data:80"]+["Remark:data:250"]+["Trip:Data:60"]#+["Lorry No:60"] + ["name:Data:120"]
	return columns

def get_data(filters):
	date = filters.get("date")
	filter_condition = ""
	if filters.get("date"):
		filter_condition += " where date = '" + filters.get("date") + "'"
	
	if filters.get("date") and filters.get("carrier"):
		filter_condition += " and carrier = '" + filters.get("carrier") +"'"
		print("################")
		print(filter_condition)

	elif filters.get("carrier"):
		filter_condition += " where carrier = '" + filters.get("carrier") + "'"
	
	dl = frappe.db.sql("""select 
		DATE_FORMAT(date,"%d-%m-%Y"),driver_full_name,
		customer_ref,
		CONCAT(COALESCE(address_line_1,''),' ',COALESCE(address_line_2,''),' ',COALESCE(address_line_3,''))AS Address,
		contact_person_name,mobile_no,delivery_note_no,
		remarks,trip,
		carrier, name
		from `tabDelivery Schedule`
		{0} 
		 ORDER BY driver,trip,modified desc""".format(filter_condition),as_list=1,debug=1)
	print "\n\nddl",dl
	k=""
	t=""
	for i in dl:
		# print i[7]
		if k!= i[8]:
			dl.insert(dl.index(i),[(i[0]),i[1],"<b>Trip No</b>",i[8],"","Lorry No",i[9],"-",i[8],"flag"])
		k = i[8]

	
	# if dl:
	# 	k = dl[1][7]
	# for i in range(1, len(dl)):
	# 	if k!= dl[i][7]:
	# 		k = dl[i][7]
	# 		print "hi"
	# 		print "k",k
	# 		print "\nndl",dl[i]
	# 		dl.insert(dl.index(dl[i]),[dl[i][0],dl[i][1],"Trip No",dl[i][7],"","","","","","","",""])
	# 	else:
	# 		k = dl[i][7]
	return dl
