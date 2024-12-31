# volunteer_management_frappe_erpnext_app/volunteer_management_frappe_erpnext_app/modules/volunteer_management/controllers.py

import frappe

def on_before_insert_volunteer(doc, method):
    """
    Triggered by doc_events['Volunteer']['before_insert'].
    We can do cross-validation or modify doc before insert.
    """
    frappe.logger().debug(f"Before insert for Volunteer: {doc.name}")

def on_after_insert_volunteer(doc, method):
    """
    Triggered by doc_events['Volunteer']['after_insert'].
    For example, you could send a welcome email.
    """
    frappe.logger().info(f"New volunteer added: {doc.name}")
    # Hypothetical function for sending an email
    # send_welcome_email(doc.email)

def get_permission_query_conditions(user):
    """
    If you want to restrict access so volunteers can only view certain records,
    implement the condition here.
    """
    if not user: 
        user = frappe.session.user
    # Example logic
    if "Volunteer Manager" not in frappe.get_roles(user):
        return """`tabVolunteer`.owner = '{0}'""".format(user)

    return ""
