cur_frm.add_fetch('lorry_no', 'driver', 'driver');
cur_frm.add_fetch('driver', 'user_id', 'driver_user_id');
cur_frm.add_fetch('driver', 'full_name', 'driver_full_name');


frappe.ui.form.on('Delivery Schedule', {
	refresh: function(frm) {

	},
	address: function(frm, cdt, cdn) {
		erpnext.utils.get_address_display(frm, 'address', 'address_display', false);
	},
		after_save: function(frm) {
		frappe.set_route("List", "Delivery Schedule");
	},
	show_route: function(frm) {
		frappe.set_route("driverdashboardroute","delivery_schedule",frm.doc.name);
	},
	send_email: function(frm) { 
		frappe.msgprint("send email is clicked");
		frappe.call({
			method: "delivery_management.custom_methods.send_email",
			args: {
				"name": frm.doc.name,
				"email": frm.doc.email,
				
			},

			callback: function(r) {
				if(r.message=="success"){
					// console.log(r.message);
					// frappe.msgprint("Item Price updated");
				}
			}
		})

	},
});


cur_frm.fields_dict.address.get_query = function(doc) {
 	return {
 		filters: {"customer": doc.customer_ref}
 	}
}



