// Copyright (c) 2016, DPI-Sagar and contributors
// For license information, please see license.txt


frappe.ui.form.on('Delivery Order', {
    refresh: function(frm) {
		function(){
				frappe.model.open_mapped_doc({
					method: "delivery_management.delivery_management.doctype.delivery_order.delivery_order.make_delivery_note",
					frm: cur_frm
				});
		},
  	},
});


frappe.provide("erpnext.hr");

// erpnext.hr.AttendanceControlPanel = frappe.ui.form.Controller.extend({
frappe.ui.form.on('Upload Delivery Schedule', {
	onload: function() {
		this.frm.set_value("delivery_from_date", get_today());
		this.frm.set_value("delivery_to_date", get_today());
	},

	refresh: function() {
		this.frm.disable_save();
		this.show_upload();
	},

	get_template:function() {
		if(!this.frm.doc.delivery_from_date || !this.frm.doc.delivery_to_date) {
			msgprint(__("Delivery From Date and Delivery To Date is mandatory"));
			return;
		}
		window.location.href = repl(frappe.request.url +
			'?cmd=%(cmd)s&from_date=%(from_date)s&to_date=%(to_date)s', {
				cmd: "erpnext.hr.doctype.upload_attendance.upload_attendance.get_template",
				from_date: this.frm.doc.att_fr_date,
				to_date: this.frm.doc.att_to_date,
			});
	},

	show_upload: function() {
		var me = this;
		var $wrapper = $(cur_frm.fields_dict.upload_html.wrapper).empty();

		// upload
		frappe.upload.make({
			parent: $wrapper,
			args: {
				method: 'erpnext.hr.doctype.upload_attendance.upload_attendance.upload'
			},
			sample_url: "e.g. http://example.com/somefile.csv",
			callback: function(attachment, r) {
				var $log_wrapper = $(cur_frm.fields_dict.import_log.wrapper).empty();

				if(!r.messages) r.messages = [];
				// replace links if error has occured
				if(r.exc || r.error) {
					r.messages = $.map(r.message.messages, function(v) {
						var msg = v.replace("Inserted", "Valid")
							.replace("Updated", "Valid").split("<");
						if (msg.length > 1) {
							v = msg[0] + (msg[1].split(">").slice(-1)[0]);
						} else {
							v = msg[0];
						}
						return v;
					});

					r.messages = ["<h4 style='color:red'>"+__("Import Failed!")+"</h4>"]
						.concat(r.messages)
				} else {
					r.messages = ["<h4 style='color:green'>"+__("Import Successful!")+"</h4>"].
						concat(r.message.messages)
				}

				$.each(r.messages, function(i, v) {
					var $p = $('<p>').html(v).appendTo($log_wrapper);
					if(v.substr(0,5)=='Error') {
						$p.css('color', 'red');
					} else if(v.substr(0,8)=='Inserted') {
						$p.css('color', 'green');
					} else if(v.substr(0,7)=='Updated') {
						$p.css('color', 'green');
					} else if(v.substr(0,5)=='Valid') {
						$p.css('color', '#777');
					}
				});
			}
		});

		// rename button
		$wrapper.find('form input[type="submit"]')
			.attr('value', 'Upload and Import')
	}
})

cur_frm.cscript = new erpnext.hr.AttendanceControlPanel({frm: cur_frm});
