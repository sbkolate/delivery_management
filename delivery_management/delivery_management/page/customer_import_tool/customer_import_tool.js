// frappe.pages['customer-import-tool'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Customer Import Tool',
// 		single_column: true
// 	});
// }


// frappe.CustomDataImportTool = frappe.DataImportTool.extend({
// 	init: function(parent) {
// 		console.log("custom init")
// 		this._super(parent)
// 		this.onload()
// 	},
// 	onload: function(parent) {
// 		console.log(" custom onload")
// 	}
// })


frappe.DataImportTool = frappe.DataImportTool.extend({
	init: function(parent) {
		console.log("Hello this file is called.")
	},
})

frappe.pages['data-import-tool'].on_page_load = function(wrapper) {
	frappe.data_import_tool = new frappe.DataImportTool(wrapper);
}
 