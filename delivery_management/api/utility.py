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
from erpnext.setup.doctype.sms_settings.sms_settings import send_sms
#from frappe.core.doctype.sms_settings.sms_settings import send_sms


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
	subject = _("Your hafary order is delivered")
	
	# sender = frappe.session.user not in STANDARD_USERS and frappe.session.user or None
	sender = "contact@digitalprizm.net"
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
		frappe.sendmail(recipients=recipients, sender=sender, subject="Your hafary order is returned",
			message=email_html,  attachments=[frappe.attach_print("Delivery Schedule", name, file_name=name,print_format="Delivery Schedule")])

	
	#send sms

	if ds_doc.mobile_no:
		if ds_doc.is_return=="Yes":
			message = ""
			message += "Hello your order "
			message += ds_doc.delivery_note_no
			message += " is Returned.\nPlease see details \n"
			ds_name = ds_doc.name
			short_url_link = short_url(ds_name)
			message += short_url_link
			send_message_api(ds_doc.mobile_no,message)

		elif ds_doc.is_return=="No":
			message = ""
			message += "Hello your order "
			message += ds_doc.delivery_note_no
			message += " is Delivered.\nPlease see details \n"
			ds_name = ds_doc.name
			short_url_link = short_url(ds_name)
			message += short_url_link
			send_message_api(ds_doc.mobile_no,message)






