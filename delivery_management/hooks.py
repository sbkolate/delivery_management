# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "delivery_management"
app_title = "Delivery Management"
app_publisher = "DPI-Sagar"
app_description = "Delivery Management"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sagar@digitalprizm.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/delivery_management/css/delivery_management.css"
# app_include_js = "/assets/delivery_management/js/delivery_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/delivery_management/css/delivery_management.css"
# web_include_js = "/assets/delivery_management/js/delivery_management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "delivery_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "delivery_management.install.before_install"
# after_install = "delivery_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

notification_config = "delivery_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"delivery_management.tasks.all"
# 	],
# 	"daily": [
# 		"delivery_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"delivery_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"delivery_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"delivery_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "delivery_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "delivery_management.event.get_events"
# }

