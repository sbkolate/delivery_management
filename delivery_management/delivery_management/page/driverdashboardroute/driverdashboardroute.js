frappe.provide('delivery_management');
frappe.provide('frappe.pages');
frappe.provide('frappe.views');

frappe.pages['driverdashboardroute'].on_page_load = function(wrapper)
{
		var page = frappe.ui.make_app_page
			({
			parent: wrapper,
			title: 'DriverDashboardRoute',
			single_column: true
			});
		
		wrapper.DriverDashboardroute = new delivery_management.Dashboard(wrapper);
		
		var html = "hello"
		$(html).appendTo($(wrapper).find('.layout-main'));
		$("<br><div class='row'><div class='party-area col-xs-4' style='margin-left:10px;z-index: 12;'> </div> <div class='party-area col-xs-8' id='party-area'> </div><br><br></div>\
  			<div class='row'>\
	  				<div class='party-area col-xs-12'>\
					<div id='myGrid1' style='width:100%;height:500px;''></div>\
				</div>\
			</div>").appendTo($(wrapper).find('.layout-main-section'));
}		

delivery_management.Dashboard = Class.extend
({
		init: function(opts, wrapper,page) {
			$.extend(this, opts);

		this.make_fun();
		this.add_filter();
		this.page.main.find(".page").css({"padding-top": "0px"});
	},
	add_filter: function(opts, wrapper,page)
		{
			console.log("in make party");
    		var me = this;
			console.log(me.page.wrapper.find("#party-area"));
	
	setTimeout(function(){
		this.party_field = frappe.ui.form.make_control({
			df: {
				"fieldtype": "Link",
				"options": "Delivery Schedule",
				"label": "Delivery Schedule",
				"fieldname": "pos_party",
				"Link": "Delivery Schedule",
				"placeholder": "Delivery Schedule",
			},
			parent: me.page.wrapper.find(".party-area"),
			only_input: true,
		});
		this.party_field.make_input();
		this.party_field.$input.on("change", function() {
					me.so_number = this.value;
					console.log(me.so_number);
					me.make_fun();
		});
	}, 300)


	},
	make_fun: function(){
            this.page.set_title(__("Dashboard") + " - " + __("Driver Route"));


    	var me = this;
	setTimeout(function(){
//set time out start
$.getScript( "http://maps.google.com/maps/api/js?key=AIzaSyCGWFz53x4ukwNmX8B0U51qa9W0t5_df3Y&&sensor=false", function( data, textStatus, jqxhr ) {
  console.log( "Load was performed." );

		
		locations = me.get_all_location();
		b = JSON.parse(locations["responseText"])
		console.log("##############")
		console.log(b.message)
		console.log("##############")

		var html = frappe.render_template("drivermaptemplate", {"data":"this is encripted data"})
		$("#myGrid1").html(html)
		var directionsService = new google.maps.DirectionsService();
		var source = new google.maps.LatLng(b.message[0].start_lat, b.message[0].start_long);
		var destination = new google.maps.LatLng(b.message[0].stop_lat, b.message[0].stop_long);

		var request = {
			origin: source,
    		destination: destination,
    		travelMode: 'DRIVING'
			};
			console.log("start locations")
		console.log(b.message);
		console.log("stop locations")
		var directionsDisplay = new google.maps.DirectionsRenderer();
	 	directionsService.route(request, function(result, status) {
    if (status == 'OK') {
      directionsDisplay.setDirections(result);
    }
  	});


    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 8,
      center: new google.maps.LatLng(18.89, 73.97),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    directionsDisplay.setMap(map);

    var infowindow = new google.maps.InfoWindow();

        
    var marker, i;

    for (i = 0; i < locations.length; i++) {
    	marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        map: map,
    });

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][0]);
          infowindow.open(map, marker);
        }
      })(marker, i));
    }

});
//end time out and get script
	}, 500)


     },
     get_all_location: function(){
     	var me = this;
     	return frappe.call({
		method: "delivery_management.delivery_management.page.driverdashboardroute.driverdashboardroute.get_driver_route",
		async:false,
		args: {
				"delivery_schedule": me.so_number
			  },
		callback: function(r)
			{
				return  r.message
			}
		});

     },

})


