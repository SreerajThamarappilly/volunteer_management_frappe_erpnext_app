# volunteer_management_frappe_erpnext_app/volunteer_management_frappe_erpnext_app/hooks.py

app_name = "volunteer_management_frappe_erpnext_app"
app_title = "Volunteer Management App"
app_publisher = "Sreeraj Thamarappilly"
app_description = "An advanced volunteer management system built on Frappe/ERPNext."
app_icon = "octicon octicon-organization"
app_color = "blue"
app_email = "sreeraj.techie@gmail.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------
# JS, CSS includes here if needed

# Installation
# ------------
# before_install = "volunteer_management_frappe_erpnext_app.install.before_install"
# after_install = "volunteer_management_frappe_erpnext_app.install.after_install"

# Scheduled Tasks
# ---------------
# schedule = {
#   "all": ["volunteer_management_frappe_erpnext_app.tasks.all"],
#   "daily": ["volunteer_management_frappe_erpnext_app.tasks.daily"],
#   ...
# }

# DocType Events
doc_events = {
    "Volunteer": {
        "before_insert": "volunteer_management_frappe_erpnext_app.modules.volunteer_management.controllers.on_before_insert_volunteer",
        "after_insert": "volunteer_management_frappe_erpnext_app.modules.volunteer_management.controllers.on_after_insert_volunteer",
        # "validate": ...
    }
}

# Permissions
# -----------
# permission_query_conditions = {
#   "Volunteer": "volunteer_management_frappe_erpnext_app.modules.volunteer_management.controllers.get_permission_query_conditions",
# }

# REST API
# Frappe automatically sets up route: /api/method/<path.to.method>
