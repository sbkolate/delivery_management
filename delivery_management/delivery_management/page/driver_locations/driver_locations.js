frappe.provide('delivery_management');

frappe.pages['driver-locations'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Driver Locations',
		single_column: true
	});

	wrapper.dashboard = new delivery_management.DriverLocations(wrapper);


	frappe.breadcrumbs.add("Clinic Dashboard");

}

