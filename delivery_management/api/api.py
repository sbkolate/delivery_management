from __future__ import unicode_literals
import frappe, os, json, json

import base64 
from frappe import _

from frappe.utils import strip, get_files_path
from frappe.desk.form.load import get_attachments

from frappe.utils import flt, time_diff_in_hours, get_datetime, getdate, today, cint, get_datetime_str
from erpnext.setup.doctype.sms_settings.sms_settings import send_sms
import ast
from bitly import ping

import json
import requests
from frappe.desk.form.load import get_attachments
from frappe.core.doctype.communication.email import make

STANDARD_USERS = ("Guest", "Administrator")


@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

@frappe.whitelist(allow_guest=True)
def update_img_in_delivery_schedule(name=None,img_1=None,img_2=None,img_3=None,img_4=None):
	ds_doc = frappe.get_doc("Delivery Schedule", name)
	
	if ds_doc.name:
		ds_doc.flags.ignore_permissions = True
		ds_doc.save(ignore_permissions=True)
		file_url = get_files_path ()
		file_url += "/"
		file_url += name
		img_count = int(ds_doc.img_count) + 1
		img_name = "_img"+ str(img_count) +".png"
		
		ds_doc.img_1 = img_1
		ds_doc.img_count = img_count

		file_url += img_name
		image_64_decode = base64.decodestring(img_1)
		image_result = open(file_url, 'wb')
		image_result.write(image_64_decode)

		file_doc = frappe.new_doc("File")
		file_doc.file_name = name + img_name
		file_doc.folder = "Home/Attachments"
		file_doc.attached_to_doctype = "Delivery Schedule"
		file_doc.attached_to_name = ds_doc.name
		file_url_attach = get_files_path ()

		file_doc.file_url = "files/" + name + img_name
		file_doc.validate()
		file_doc.insert(ignore_permissions=True)
		ds_doc.save(ignore_permissions=True)
		frappe.db.commit()
	
	if img_2:
		ds_doc.flags.ignore_permissions = True
		ds_doc.save(ignore_permissions=True)
		file_url = get_files_path ()
		file_url += "/"
		file_url += name
		img_count = int(ds_doc.img_count) + 1
		img_name = "_img"+ str(img_count) +".png"
		
		ds_doc.img_2 = img_2
		ds_doc.img_count = img_count

		file_url += img_name
		image_64_decode = base64.decodestring(img_2)
		image_result = open(file_url, 'wb')
		image_result.write(image_64_decode)

		file_doc = frappe.new_doc("File")
		file_doc.file_name = name + img_name
		file_doc.folder = "Home/Attachments"
		file_doc.attached_to_doctype = "Delivery Schedule"
		file_doc.attached_to_name = ds_doc.name
		file_url_attach = get_files_path ()

		file_doc.file_url = "files/" + name + img_name
		file_doc.validate()
		file_doc.insert(ignore_permissions=True)
		ds_doc.save(ignore_permissions=True)
		frappe.db.commit()

	if img_3:
		ds_doc.flags.ignore_permissions = True
		ds_doc.save(ignore_permissions=True)
		file_url = get_files_path ()
		file_url += "/"
		file_url += name
		img_count = int(ds_doc.img_count) + 1
		img_name = "_img"+ str(img_count) +".png"
		
		ds_doc.img_3 = img_3
		ds_doc.img_count = img_count

		file_url += img_name
		image_64_decode = base64.decodestring(img_3)
		image_result = open(file_url, 'wb')
		image_result.write(image_64_decode)

		file_doc = frappe.new_doc("File")
		file_doc.file_name = name + img_name
		file_doc.folder = "Home/Attachments"
		file_doc.attached_to_doctype = "Delivery Schedule"
		file_doc.attached_to_name = ds_doc.name
		file_url_attach = get_files_path ()

		file_doc.file_url = "files/" + name + img_name
		file_doc.validate()
		file_doc.insert(ignore_permissions=True)
		ds_doc.save(ignore_permissions=True)
		frappe.db.commit()

	if img_4:
		ds_doc.flags.ignore_permissions = True
		ds_doc.save(ignore_permissions=True)
		file_url = get_files_path ()
		file_url += "/"
		file_url += name
		img_count = int(ds_doc.img_count) + 1
		img_name = "_img"+ str(img_count) +".png"
		
		ds_doc.img_4 = img_4
		ds_doc.img_count = img_count

		file_url += img_name
		image_64_decode = base64.decodestring(img_4)
		image_result = open(file_url, 'wb')
		image_result.write(image_64_decode)

		file_doc = frappe.new_doc("File")
		file_doc.file_name = name + img_name
		file_doc.folder = "Home/Attachments"
		file_doc.attached_to_doctype = "Delivery Schedule"
		file_doc.attached_to_name = ds_doc.name
		file_url_attach = get_files_path ()

		file_doc.file_url = "files/" + name + img_name
		file_doc.validate()
		file_doc.insert(ignore_permissions=True)
		ds_doc.save(ignore_permissions=True)
		frappe.db.commit()
	return "Delivery Schedule is updated for " + ds_doc.name
	


	

