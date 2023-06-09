frappe.provide('delivery_management');
// frappe.require("/assets/delivery_management/js/googlemap.js");


frappe.pages['driverdashboard'].on_page_lo
ad = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Driver Dashboard',
		single_column: true
	});

	wrapper.driverdashboard = new delivery_management.Dashboard(wrapper);

	// var html = frappe.render_template("maptemplate", {"data":"this is encripted data"})
	var html = "hello"
	$(html).appendTo($(wrapper).find('.layout-main'));
	// frappe.breadcrumbs.add("Clinic Dashboard");

	$("<br><div class='row'><div class='party-area col-xs-4' style='margin-left:10px;z-index: 12;'> </div> <div class='party-area col-xs-8'> </div><br><br></div>\
  <div class='row'>\
	  	<div class='party-area col-xs-12'>\
			<div id='myGrid1' style='width:100%;height:500px;''></div>\
		</div>\
	</div>").appendTo($(wrapper).find('.layout-main-section'));


}

delivery_management.Dashboard = Class.extend
	({
		init: function(opts, wrapper,page)
		{
			$.extend(this, opts);
			this.add_filter()
			this.make_fun();
			this.page.main.find(".page").css({"padding-top": "0px"});
		},
		add_filter: function(opts, wrapper,page){
			console.log("in make party");
    		var me = this;
			console.log(me.page.wrapper.find("#party-area"));
	
			setTimeout(function(){
					this.party_field = frappe.ui.form.make_control({
						df: {
							"fieldtype": "Link",
							"options": "Driver",
							"label": "Driver",
							"fieldname": "pos_party",
							"Link": "Driver",
							"placeholder": "Driver",
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
					console.log("#############")
					console.log(window.location.href)
					driver= window.location.href.split("/")[5]
					console.log(driver)
					$('input[data-fieldname="pos_party"]').val(driver).change();

			}, 300)


		},
		make_fun: function(){
		this.page.set_title(__("Dashboard") + " - " + __("Driver Location"));
		var me = this;
		setTimeout(function(){
			$.getScript( "http://maps.google.com/maps/api/js?key=AIzaSyCGWFz53x4ukwNmX8B0U51qa9W0t5_df3Y&&sensor=false", function( data, textStatus, jqxhr ) {
  			console.log( "Load was performed." );

			locations = me.get_all_location();
			b = JSON.parse(locations["responseText"])
			console.log("@@@@@@@@@@@@@@")
			console.log(b.message)

			var html = frappe.render_template("maptemplate", {"data":"this is encripted data"})
			$("#myGrid1").html(html)

			
			console.log(b.message);
			var locations =[];
			// for(i=0;i<b.message.length;i++)
			// 	{
			// 		console.log(b.message[i].latitude);
			// 		console.log(b.message[i].longitude)
			// 		locations.push([b.message[i].carrier_number, parseFloat(b.message[i].latitude), parseFloat(b.message[i].longitude), i]);
			// 	}
			console.log(b.message[0].carrier_number)
			console.log(b.message[0].latitude)
			console.log(b.message[0].longitude)
			locations.push([b.message[0].carrier_number, parseFloat(b.message[0].latitude), parseFloat(b.message[0].longitude)]);
			  



			
				var map = new google.maps.Map(document.getElementById('map'),
				{
      				zoom: 8,
      				center: new google.maps.LatLng(18.89, 73.97),
     				mapTypeId: google.maps.MapTypeId.ROADMAP
    			});

    				var infowindow = new google.maps.InfoWindow();
    				var marker, i;

    			for (i = 0; i < locations.length; i++)
    			{ 
    				
    				// console.log(locations[i][2]);
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
	}, 100)


     },
     get_all_location: function(){
     	var me = this;
     	console.log("###")
     	console.log(me.so_number)
		
		return frappe.call({
			method: "delivery_management.delivery_management.page.driverdashboard.driverdashboard.get_driver_locations",
			async:false,
		args: {
				"driver": me.so_number

			  },
		callback: function(r)
			{
				return  r.message
			}
		});

     },

})
