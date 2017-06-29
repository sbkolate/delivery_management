// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt


frappe.query_reports["Accounts Receivable"] = {
    "filters": [
        {
            "fieldname":"company",
            "label": __("Company"),
            "fieldtype": "Link",
            "options": "Company",
            "default": frappe.defaults.get_user_default("company")
        },
    ]
}
frappe.query_reports["Invoice Details"] = {
	"filters": [
		{
			"fieldname":"doctor",
			"label": __("Doctor"),
			"fieldtype": "Link",
			"options": "Doctor",
		},
	]
}
