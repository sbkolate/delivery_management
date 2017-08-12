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
		
	},
	onload: function(frm, cdt, cdn) {
		if(frm.doc.__islocal == 1) {
			if($('#cancelredirect').length == 0) {
				$(".page-actions").append("<button type='button' id='cancelredirect' class='btn btn-default'>Cancel</button>")
			}
		}
	},
	after_save: function(frm) {
		console.log("after_save")
		frappe.set_route("List", "Driver");
	},

});
