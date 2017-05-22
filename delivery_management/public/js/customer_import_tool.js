frappe.pages['customer-import-tool'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Customer Import Tool',
		single_column: true
	});
}


frappe.CustomDataImportTool = frappe.DataImportTool.extend({
	init: function(parent) {
		console.log("custom init")
		this._super(parent)
		this.onload()
	},
	onload: function(parent) {
		console.log(" custom onload")
	}
})