from __future__ import unicode_literals
import frappe, os, json

import base64 

from frappe.utils import strip, get_files_path
from frappe.desk.form.load import get_attachments

from frappe.utils import flt, time_diff_in_hours, get_datetime, getdate, today, cint, get_datetime_str
from erpnext.setup.doctype.sms_settings.sms_settings import send_sms
import ast

@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

@frappe.whitelist(allow_guest=True)
def update_img_in_delivery_schedule(name=None,img_1=None,img_2=None,img_3=None,img_4=None):
	ds_doc = frappe.get_doc("Delivery Schedule", name)
	
	file_url = get_files_path ()

	file_url += "/"
	file_url += name
	img_count = int(ds_doc.img_count) 

	
	if ds_doc.name:
		ds_doc.img_1=img_1
		print("##########################")
		print(ds_doc.img_1)

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
		ds_doc.img_2=img_2
		print("##########################")
		print(ds_doc.img_2)

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
		ds_doc.img_3=img_3
		print("##########################")
		print(ds_doc.img_3)
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
		ds_doc.img_4=img_4
		print("##########################")
		print(ds_doc.img_4)
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
def update_location_for_carrier(name=None,lat=None,lon=None):
	carrier = frappe.get_doc("Carrier", name)
	if carrier.name:
		carrier.flags.ignore_permissions = True
		carrier.latitude = lat
		carrier.longitude = lon
		carrier.save(ignore_permissions=True)
		return "Location updated for the carrier " + carrier.name
	

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
	print "hi"
	if ds_doc.name:
		ds_doc.start_lat = lat
		ds_doc.start_long = lon
		ds_doc.status='In Transit'
		ds_doc.save(ignore_permissions=True)
		frappe.db.commit()
		send_delivery_dispatch_alert(ds_doc.name)
		return "Location updated for the Delivery Shedule Latitude " + ds_doc.start_lat+" Longitude "+ds_doc.start_long
from bitly import ping

import json
import requests
def short_url(url):
	base_url = "https://hafardev/name="
	url = base_url + url
	post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyDaTiY50Ly3rLN5Ox8R3jpADtri2RT6fcU'
	params = json.dumps({'longUrl': url})
	response = requests.post(post_url,params,headers={'Content-Type': 'application/json'})
	google_url = response.json()
	return google_url['id']

def send_delivery_dispatch_alert(name):
	ds_doc = frappe.get_doc("Delivery Schedule", name)
	#send email
	frappe.sendmail(recipients=ds_doc.email, sender=None, subject="Delivery Report",
			message="Hi "+ds_doc.contact_person_name+","+" <br> Your Delivery with DN:"+ds_doc.name +" is dispatched.<br>"
			"Kindly Find the attachment.",attachments=[frappe.attach_print("Delivery Schedule", ds_doc.name, file_name=ds_doc.name,print_format="Standard")])
	# ds_doc.save(ignore_permissions=True)
	#send sms
	message = ""
	message += "Hello your order "
	message += ds_doc.delivery_note_no
	message += " is dispatched. please see details "
	ds_name = ds_doc.name
	short_url_link = short_url(ds_name)
	message += short_url_link
	send_message_api(ds_doc.mobile_no,message)



@frappe.whitelist(allow_guest=True)
def update_stop_loc_in_ds(name=None,lat=None,lon=None):
	ds_doc = frappe.get_doc("Delivery Schedule", str(name))
	if ds_doc.name:
		ds_doc.stop_lat = lat
		ds_doc.stop_long = lon
		ds_doc.status='Delivered'
		ds_doc.save(ignore_permissions=True)
		frappe.db.commit()
		return "Location updated for the Delivery Shedule Latitude " + ds_doc.stop_lat+" Longitude "+ds_doc.stop_long
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
	single_delivery_shedule = frappe.get_doc("Delivery Schedule", str(name))
	addr = ""
	seq = (str(single_delivery_shedule.address_line_1)," ",str(single_delivery_shedule.address_line_2))
	addr = addr.join(seq)
	delivery_shedule = {
		"ID" : single_delivery_shedule.name,
		"Customer Ref": single_delivery_shedule.customer_ref,
		"Date": single_delivery_shedule.date,
		"Address Disply": addr,
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




@frappe.whitelist(allow_guest=True)
def get_single_delivery(name=None):
	single_delivery_shedule = frappe.get_doc("Delivery Schedule", str(name))
	addr = ""
	seq = (str(single_delivery_shedule.address_line_1)," ",str(single_delivery_shedule.address_line_2))
	addr = addr.join(seq)
	delivery_shedule = {
		"ID" : single_delivery_shedule.name,
		"Customer Ref": single_delivery_shedule.customer_ref,
		"Date": single_delivery_shedule.date,
		"Address Disply": addr,
		"Driver ID": single_delivery_shedule.driver_user_id,
		"Driver Name": single_delivery_shedule.driver_full_name,
		"Trip": single_delivery_shedule.trip,
		"Delivery Note": single_delivery_shedule.delivery_note_no,
		"Mobile No": single_delivery_shedule.mobile_no,
		"Contact No": single_delivery_shedule.contact_no 

	}

	attachments = get_attachments("Delivery Schedule", single_delivery_shedule.name)
	# attachments.append(frappe.attach_print(self.doctype, self.name, doc=self))
	
	delivery_shedule.update({"attachments":attachments})
	print "helllo\n\n"
	print attachments
	return delivery_shedule




	
	



