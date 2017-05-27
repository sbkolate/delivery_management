# -*- coding: utf-8 -*-
# Copyright (c) 2017, DPI-Sagar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, add_days, date_diff
from frappe import _
from frappe.utils.csvutils import UnicodeWriter
from frappe.model.document import Document


class UploadCustomer(Document):
	pass

@frappe.whitelist()
def get_template():
	if not frappe.has_permission("Customer", "create"):
		raise frappe.PermissionError

	args = frappe.local.form_dict

	w = UnicodeWriter()
	w = add_header(w)

	w = add_data(w, args)
	w = add_address(w, args)

	# write out response as a type csv
	frappe.response['result'] = cstr(w.getvalue())
	frappe.response['type'] = 'csv'
	frappe.response['doctype'] = "Customer"

def add_header(w):
	w.writerow(["Notes:"])
	w.writerow(["Please do not change the template headings"])
	w.writerow(["Status should be one of these values: "])
	w.writerow(["If you are overwriting existing attendance records, 'ID' column mandatory"])
	w.writerow(["ID", "Customer Name", "Customer Group", "Type",
		 "Territory", "Address Title", "Address Line 1", "Address Line 2", "Address Line 3", 
		 "City", "Pin Code", "Contact No", "First Name", "Last Name", "Mobile No", "Email", "Fax"])
	return w

def add_data(w, args):
	customers = get_active_customers()
	existing_customer_records = get_existing_customer_records(args)
	for customer in customers:
		existing_customer = {}
		if existing_customer_records \
			and tuple([name, customer.customer_name]) in existing_customer_records:
				existing_customer = existing_customer_records[tuple([name, customer.customer_name])]
		row = [
			existing_customer and existing_customer.name or "",
			customer.name, customer.customer_name, date,
			existing_customer and existing_customer.status or "",
			existing_customer and existing_customer.leave_type or "", customer.customer_name,
			existing_customer and existing_customer.naming_series or get_naming_series(),
		]
		w.writerow(row)
	return w

def add_address(w, args):
	existing_customer_records = get_existing_customer_records(args)
	for customer in customers:
		existing_customer = {}
		if existing_customer_records \
			and tuple([name, customer.customer_name]) in existing_customer_records:
				existing_customer = existing_customer_records[tuple([name, customer.customer_name])]
		row = [
			existing_customer and existing_customer.name or "",
			customer.name, customer.customer_name, date,
			existing_customer and existing_customer.status or "",
			existing_customer and existing_customer.leave_type or "", customer.customer_name,
			existing_customer and existing_customer.naming_series or get_naming_series(),
		]
		w.writerow(row)
	return w

def get_active_customers():
	customers = frappe.db.sql("""select name, customer_name, customer_group, customer_type, territory
		from `tabCustomer` where docstatus < 2 and status = 'Enabled' """, as_dict=1)
	return customers

def get_existing_customer_records(args):
	customer = frappe.db.sql("""select name, customer_name, customer_group, customer_type, territory
		from `tabCustomer` where docstatus < 2""", as_dict=1)

	existing_customer = {}
	for att in customer:
		existing_customer[tuple([att.name, att.customer_name])] = att

	return existing_customer

def get_naming_series():
	series = frappe.get_meta("Customer").get_field("naming_series").options.strip().split("\n")
	if not series:
		frappe.throw(_("Please setup numbering series for Customer via Setup > Numbering Series"))
	return series[0]


@frappe.whitelist()
def upload():
	if not frappe.has_permission("Customer", "create"):
		raise frappe.PermissionError

	from frappe.utils.csvutils import read_csv_content_from_uploaded_file
	from frappe.modules import scrub

	rows = read_csv_content_from_uploaded_file()
	rows = filter(lambda x: x and any(x), rows)
	if not rows:
		msg = [_("Please select a csv file")]
		return {"messages": msg, "error": msg}
	columns = [scrub(f) for f in rows[4]]
	columns[0] = "name"
	columns[1] = "customer_name"
	ret = []
	error = False

	from frappe.utils.csvutils import check_record, import_doc

	for i, row in enumerate(rows[5:]):
		if not row: continue
		row_idx = i + 5
		d = frappe._dict(zip(columns, row))
		d["doctype"] = "Customer"
		if d.name:
			d["docstatus"] = frappe.db.get_value("Customer", d.name, "docstatus")

		try:
			check_record(d)
			ret.append(import_doc(d, "Customer", 1, row_idx, submit=False))
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