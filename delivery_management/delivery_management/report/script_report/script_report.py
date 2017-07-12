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

	dl = frappe.db.sql("""select name,date,customer_ref,delivery_note_no,lorry_no,trip,
		contact_person_name,address_line_1,address_line_2,address_line_3,pin_code,contact_no,mobile_no,
		email,remarks from `tabDelivery Schedule` 
			ORDER BY modified desc""",as_list=1,debug=1)
	return dl
	
def  get_colums():
	# columns = ["Sales Invoice:Link/Sales Invoice:120"]+["Date:Date:100"]+ ["Hospital:Link/Hospital:140"] +["Doctor:Link/Doctor:140"]\
	# 	+["Company:Link/Company:125"]+["Patient:Link/Patient:140"]+["Case:Link/Case:90"]+["Net Amount:Currency:120"] + ["Outstanding:Currency:120"]
	columns = ["Delivery Note No:Link/Delivery Schedule:80"]+["Date:Date:80"]+ ["Customer Ref:Data:60"]+ ["Delivery Note:90"]\
	+["Lorry No:100"]+["Trip:Data:100"]+ ["Contact Person Name:Data:80"]+["Address Line 1:Data:150"]\
	+["Address Line 2:60"]+["Address Line 3:60"]+["Pin Code:60"]+["Contact No:60"]+["Mobile No:60"]+["Email:60"]+["Remark:60"]

	return columns

