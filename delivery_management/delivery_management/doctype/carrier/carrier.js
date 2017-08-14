// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt

cur_frm.add_fetch('driver', 'user_id', 'user_id');

frappe.ui.form.on('Carrier', {
	refresh: function(frm) {

		if(frm.doc.__islocal == 1) {
			cur_frm.add_custom_button(__('<i class="fa fa-home" title="Back" style="margin-left: 10px;color: red;"> Cancel</i>'),
			function () { frappe.set_route("/"); }, 'fa fa-home btn-default', 'btn-danger')

		}
		else{

			cur_frm.add_custom_button(__('<i class="fa fa-street-view" title="Show Route" style=""> Driver Location</i>'),
			function () { cur_frm.cscript.show_route(frm); }, 'fa fa-retweet', 'btn-default')
			cur_frm.add_custom_button(__('<i class="fa fa-home" title="Back" style="margin-left: 10px;color: red;"> Cancel</i>'),
			function () { frappe.set_route("/"); }, 'fa fa-home btn-default', 'btn-danger')

		}
	},
	onload: function(frm, cdt, cdn) {
		// if(frm.doc.__islocal == 1) {
		// 	if($('#cancelredirect').length == 0) {
		// 		$(".page-actions").append("<button type='button' id='cancelredirect' class='btn btn-default'>Cancel</button>")
		// 	}
		// }
	},
	after_save: function(frm) {
		console.log("after_save")
		frappe.set_route("List", "Carrier");
	},
	driver_location: function(frm) {
	frappe.set_route("driverdashboard","Driver",frm.doc.driver);
	},
});


cur_frm.cscript.show_route = function (frm) {

	window.location.hash =  'driverdashboard/Driver/' + frm.doc.driver;
	window.location.reload()
		// frappe.set_route("driverdashboardroute","delivery_schedule",frm.doc.name);

}