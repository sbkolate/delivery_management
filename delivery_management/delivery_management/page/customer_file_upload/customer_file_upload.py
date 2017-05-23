import frappe
from frappe.utils.csvutils import read_csv_content_from_uploaded_file
import json
from __future__ import unicode_literals
from frappe.utils import cstr, add_days, date_diff, getdate
from frappe import _
from frappe.utils.csvutils import UnicodeWriter
from frappe.model.document import Document


# @frappe.whitelist()
# def upload(update_due_date = None):
# 	params = json.loads(frappe.form_dict.get("params") or '{}')
# 	csv_rows = read_csv_content_from_uploaded_file()
# 	ret = []
# 	error = False
# 	for index,line in enumerate(csv_rows):
# 		d = {key:'' for key in csv_rows[0]}
# 		if index > 0:
# 			print ("hiiii")
			# d['Migrated agreement ID'] = line[0]
			# d['Agreement No'] = line[8]
			# d["Payoff"] = line[9]	
			# d['Payment ID'] = d['Agreement No']+"-"+line[1] if not d["Payoff"] else ""
			# d['Payment date'] = line[2]
			# d['Payment due date'] = line[3]
			# d['Cash'] = line[4]
			# #d['Credit card'] = line[5]
			# d['Bank Transfer'] = line[5]
			# d['Discount'] = line[6]
			# d['Late Fees'] = line[7]
			# ret.append(made_payments(d,params))

	# return {"messages": ret,"error":False}		
						


@frappe.whitelist()
def get_template():
	if not frappe.has_permission("Customer File Upload", "create"):
		raise frappe.PermissionError

	args = frappe.local.form_dict

	w = UnicodeWriter()
	w = add_header(w)

	w = add_data(w, args)

	# write out response as a type csv
	frappe.response['result'] = cstr(w.getvalue())
	frappe.response['type'] = 'csv'
	# frappe.response['doctype'] = "Upload Delivery Schedule"
	frappe.response['page'] = 'Customer File Upload'


def add_header(w):
	status = ", ".join((frappe.get_meta('Customer File Upload').get_field("status").options or "").strip().split("\n"))
	w.writerow(["Notes:"])
	w.writerow(["Please do not change the template headings"])
	w.writerow(["Status should be one of these values: " + status])
	w.writerow(["If you are overwriting existing attendance records, 'ID' column mandatory"])
	w.writerow(["ID", "Employee", "Employee Name", "Date", "Status", "Leave Type",
		 "Company", "Naming Series"])
	return w

def add_data(w, args):
	dates = get_dates(args)
	users = get_active_users()
	# existing_attendance_records = get_existing_attendance_records(args)
	for date in dates:
		for user in users:
			existing_attendance = {}
			if existing_attendance_records \
				and tuple([date, user.name]) in existing_attendance_records:
					existing_attendance = existing_attendance_records[tuple([date, user.name])]
			row = [
				existing_attendance and existing_attendance.name or "",
				user.name, user.user_name, date,
				existing_attendance and existing_attendance.status or "",
				existing_attendance and existing_attendance.leave_type or "", user.company,
				existing_attendance and existing_attendance.naming_series or get_naming_series(),
			]
			w.writerow(row)
	return w

def get_dates(args):
	"""get list of dates in between from date and to date"""
	no_of_days = date_diff(add_days(args["to_date"], 1), args["from_date"])
	dates = [add_days(args["from_date"], i) for i in range(0, no_of_days)]
	return dates

def get_active_users():
	users = frappe.db.sql("""select name, first_name, company
		from tabUser where docstatus < 2 and status = 'Active'""", as_dict=1)
	return users

def get_existing_attendance_records(args):
	attendance = frappe.db.sql("""select name, attendance_date, employee, status, leave_type, naming_series
		from `tabAttendance` where attendance_date between %s and %s and docstatus < 2""",
		(args["from_date"], args["to_date"]), as_dict=1)

	existing_attendance = {}
	for att in attendance:
		existing_attendance[tuple([att.attendance_date, att.employee])] = att

	return existing_attendance

def get_naming_series():
	series = frappe.get_meta("Attendance").get_field("naming_series").options.strip().split("\n")
	if not series:
		frappe.throw(_("Please setup numbering series for Attendance via Setup > Numbering Series"))
	return series[0]


@frappe.whitelist()
def upload():
	print "hiiiiiii"
	# if not frappe.has_permission("Upload Delivery Schedule", "create"):
	# 	raise frappe.PermissionError

	# from frappe.utils.csvutils import read_csv_content_from_uploaded_file
	# from frappe.modules import scrub

	# rows = read_csv_content_from_uploaded_file()
	# rows = filter(lambda x: x and any(x), rows)
	# if not rows:
	# 	msg = [_("Please select a csv file")]
	# 	return {"messages": msg, "error": msg}
	# columns = [scrub(f) for f in rows[4]]
	# columns[0] = "name"
	# columns[3] = "attendance_date"
	# ret = []
	# error = False

	# from frappe.utils.csvutils import check_record, import_doc

	# for i, row in enumerate(rows[5:]):
	# 	if not row: continue
	# 	row_idx = i + 5
	# 	d = frappe._dict(zip(columns, row))
	# 	d["doctype"] = "Upload Delivery Schedule"
	# 	if d.name:
	# 		d["docstatus"] = frappe.db.get_value("Upload Delivery Schedule", d.name, "docstatus")

	# 	try:
	# 		check_record(d)
	# 		ret.append(import_doc(d, "Upload Delivery Schedule", 1, row_idx, submit=True))
	# 	except Exception, e:
	# 		error = True
	# 		ret.append('Error for row (#%d) %s : %s' % (row_idx,
	# 			len(row)>1 and row[1] or "", cstr(e)))
	# 		frappe.errprint(frappe.get_traceback())

	# if error:
	# 	frappe.db.rollback()
	# else:
	# 	frappe.db.commit()
	# return {"messages": ret, "error": error}