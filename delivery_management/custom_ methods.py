import frappe
from frappe.utils import flt, rounded,money_in_words
from frappe.model.mapper import get_mapped_doc
from frappe import throw, _


@frappe.whitelist()
def set_customer_full_name(doc, method):
	frappe.msgprint("hiiiiii")
	# customer_doc = frappe.get_doc("Account",account)
	# customer = frappe.db.get_value("Customer", doc.name,"name")


	# if not account:
	# 	if company:
	# 		gst_account = frappe.new_doc("Account")
	# 		gst_account.account_name = "GST"
	# 		gst_account.account_type = "Tax"
	# 		gst_account.tax_rate = doc.gst_tax_rate
	# 		gst_account.currency = doc.default_currency
	# 		gst_account.parent_account = "Duties and Taxes - " + doc.abbr
	# 		gst_account.company = doc.name
	# 		gst_account.save()
	# else:
	# 	gst_account = frappe.get_doc("Account",account)
	# 	if gst_account:
	# 		gst_account.tax_rate = doc.gst_tax_rate
	# 		gst_account.save()













@frappe.whitelist()
def create_gst_account_after_company(doc, method):
	if doc.gst == "Yes":
		account = frappe.db.get_value("Account", "GST - "+ doc.abbr,"name")
		if not account:
			gst_account = frappe.new_doc("Account")
			gst_account.account_name = "GST"
			gst_account.account_type = "Tax"
			gst_account.tax_rate = doc.gst_tax_rate
			gst_account.currency = doc.default_currency
			gst_account.parent_account = "Duties and Taxes - " + doc.abbr
			gst_account.company = doc.name
			# gst_account.save()

@frappe.whitelist()
def create_gst_account(doc, method):
	if doc.gst == "Yes":
		account = frappe.db.get_value("Account", "GST - "+ doc.abbr,"name")
		company = frappe.db.get_value("Company", doc.name ,"name")
		if not account:
			if company:
				gst_account = frappe.new_doc("Account")
				gst_account.account_name = "GST"
				gst_account.account_type = "Tax"
				gst_account.tax_rate = doc.gst_tax_rate
				gst_account.currency = doc.default_currency
				gst_account.parent_account = "Duties and Taxes - " + doc.abbr
				gst_account.company = doc.name
				gst_account.save()
		else:
			gst_account = frappe.get_doc("Account",account)
			if gst_account:
				gst_account.tax_rate = doc.gst_tax_rate
				gst_account.save()