@frappe.whitelist(allow_guest=True)
def update_location_for_delivery_order(name=None, carrier=None, lat=None, lon=None):
	delvery_order = frappe.get_doc("Delivery Order", name)
	if delvery_order:
		delvery_order.flags.ignore_permissions = True
		delvery_order.carrier = carrier
		delvery_order.latitude = lat
		delvery_order.longssitude = lon
		delvery_order.save(ignore_permissions=True)
	return "Location updated for the Delivery Order " + delvery_order.name + " and Carrier " + delvery_order.carrier


@frappe.whitelist(allow_guest=True)
def get_driver_details(first_name=None):
	driver = frappe.get_doc("Driver", first_name)
	if not driver:
		frappe.throw("Driver " + name +" not found...")

	driver_details = {
		"ID" : driver.name,
		"Full Name": driver.full_name,
		"Email ": driver.email_address,
		"Contact Number" : driver.contact_number,
		"Assigned Vehicle No.": driver.carrier,
		}
	return driver_details

@frappe.whitelist(allow_guest=True)
def get_driver_details_from_email(user_id=None):
	driver_id = frappe.db.get_value("Driver", {"user_id":user_id}, "name")
	driver = frappe.get_doc("Driver", driver_id)
	if not driver:
		frappe.throw("Driver " + name +" not found...")

	carrier_type = ""
	if driver.carrier:
		carrier_type = frappe.db.get_value("Carrier",driver.carrier,"type")
	
	driver_details = {
		"ID" : driver.name,
		"Full Name": driver.full_name,
		"Email ": driver.email_address,
		"Contact Number" : driver.contact_number,
		"Profile Picture": driver.profile_picture,
		"Assigned Vehicle No.": driver.carrier,
		"carrier_type": carrier_type,
		}
	return driver_details

@frappe.whitelist(allow_guest=True)
def get_delivery_order_customer_details(name=None):
	delivery_order = frappe.get_doc("Delivery Order", name)
	customer_details = {
		"ID" : delivery_order.name,
		"Full Name": delivery_order.customer,
		"Profile Picture": driver.profile_picture,
		"Email ": delivery_order.customer,
		"Contact Number" : driver.contact_number,
		"Assigned Vehicle No.": driver.vehicle_no
		
	}
	return customer_details

@frappe.whitelist(allow_guest=True)
def get_delivery_schedule_list(user_id=None):
	date=today()
	ds_list = frappe.db.sql("""select name, customer_ref,
		delivery_note_no,date,trip,mobile_no,contact_no,status,
		CONCAT(address_line_1,' ',address_line_2)AS Address 
		from `tabDelivery Schedule` WHERE driver_user_id='{0}' and date='{1}' order by trip""".format(user_id,date),as_dict=1)
	
	return ds_list


@frappe.whitelist(allow_guest=True)
def update_start_loc_in_ds(name=None,lat=None,lon=None):
	ds_doc = frappe.get_doc("Delivery Schedule", str(name))
	if ds_doc.name:
		ds_doc.start_lat = lat
		ds_doc.start_long = lon
		ds_doc.status='In Transit'
		ds_doc.save(ignore_permissions=True)
		frappe.db.commit()
		
		return "Location updated for the Delivery Shedule Latitude " + ds_doc.start_lat+" Longitude "+ds_doc.start_long


@frappe.whitelist(allow_guest=True)
def update_stop_loc_in_ds(name=None,lat=None,lon=None):
	ds_doc = frappe.get_doc("Delivery Schedule", str(name))
	if ds_doc.name:
		ds_doc.stop_lat = lat
		ds_doc.stop_long = lon
		ds_doc.status='Delivered'
		ds_doc.save(ignore_permissions=True)
		frappe.db.commit()
		send_delivery_dispatch_alert(ds_doc.name)
		return "Location updated for the Delivery Shedule Latitude " + ds_doc.stop_lat+" Longitude "+ds_doc.stop_long



