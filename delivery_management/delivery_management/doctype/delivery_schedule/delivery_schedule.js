cur_frm.add_fetch('lorry_no', 'driver', 'driver');
cur_frm.add_fetch('driver', 'user_id', 'driver_user_id');
cur_frm.add_fetch('driver', 'full_name', 'driver_full_name');
cur_frm.add_fetch('driver', 'carrier', 'carrier');




frappe.ui.form.on('Delivery Schedule', {
	refresh: function(frm) {
		if(frm.doc.__islocal == 1) {
			cur_frm.add_custom_button(__('<i class="fa fa-home" title="Back" style="margin-left: 10px;background-color: red;padding: 6px;margin: -10px;border-radius: 5px;color: white;"> Cancel</i>'),
			function () { frappe.set_route("/"); }, 'fa fa-home btn-default', 'btn-danger')
		}
		else{

			cur_frm.add_custom_button(__('<i class="fa fa-map" title="Show Route" style=""> Show Route</i>'),
				function () { 
					cur_frm.cscript.show_route(frm); }, 'fa fa-retweet', 'btn-default')


			cur_frm.add_custom_button(__('<i class="fa fa-envelope" title="Show Route" style=""> Send Email</i>'),
				function () {
					cur_frm.cscript.send_email(frm); }, 'fa fa-retweet', 'btn-default')
			cur_frm.add_custom_button(__('<i class="fa fa-home" title="Back" style="margin-left: 10px;background-color: red;padding: 6px;margin: -10px;border-radius: 5px;color: white;"> Cancel</i>'),
			function () { frappe.set_route("/"); }, 'fa fa-home btn-default', 'btn-danger')
		}
		if(frm.doc.__islocal == 1) {
			$(".ellipsis.title-text").hide()
		}
		else{
			$(".ellipsis.title-text").show()

		}
	},
	onload: function(frm, cdt, cdn) {
		// if(frm.doc.__islocal == 1) {
		// 	if(0 == 0) {
		// 		$(".page-actions").append("<button type='button' id='cancelredirect' class='btn btn-default'>Cancel</button>")
		// 	}
		// }
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
		frappe.msgprint("email sent");
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

cur_frm.cscript.show_route = function (frm) {

	window.location.hash =  'driverdashboardroute/delivery_schedule/' + frm.doc.name;
	window.location.reload()
		// frappe.set_route("driverdashboardroute","delivery_schedule",frm.doc.name);

}
cur_frm.fields_dict.address.get_query = function(doc) {
 	return {
 		filters: {"customer": doc.customer_ref}
 	}
}

cur_frm.cscript.send_email=function(frm) { 
		
		frappe.call({
			method: "delivery_management.custom_methods.send_email",
			args: {
				"name": frm.doc.name,
				"email": frm.doc.email,
				
			},

			callback: function(r) {
				if(r.message=="success"){
					
				}
			}
		})

	}












