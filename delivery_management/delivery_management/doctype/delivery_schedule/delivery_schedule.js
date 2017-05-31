// Copyright (c) 2017, DPI-Sagar and contributors
// For license information, please see license.txt

// cur_frm.add_fetch('address', 'address_line1', 'address_line_1');
// cur_frm.add_fetch('address', 'address_line2', 'address_line_2');
// cur_frm.add_fetch('contact_person_name', 'mobile_no', 'mobile_no');
// cur_frm.add_fetch('address', 'email_id', 'email');
// cur_frm.add_fetch('address', 'pincode', 'pin_code');
// cur_frm.add_fetch('address', 'phone', 'contact_no');

frappe.ui.form.on('Delivery Schedule', {
	refresh: function(frm) {

	},
	address: function(frm, cdt, cdn) {
		erpnext.utils.get_address_display(frm, 'address', 'address_display', false);
	},
});


// cur_frm.set_query('distributor', function () {
//     return {
//         filters: {
//             'party_type': 'Distributor'
//         }
//     }
// });

cur_frm.fields_dict.address.get_query = function(doc) {
 	return {
 		filters: {"customer": doc.customer_ref}
 	}
}