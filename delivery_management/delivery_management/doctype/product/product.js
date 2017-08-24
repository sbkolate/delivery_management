// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product', {
	refresh: function(frm) {
		if(frm.doc.__islocal == 1) {
			$(".ellipsis.title-text").hide()
		}
		else{
			$(".ellipsis.title-text").show()

		}

	}
});
