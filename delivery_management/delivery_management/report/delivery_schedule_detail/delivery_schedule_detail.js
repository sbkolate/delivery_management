// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt

frappe.query_reports["Delivery Schedule Detail"] = {
	"filters": [
		{
			"fieldname":"date",
			"label": __("Date"),
			"fieldtype": "Date",
			// "default": frappe.datetime.get_today(),
		},

		{
			"fieldname":"driver",
			"label": __("Driver"),
			"fieldtype": "Link",
			"options": "Driver",
			// "default": frappe.datetime.get_today(),
		},
	]


}


