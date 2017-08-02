// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt

cur_frm.add_fetch('driver', 'user_id', 'user_id');

frappe.ui.form.on('Carrier', {
	refresh: function(frm) {

	},
	after_save: function(frm) {
		console.log("after_save")
		frappe.set_route("List", "Carrier");
	},
	driver_location: function(frm) {
	frappe.set_route("driverdashboard","Driver",frm.doc.driver);
	},
});
