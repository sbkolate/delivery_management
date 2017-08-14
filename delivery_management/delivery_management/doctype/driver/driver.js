// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt


cur_frm.add_fetch('user_id', 'first_name', 'first_name');
cur_frm.add_fetch('user_id', 'last_name', 'last_name');
cur_frm.add_fetch('user_id', 'birth_date', 'date_of_birth');
cur_frm.add_fetch('user_id', 'phone', 'contact_number');
cur_frm.add_fetch('user_id', 'email', 'email_address');
cur_frm.add_fetch('user_id', 'gender', 'gender');



frappe.ui.form.on('Driver', {
	refresh: function(frm) {
			cur_frm.add_custom_button(__('<i class="fa fa-home" title="Back" style="margin-left: 10px;background-color: red;padding: 6px;margin: -10px;border-radius: 5px;color: white;"> Cancel</i>'),
			function () { frappe.set_route("/"); }, 'fa fa-home btn-default', 'btn-danger');
		
	},
	onload: function(frm, cdt, cdn) {

	},
	after_save: function(frm) {
		console.log("after_save")
		frappe.set_route("List", "Driver");
	},

});
