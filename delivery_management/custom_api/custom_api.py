from __future__ import unicode_literals
import frappe, os, json
from frappe.utils import cstr
from unidecode import unidecode

@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"