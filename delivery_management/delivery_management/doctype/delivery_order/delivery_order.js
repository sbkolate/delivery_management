// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt

cur_frm.add_fetch('product_code', 'product_name', 'product_name');
cur_frm.add_fetch('product_code', 'description', 'description');
cur_frm.add_fetch('contact_person', 'mobile_no', 'mobile_no');


frappe.ui.form.on('Delivery Order', {
    refresh: function(frm) {
		cur_frm.add_custom_button(__('Make Delivery Note'), 
			function(){
				frappe.model.open_mapped_doc({
					method: "delivery_management.delivery_management.doctype.delivery_order.delivery_order.make_delivery_note",
					frm: cur_frm
				})
		}, __("Make"));
  	},
	customer_address: function(frm, cdt, cdn) {
		erpnext.utils.get_address_display(frm, 'customer_address', 'address_display', false);
	},
	shipping_address_name: function(frm, cdt, cdn) {
		erpnext.utils.get_address_display(frm, "shipping_address_name", "shipping_address_display", false);
	},
});