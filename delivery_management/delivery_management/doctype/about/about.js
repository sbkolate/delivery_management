// Copyright (c) 2017, DPI and contributors
// For license information, please see license.txt

frappe.ui.form.on('About', {
	refresh: function(frm) {
		cur_frm.add_custom_button(__('<i class="fa fa-home" title="Back" style="margin-left: 10px;background-color: red;padding: 6px;margin: -10px;border-radius: 5px;color: white;"> Cancel</i>'),
			function () { frappe.set_route("/"); }, 'fa fa-home btn-default', 'btn-danger')
	}
});
