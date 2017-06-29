# Copyright (c) 2013, indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
	columns, data = [], []
	columns = get_colums()
	data = get_data(filters)
	return columns, data

def get_data(filters):
		# dl = frappe.db.sql("""select name, posting_date, customer,doctor,company,patient_full_name,case,base_grand_total, outstanding_amount FROM
		# 		`tabSales Invoice` Where doctor = '{0}' and docstatus=1 ORDER BY modified desc""".format(filters.get("doctor")),as_list=1,debug=1)

	dl = frappe.db.sql("""select name,date,trip,lorry_no,driver,customer_ref,contact_no,address,pin_code,remarks from `tabDelivery Schedule` 
			ORDER BY modified desc""",as_list=1,debug=1)
	return dl
	
def  get_colums():
	# columns = ["Sales Invoice:Link/Sales Invoice:120"]+["Date:Date:100"]+ ["Hospital:Link/Hospital:140"] +["Doctor:Link/Doctor:140"]\
	# 	+["Company:Link/Company:125"]+["Patient:Link/Patient:140"]+["Case:Link/Case:90"]+["Net Amount:Currency:120"] + ["Outstanding:Currency:120"]
	columns = ["Delivery Note No:Link/Delivery Schedule:80"]+["Date:Date:80"]+ ["Trip:Data:60"]+ ["Lorry No:Link/Delivery Schedule:90"]\
	+["Driver:Link/Driver:100"]+["Contact Name:Data:100"]+ ["Contact No:Data:80"]+["Customer Address:Data:150"]\
	+["Pin Code:Int:60"]+["Remarks:Data:100"]	

	return columns

