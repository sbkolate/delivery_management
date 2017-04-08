// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt

cur_frm.add_fetch('product_code', 'product_name', 'product_name');
cur_frm.add_fetch('product_code', 'description', 'description');


frappe.ui.form.on('Delivery Request', {
	refresh: function(frm) {

	}
});
