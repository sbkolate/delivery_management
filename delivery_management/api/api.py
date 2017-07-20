from __future__ import unicode_literals
import frappe, os, json

import base64 

from frappe.utils import strip, get_files_path

from frappe.utils import flt, time_diff_in_hours, get_datetime, getdate, today, cint, get_datetime_str

@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

@frappe.whitelist(allow_guest=True)
def update_img_in_delivery_schedule(name=None,img_1=None):
	ds_doc = frappe.get_doc("Delivery Schedule", name)
	if ds_doc.name:
		ds_doc.flags.ignore_permissions = True
		ds_doc.img_1 = img_1
		ds_doc.save(ignore_permissions=True)
		file_url = get_files_path ()
		file_url += "/"
		file_url += name 
		img_count = int(ds_doc.img_count) + 1
		img_name = "_img"+ str(img_count) +".png"
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
		file_doc.insert()
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
		delivery_note_no,date,trip,mobile_no,contact_no,
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
		return "Location updated for the Delivery Shedule Latitude " + ds_doc.stop_lat+" Longitude "+ds_doc.stop_long
#update path
@frappe.whitelist(allow_guest=True)
def update_driving_in_ds(name=None,lat=None,lon=None,):
	ds_doc = frappe.get_doc("Delivery Schedule", str(name))
	if ds_doc.driving_path:
		import ast
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


