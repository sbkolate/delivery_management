

// frappe.listview_settings['Delivery Management'] = {
// 	add_fields: ["customer_ref", "delivery_note_no", "status"],
// 	get_indicator: function(doc) {
// 		if(doc.status==="Delivered"){
// 			return [__("Delivered"), "red", "status,=,Delivered"];

// 		// } else if (doc.status==="In Transit"){
// 		// 	return [__("In Transit"), "yellow", "status,=,In Transit"];

// 		// } else if (doc.status==="Delivered"){
// 		// 	return [__("Delivered"), "green", "status,=,Delivered"];

// 		// } 
// 	},
// 	onload: function(listview) {
// 		var method = "erpnext.selling.doctype.sales_order.sales_order.close_or_unclose_sales_orders";

// 		listview.page.add_menu_item(__("Close"), function() {
// 			listview.call_for_selected_items(method, {"status": "Closed"});
// 		});

// 		listview.page.add_menu_item(__("Re-open"), function() {
// 			listview.call_for_selected_items(method, {"status": "Submitted"});
// 		});

// 	}
// };
