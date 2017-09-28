# -*- coding: utf-8 -*-
# Copyright (c) 2015, DPI-Sagar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, add_days, date_diff
from frappe import _
from frappe.utils.csvutils import UnicodeWriter
from frappe.model.document import Document
import datetime

class UploadDeliverySchedule(Document):
	pass

@frappe.whitelist()
def get_template():
	if not frappe.has_permission("Delivery Schedule", "create"):
		raise frappe.PermissionError

	args = frappe.local.form_dict

	w = UnicodeWriter()
	w = add_header(w)

	w = add_data(w, args)

	# write out response as a type csv
	frappe.response['result'] = cstr(w.getvalue())
	frappe.response['type'] = 'csv'
	frappe.response['doctype'] = "Delivery Schedule"

def add_header(w):
	w.writerow(["Notes:"])
	w.writerow(["Please do not change the template headings"])
	w.writerow(["ID", "Date", "Customer Ref", "Address Line 1", "Address Line 2", "Address Line 3",
		 "Contact Person Name", "Mobile No", 
		 "Contact No", "Delivery Note No", "Email",
		 "Lorry No",  "Trip","Remarks",
		 "Pin Code","Is Return"])
	# w.writerow(["ID", "Date", "Customer Ref", "Delivery Note No", "Lorry No", "Trip",
	# 	 "Contact Person Name", "Address Line 1", "Address Line 2", "Address Line 3", 
	# 	 "Pin Code", "Contact No", "Mobile No", "Email", "Remarks"])
	return w

def add_data(w, args):
	customers = get_active_customers()
	existing_attendance_records = get_existing_attendance_records(args)
	for customer in customers:
		existing_attendance = {}
		if existing_attendance_records \
			and tuple([date, customer.name]) in existing_attendance_records:
				existing_attendance = existing_attendance_records[tuple([date, customer.name])]
		row = [
			existing_attendance and existing_attendance.name or "",
			customer.name, customer.first_name, date,
			existing_attendance and existing_attendance.status or "",
			existing_attendance and existing_attendance.leave_type or "", customer.first_name,
			existing_attendance and existing_attendance.naming_series or get_naming_series(),
		]
		w.writerow(row)
	return w

def get_active_customers():
	customers = frappe.db.sql("""select name, first_name, customer_group, customer_type, territory
		from `tabCustomer` where docstatus < 2 and status = 'Enabled' """, as_dict=1)
	return customers

def get_existing_attendance_records(args):
	schedule = frappe.db.sql("""select name, date, customer_ref, delivery_note_no, lorry_no, contact_person_name
		from `tabDelivery Schedule` where docstatus < 2""", as_dict=1)

	existing_attendance = {}
	for att in schedule:
		existing_attendance[tuple([att.date, att.customer_ref])] = att

	return existing_attendance

def get_naming_series():
	series = frappe.get_meta("Delivery Schedule").get_field("naming_series").options.strip().split("\n")
	if not series:
		frappe.throw(_("Please setup numbering series for Attendance via Setup > Numbering Series"))
	return series[0]


@frappe.whitelist()
def upload():
	if not frappe.has_permission("Delivery Schedule", "create"):
		raise frappe.PermissionError

	from frappe.utils.csvutils import read_csv_content_from_uploaded_file
	from frappe.modules import scrub

	rows = read_csv_content_from_uploaded_file()
	rows = filter(lambda x: x and any(x), rows)
	if not rows:
		msg = [_("Please select a csv file")]
		return {"messages": msg, "error": msg}
	columns = [scrub(f) for f in rows[2]]
	columns[0] = "name"
	columns[1] = "date"
	ret = []
	error = False

	from frappe.utils.csvutils import check_record, import_doc

	for i, row in enumerate(rows[3:]):
		if not row: continue
		row_idx = i + 3
		d = frappe._dict(zip(columns, row))
		d["doctype"] = "Delivery Schedule"
		d["customer_ref"] = row[2]
		d["is_return"] = row[15]

		import datetime
		new_date = datetime.datetime.strptime(row[1],'%d-%b-%y').strftime('%d-%m-%Y')
		d["date"] = new_date

		if d.name:
			d["docstatus"] = frappe.db.get_value("Delivery Schedule", d.name, "docstatus")

		try:
			check_record(d)
			ret.append(import_doc(d, "Delivery Schedule", 1, row_idx, submit=False))
		except Exception, e:
			error = True
			ret.append('Error for row (#%d) %s : %s' % (row_idx,
				len(row)>1 and row[1] or "", cstr(e)))
			frappe.errprint(frappe.get_traceback())

	if error:
		frappe.db.rollback()
	else:
		frappe.db.commit()
	return {"messages": ret, "error": error}
