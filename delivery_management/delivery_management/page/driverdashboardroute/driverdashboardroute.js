frappe.provide('delivery_management');
frappe.require("/assets/delivery_management/js/googlemap.js");

frappe.pages['driverdashboardroute'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'DriverDashboardRoute',
		single_column: true
	});
wrapper.DriverDashboardroute = new delivery_management.Dashboard(wrapper);

	// var html = frappe.render_template("maptemplate", {"data":"this is encripted data"})
	var html = "hello"
	$(html).appendTo($(wrapper).find('.layout-main'));
	// frappe.breadcrumbs.add("Clinic Dashboard");

	$("<br><div class='row'><div class='party-area col-xs-4' style='margin-left:10px;'> </div> <div class='party-area col-xs-8'> </div><br><br></div>\
  <div class='row'>\
	  	<div class='party-area col-xs-12'>\
			<div id='myGrid1' style='width:100%;height:500px;''></div>\
		</div>\
	</div>").appendTo($(wrapper).find('.layout-main-section'));


}

delivery_management.Dashboard = Class.extend({
	init: function(opts, wrapper,page) {
		$.extend(this, opts);

		this.make_fun();
		this.page.main.find(".page").css({"padding-top": "0px"});
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
		// var locations =[];
		for(i=0;i<b.message.length;i++)
		{
			console.log(b.message[i].start_lat);
			console.log(b.message[i].start_long)
			
		}
		

	var directionsService = new google.maps.DirectionsService();
	var request = {
	    origin: 'kotarud',
	    destination: 'Hinjewadi',
	    travelMode: 'DRIVING'
  	};
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
// var image = 'img/truck.png';
        
    var marker, i;

    for (i = 0; i < locations.length; i++) { 
    	// console.log("############");
    	// console.log(locations[i][2]);
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        map: map,
        // icon: image
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
	}, 100)


     },
     get_all_location: function(){
     	var me = this;
		
		return frappe.call({
			method: "delivery_management.delivery_management.page.driverdashboardroute.driverdashboardroute.get_driver_route",
			async:false,
			callback: function(r) {
				return  r.message
			}
		});

     },

})

