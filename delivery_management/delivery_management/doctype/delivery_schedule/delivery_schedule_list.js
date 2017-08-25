frappe.listview_settings['Delivery Schedule'] = {
	add_fields: ["customer_ref", "delivery_note_no", "status"],
	filters:[["status","=", "Open"]],
	get_indicator: function(doc) {
		if(doc.status=="Delivered"){
			return [__("Delivered"), "green", "status,=,Delivered"];

		} else if (doc.status=="In Transit"){
			return [__("In Transit"), "yellow", "status,=,In Transit"];

		} else if (doc.status=="Open"){
			return [__("Open"), "red", "status,=,Open"];

		} 
	}
};
