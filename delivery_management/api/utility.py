from __future__ import unicode_literals

import frappe, os, json, json
from frappe import _
import json
import requests
import ast
from bitly import ping
from frappe.utils import strip, get_files_path
from frappe.desk.form.load import get_attachments

from frappe.utils import flt, time_diff_in_hours, get_datetime, getdate, today, cint, get_datetime_str

#from erpnext.setup.doctype.sms_settings.sms_settings import send_sms
from frappe.core.doctype.sms_settings.sms_settings import send_sms

from frappe.desk.form.load import get_attachments
from frappe.core.doctype.communication.email import make

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
def update_location_for_carrier(name=None,lat=None,lon=None):
	carrier = frappe.get_doc("Carrier", name)
	if carrier.name:
		carrier.flags.ignore_permissions = True
		carrier.latitude = lat
		carrier.longitude = lon
		carrier.save(ignore_permissions=True)
		frappe.db.commit()
		return "Location updated for the carrier " + carrier.name



def short_url(url):
	host_name = frappe.get_site_config().host_name
	# base_url = "http://hafarydev.digitalprizm.net/myorder?name="
	base_url = host_name + "/myorder?name=" + url
	print "********\n\n\n"
	print(base_url)
	post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyDaTiY50Ly3rLN5Ox8R3jpADtri2RT6fcU'
	params = json.dumps({'longUrl': base_url})
	response = requests.post(post_url,params,headers={'Content-Type': 'application/json'})
	google_url = response.json()
	print (google_url['id'])
	return google_url['id']


def send_delivery_dispatch_alert(name):
	ds_doc = frappe.get_doc("Delivery Schedule", str(name))
	ds_name = ds_doc.name
	url_link = short_url(ds_name)
	subject_line = "Your Hafary order "
	if ds_doc.delivery_note_no:
		subject_line += ds_doc.delivery_note_no
		subject_line += " "
	subject_line += "is delivered"

	subject = _(subject_line)
	
	# sender = frappe.session.user not in STANDARD_USERS and frappe.session.user or None
	sender = "enquiry@hafary.com.sg"
	if ds_doc.is_return=="No":
		message="Hi "+ds_doc.contact_person_name+","+" <br> Your Delivery with DN:"+ds_doc.delivery_note_no +" is delivered.<br>For more info click here   "+url_link+"<br>"+"Kindly Find the attachment."
	elif ds_doc.is_return=="Yes":
		message="Hi "+ds_doc.contact_person_name+","+" <br> Your Delivery with DN:"+ds_doc.name +" is Returned.<br>For more info click here   "+url_link+"<br>"+"Kindly Find the attachment."

	# attachments = ds_doc.get_attachments()
	recipients = ds_doc.email
	email_html = frappe.render_template("templates/include/dispatchalert.html", {"doc":ds_doc, "short_url": url_link })
	
	# ds_doc.send_email(recipients, sender, subject, message, attachments=[frappe.attach_print("Delivery Schedule", name, file_name=name,print_format="Delivery Schedule")])
	
	#convert msg html
	
	if ds_doc.is_return=="No":
		frappe.sendmail(recipients=recipients, sender=sender, subject=subject,
			message=email_html,  attachments=[frappe.attach_print("Delivery Schedule", name, file_name=name,print_format="Delivery Schedule")])
	elif ds_doc.is_return=="Yes":
		frappe.sendmail(recipients=recipients, sender=sender, subject="Your Hafary order is returned",
			message=email_html,  attachments=[frappe.attach_print("Delivery Schedule", name, file_name=name,print_format="Delivery Schedule")])

	
	#send sms

	if ds_doc.mobile_no:
		if ds_doc.is_return=="Yes":
			message = ""
			message += "Hello your order "
			message += ds_doc.delivery_note_no
			message += " has been Returned.\nClick "
			ds_name = ds_doc.name
			short_url_link = short_url(ds_name)
			message += short_url_link
			message += " to view details.\nThank you."

		elif ds_doc.is_return=="No":
			message = ""
			message += "Hello your order "
			message += ds_doc.delivery_note_no
			message += " has been Delivered.\nClick "
			ds_name = ds_doc.name
			short_url_link = short_url(ds_name)
			message += short_url_link
			message += " to view details.\nThank you."

			send_message_api(ds_doc.mobile_no,message)



def sc_get_item_for_list_in_html(context):
	# add missing absolute link in files
	# user may forget it during upload
	if (context.get("website_image") or "").startswith("files/"):
		context["website_image"] = "/" + urllib.quote(context["website_image"])

	products_template = 'templates/include/my_product_list.html'
	if cint(frappe.db.get_single_value('Products Settings', 'products_as_list')):
		products_template = 'templates/include/my_product_list.html'

	return frappe.get_template(products_template).render(context)


@frappe.whitelist(allow_guest=True)
def get_single_delivery_myorderpage(name=None):
	single_delivery_shedule = frappe.get_doc("Delivery Schedule", str(name))

	ds_list = frappe.db.sql("""select name,customer_ref,date,driver_user_id,
		trip,driver_full_name,
		ifnull(mobile_no, '') AS mobile_no,
		ifnull(contact_no, '') AS contact_no,
		ifnull(delivery_note_no, '') AS delivery_note_no,
		ifnull(address_line_1, '')AS address1,
		ifnull(address_line_2, '')AS address2,
		ifnull(address_line_3, '')AS address3,
		ifnull(pin_code, '')AS pin_code

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
		"Address Line1": ds_list.address1,
		"Address Line2": ds_list.address2,
		"Address Line3": ds_list.address3,
		"pin_code": ds_list.pin_code

	}

	attachments = get_attachments("Delivery Schedule", single_delivery_shedule.name)
	data = attachments
	k = [sc_get_item_for_list_in_html(r) for r in data]
	k = "".join(k)

	delivery_shedule.update({"attachments":"<h3>Product Images:</h3>"+k})
	return delivery_shedule







