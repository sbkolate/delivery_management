// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt

cur_frm.add_fetch('product_code', 'product_name', 'product_name');
cur_frm.add_fetch('product_code', 'description', 'description');

frappe.ui.form.on('Delivery Order', {
	refresh: function(frm) {
		
	}
});


frappe.ui.form.on('Delivery Order', {
	refresh: function(frm) {
		if(frm.doc.docstatus == 1) {
			cur_frm.add_custom_button(__("Make Delivery Note"),
				function() {
					frappe.model.open_mapped_doc({
							method: "delivery_management.delivery_management.doctype.delivery_order.delivery_order.make_delivery_note",
							frm: cur_frm
					})
				})
			}
		},
});

