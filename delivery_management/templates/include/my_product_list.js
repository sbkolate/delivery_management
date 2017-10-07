// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

window.get_product_list = function() {
	// $(".more-btn .btn").click(function() {
	// 	window.get_product_list()
	// });

	if(window.start==undefined) {
		throw "product list not initialized (no start)"
	}
	var ds_name = window.location.href.split("?")[1]
	url = "/api/method/delivery_management.api.utility.get_single_delivery_myorderpage?" + ds_name
	$.ajax({
		url: url,
		// url: "/api/method/delivery_management.api.api.get_single_delivery?name=DSCH00078",
		type: 'GET',
		dataType: 'json',
		success: function (data, textStatus, xhr) {
			console.log(data)
			window.render_product_list(data.message || []);
			console.log("successw3!!");
		},
		error: function (data, textStatus, xhr) {
			console.log("Failure!!");
		}
	});

	// $.ajax({
	// 	method: "GET",
	// 	url: "/",
	// 	dataType: "json",
	// 	data: {
	// 		cmd: "delivery_management.www.sc_product_search.get_product_list",
	// 		start: window.start,
	// 		search: window.search,
	// 		product_group: window.product_group
	// 	},
	// 	dataType: "json",
	// 	success: function(data) {
	// 		window.render_product_list(data.message || []);
	// 	}
	// })
}

window.render_product_list = function(data) {
	console.log(data)
	var table = $("#search-list .table");
	html = "</br>"
	html = "</br><table class='table table-bordered'>"
	html +="<tr>\
    			<td>Delivery Schedule</td><td>"
    html += data["ID"]
    html +=  "</td></tr>"

	html +="<tr>\
    			<td>Address</td><td>"
    html += data["Address Line1"]+","
    html += data["Address Line2"]+","
    html += data["Address Line3"]
    html +=  "</td></tr>"

   	html +="<tr>\
    			<td>Driver Name</td><td>"
    html += data["Driver Name"]
    html +=  "</td></tr>"

    html +="<tr>\
    			<td>Delivery Note</td><td>"
    html += data["Delivery Note"]
    html +=  "</td></tr>"

    html +="<tr>\
    			<td>Contact No</td><td>"
    html += data["Contact No"]
    html +=  "</td></tr>"

    html +="<tr>\
    			<td>Mobile No</td><td>"
    html += data["Mobile No"]
    html +=  "</td></tr>"
    html +=  "</table>"
    html +=  data["attachments"]

	// html += "</br></br>Product Images: <br>"

	// html +=  "<div style='width:830; background-color:white; height:120px; overflow:scroll; overflow-x: scroll;overflow-y: hidden;'>"
	// for (i = 0; i < Object.keys(data["attachments"]).length; i++) {
	// 	     html += "<img style=' float:left; display:inline; margin-right: 25px; padding:10px;border: 1px solid gray' src='"
	// 	    html += data["attachments"][i]["file_url"]

	// 	     //html += "http://qa.shopchemical.com/files/imgpsh_fullsize.png"
	// 	     html += "' width='160' height='90' alt='Product Image' />"
	// }
	// html += "</div>"


	// $("#delivery_details").append(JSON.stringify(data));
	$("#delivery_details").append(html);

	// if(data.length) {
	// 	if(!table.length)
	// 		var table = $("<table class='table'>").appendTo("#search-list");

	// 	$.each(data, function(i, d) {
	// 		$(d).appendTo(table);
	// 	});
	// }
	// if(data.length < 10) {
	// 	if(!table) {
	// 		$(".more-btn")
	// 			.replaceWith("<div class='alert alert-warning'>No products found.</div>");
	// 	} else {
	// 		$(".more-btn")
	// 			.replaceWith("<div class='text-muted'>1sssNothing more to show.</div>");
	// 	}
	// } else {
	// 	$(".more-btn").toggle(true)
	// }
	window.start += (data.length || 0);
}
