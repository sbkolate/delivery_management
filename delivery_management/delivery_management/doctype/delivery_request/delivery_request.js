// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt

cur_frm.add_fetch('product_code', 'product_name', 'product_name');
cur_frm.add_fetch('product_code', 'description', 'description');


// frappe.ui.form.on('Delivery Request', {
// 	refresh: function(frm) {

// 	}
// });


frappe.ui.form.on('Delivery Request', {
    refresh: function(frm) {
    	var me = this;
		cur_frm.add_custom_button(__('Make Delivery Order'), 
			function(){
				frappe.model.open_mapped_doc({
					method: "delivery_management.delivery_management.doctype.delivery_request.delivery_request.make_delivery_order",
					frm: cur_frm
				})
		}, __("Make"));
  	}

 //  	make_delivery_order: function() {

	// },
});

// frappe.ui.form.on('Case', {
// 	refresh: function(frm) {
// 		if(frm.doc.docstatus == 1) {
// 			cur_frm.add_custom_button(__("Create Invoice"),
// 				function() {
// 					frappe.model.open_mapped_doc({
// 							method: "clinic_management.clinic_management.doctype.case.case.create_quote",
// 							frm: cur_frm
// 					})
// 				})
// 			}
// 	},
// 	onload: function(frm) {
// 		if(frm.doc.__islocal == 1) {
// 			frm.doc.company = "";
// 		}
// 	},
	// company: function(frm) {
	// 	if(!frm.doc.doctor) frappe.throw(__("Please select Doctor first"));
	// },
// });






















frappe.ui.form.on("Delivery Request", "on_update", function(frm) {
    frm.add_custom_button(__("Make Delivery Order"), function() {
        

        var subject = frm.doc.subject;
        var event_type = frm.doc.event_type;

        // do something with these values, like an ajax request 
        // or call a server side frappe function using frappe.call
        $.ajax({
            url: "http://example.com/just-do-it",
            data: {
                "subject": subject,
                "event_type": event_type
            }

            // read more about $.ajax syntax at http://api.jquery.com/jquery.ajax/

        });
    });
});