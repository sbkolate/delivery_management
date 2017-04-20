// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt


cur_frm.add_fetch('driver', 'first_name', 'first_name');
cur_frm.add_fetch('Driver', 'last_name', 'last_name');
cur_frm.add_fetch('Driver', 'birth_date', 'date_of_birth');
cur_frm.add_fetch('Driver', 'phone', 'contact_number');
cur_frm.add_fetch('Driver', 'email', 'email_address');
cur_frm.add_fetch('Driver', 'gender', 'gender');



frappe.ui.form.on('Driver', {
	refresh: function(frm) {

	}
});
