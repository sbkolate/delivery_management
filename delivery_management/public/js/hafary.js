$('#body_div').on('click', '#cancelredirect',function() {
	frappe.set_route("/");
	console.log("hi");
});

