// Copyright (c) 2017, DPI-Sagar and contributors
// For license information, please see license.txt

cur_frm.add_fetch('address', 'address_line1', 'address_line_1');
cur_frm.add_fetch('address', 'address_line2', 'address_line_2');
cur_frm.add_fetch('contact_person_name', 'mobile_no', 'mobile_no');
cur_frm.add_fetch('address', 'email_id', 'email');
cur_frm.add_fetch('address', 'pincode', 'pin_code');
cur_frm.add_fetch('address', 'phone', 'contact_no');

frappe.ui.form.on('Delivery Schedule', {
	refresh: function(frm) {

	}
});
