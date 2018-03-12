// Copyright (c) 2016, DPI and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Delivery Schedule Tracking"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd":1
		},
		{
			"fieldname":"carrier",
			"label": __("Carrier"),
			"fieldtype": "Link",
			"options": "Carrier",
			"get_query": function() {
				return {
					"query": "delivery_management.delivery_management.doctype.carrier.carrier.get_carrier",
				}
			}
			// "default": frappe.datetime.get_today(),
		},
		{
			"fieldname":"delivery_note_no",
			"label": __("Delivery Note No"),
			"fieldtype": "Data",
			"get_query": function() {
				return {
					"query": "delivery_management.delivery_management.doctype.carrier.carrier.get_carrier",
				}
			}
			
			// "default": frappe.datetime.get_today(),
		},

	]
}