def short_url(url):

	base_url = "http://hafarydev.digitalprizm.net/myorder?name="

	url = base_url + url
	post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyDaTiY50Ly3rLN5Ox8R3jpADtri2RT6fcU'
	params = json.dumps({'longUrl': url})
	response = requests.post(post_url,params,headers={'Content-Type': 'application/json'})
	google_url = response.json()
	return google_url['id']


def send_delivery_dispatch_alert(name):


	ds_doc = frappe.get_doc("Delivery Schedule", name)
	ds_name = ds_doc.name
	url_link = short_url(ds_name)
	subject = _("Your hafary order is delivered")
	sender = frappe.session.user not in STANDARD_USERS and frappe.session.user or None
	message="Hi "+ds_doc.contact_person_name+","+" <br> Your Delivery with DN:"+ds_doc.delivery_note_no +" is delivered.<br>For more info click here   "+url_link+"<br>"+"Kindly Find the attachment."
	# attachments = ds_doc.get_attachments()
	recipients = ds_doc.email
	
	ds_doc.send_email(recipients, sender, subject, message, attachments=[frappe.attach_print("Delivery Schedule", name, file_name=name,print_format="Delivery Schedule")])

	ds_doc.save(ignore_permissions=True)

	#send sms
	if ds_doc.mobile_no:
		message = ""
		message += "Hello your order "
		message += ds_doc.delivery_note_no
		message += " is delivered.\nPlease see details \n"
		ds_name = ds_doc.name
		short_url_link = short_url(ds_name)
		message += short_url_link
		send_message_api(ds_doc.mobile_no,message)




#update path
@frappe.whitelist(allow_guest=True)
def update_driving_in_ds(name=None,lat=None,lon=None,):
	ds_doc = frappe.get_doc("Delivery Schedule", str(name))
	
	if ds_doc.start_lat:
		ds_doc.start_lat = lat
	if not ds_doc.start_long:
		ds_doc.start_long = lon
		ds_doc.status='In Transit'
		send_delivery_dispatch_alert(ds_doc.name)
		ds_doc.save(ignore_permissions=True)
		frappe.db.commit()

	if ds_doc.driving_path:
		path_list = ast.literal_eval(ds_doc.driving_path)
		mylist = []
		mylist = [lat,lon]
		path_list.append(mylist)
		ds_doc.driving_path = str(path_list)
		ds_doc.save(ignore_permissions=True)
		frappe.db.commit()
	else:
		path_list=[]
		driving_path_list = []
		path_list.append(lat)
		path_list.append(lon)
		driving_path_list.append(path_list)
		ds_doc.driving_path = str(driving_path_list)
		ds_doc.save(ignore_permissions=True)
		frappe.db.commit()
	return "Location updated for the Delivery Shedule for Dring Path "


@frappe.whitelist(allow_guest=True)
def get_demo():
	get_demo="demo api"
	return get_demo


@frappe.whitelist(allow_guest=True)
def get_single_delivery_shedule(name=None):
	single_delivery_shedule = frappe.db.sql("""select name,customer_ref,date,driver_user_id,
		trip,driver_full_name,
		ifnull(mobile_no, '') AS mobile_no,
		ifnull(trip, '') AS trip,
		ifnull(contact_no, '') AS contact_no,
		ifnull(delivery_note_no, '') AS delivery_note_no,
		CONCAT(ifnull(address_line_1, ''),' ',ifnull(address_line_2, ''), ' ', ifnull(address_line_3, '')) AS address
		from `tabDelivery Schedule` WHERE name='{0}' """.format(name),as_dict=1)
	
	if single_delivery_shedule:
		single_delivery_shedule = single_delivery_shedule[0]
	
	delivery_shedule = {
		"ID" : single_delivery_shedule.name,
		"Customer Ref": single_delivery_shedule.customer_ref,
		"Date": single_delivery_shedule.date,
		"Address Disply":single_delivery_shedule.address,
		"Driver ID": single_delivery_shedule.driver_user_id,
		"Driver Name": single_delivery_shedule.driver_full_name,
		"Trip": single_delivery_shedule.trip,
		"Delivery Note": single_delivery_shedule.delivery_note_no,
		"Mobile No": single_delivery_shedule.mobile_no,
		"Contact No": single_delivery_shedule.contact_no 

	}
	return delivery_shedule



@frappe.whitelist(allow_guest=True)
def get_driver_locations():
	driver_locations = frappe.db.sql(""" select carrier_number,driver,user_id,latitude,longitude from `tabCarrier` """.format(),as_dict=1)

	return driver_locations


@frappe.whitelist(allow_guest=True)
def get_path_delivery_schedule(delivery_note_no=None):
	path_delivery_schedule = frappe.db.sql("""select delivery_note_no, start_lat,stop_lat,driving_path
		from `tabDelivery Schedule` WHERE delivery_note_no='{0}' """.format(delivery_note_no),as_dict=1)
	
	return path_delivery_schedule



@frappe.whitelist(allow_guest=True)
def send_message_api(mobile_no=None,message=None):
	ds_sms = frappe.new_doc("SMS History")
	if mobile_no:
		ds_sms.flags.ignore_permissions = True
		ds_sms.send_to = mobile_no
		ds_sms.message = message
		ds_sms.save(ignore_permissions=True)
		frappe.db.commit()
		send_sms([mobile_no],message)
		return "success"
	else:
		return "SMS not send"




@frappe.whitelist(allow_guest=True)
def get_about():
	data = frappe.db.sql("""select field, value 
		from tabSingles 
		where doctype ='About' 
		and (field = 'title' 
			 OR field = 'description')""", as_dict=1)

	about = {}
	for item in data:
		about.update({item['field']: item['value']})


	return about


@frappe.whitelist(allow_guest=True)
def get_delivery_schedule_list1():
	ds_list = frappe.db.sql("""select name, customer_ref,
		delivery_note_no 
		from `tabDelivery Schedule`""".format(),as_dict=1)
	
	return ds_list



def sc_get_item_for_list_in_html(context):
	# add missing absolute link in files
	# user may forget it during upload
	if (context.get("website_image") or "").startswith("files/"):
		context["website_image"] = "/" + urllib.quote(context["website_image"])

	products_template = 'templates/include/my_product_list.html'
	if cint(frappe.db.get_single_value('Products Settings', 'products_as_list')):
		products_template = 'templates/include/my_product_list.html'

	print "\nsc_get_item_for_list_in_html"
	print products_template
	print context
	return frappe.get_template(products_template).render(context)



@frappe.whitelist(allow_guest=True)
def get_single_delivery(name=None):
	single_delivery_shedule = frappe.get_doc("Delivery Schedule", str(name))

	ds_list = frappe.db.sql("""select name,customer_ref,date,driver_user_id,
		trip,driver_full_name,
		ifnull(mobile_no, '') AS mobile_no,
		ifnull(contact_no, '') AS contact_no,
		ifnull(delivery_note_no, '') AS delivery_note_no,
		CONCAT(address_line_1,' ',address_line_2) AS address,
		ifnull(address,' ') AS address
		from `tabDelivery Schedule` WHERE name='{0}' """.format(name),as_dict=1)
	
	if ds_list:
		ds_list = ds_list[0]
	
	delivery_shedule = {
		"ID" : ds_list.name,
		"Customer Ref": ds_list.customer_ref,
		"Date": ds_list.date,	
		"Driver ID": ds_list.driver_user_id,
		"Driver Name": ds_list.driver_full_name,
		"Trip": ds_list.trip,
		"Delivery Note": ds_list.delivery_note_no,
		"Mobile No": ds_list.mobile_no,
		"Contact No": ds_list.contact_no,
		"Address Disply": ds_list.address

	}

	attachments = get_attachments("Delivery Schedule", single_delivery_shedule.name)
	# attachments.append(frappe.attach_print(self.doctype, self.name, doc=self))
	data = attachments
	k = [sc_get_item_for_list_in_html(r) for r in data]
	k = "".join(k)

	delivery_shedule.update({"attachments":"<h3>Product Images:</h3>"+k})
	print "helllo\n\n"
	print attachments
	return delivery_shedule


@frappe.whitelist(allow_guest=True)
def update_location_for_carrier(name=None,lat=None,lon=None):
	carrier = frappe.get_doc("Carrier", name)
	if carrier.name:
		carrier.flags.ignore_permissions = True
		carrier.latitude = lat
		carrier.longitude = lon
		carrier.save(ignore_permissions=True)
		return "Location updated for the carrier " + carrier.name


#depricated api

#end of depricated api
	
	



