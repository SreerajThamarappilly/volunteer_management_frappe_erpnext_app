# volunteer_management_frappe_erpnext_app/volunteer_management_frappe_erpnext_app/modules/volunteer_management/rest_api.py

import frappe
from volunteer_management_frappe_erpnext_app.volunteer_management_frappe_erpnext_app.modules.volunteer_management.services import (
    cache_volunteer_data, 
    get_cached_volunteer_data
)

@frappe.whitelist(allow_guest=True)
def get_all_volunteers():
    """
    GET /api/method/volunteer_management_frappe_erpnext_app.volunteer_management_frappe_erpnext_app.modules.volunteer_management.rest_api.get_all_volunteers

    Fetches all volunteers. Returns JSON array of volunteer objects.
    """
    volunteers = frappe.get_all("Volunteer", fields=["name", "email", "skills", "availability"])
    return {
        "status": "success",
        "data": volunteers
    }

@frappe.whitelist()
def create_volunteer(**kwargs):
    """
    POST /api/method/volunteer_management_frappe_erpnext_app.volunteer_management_frappe_erpnext_app.modules.volunteer_management.rest_api.create_volunteer
    Body (JSON):
    {
        "name": "John Doe",
        "email": "john@example.com",
        "skills": ["Python", "Data Analysis"],
        "availability": "Weekends"
    }

    Creates a new Volunteer document in Frappe.
    """
    name = kwargs.get('name')
    email = kwargs.get('email')
    skills = kwargs.get('skills', [])
    availability = kwargs.get('availability', '')

    if not name or not email:
        frappe.throw("Name and Email are mandatory fields.")

    # Create the document
    doc = frappe.get_doc({
        "doctype": "Volunteer",
        "name": name,
        "email": email,
        "skills": skills,
        "availability": availability
    })
    doc.insert()
    frappe.db.commit()

    # Cache the newly created volunteer data
    cache_volunteer_data(email, doc.as_dict())

    return {
        "status": "success",
        "message": f"Volunteer {name} created successfully.",
        "data": doc.as_dict()
    }

@frappe.whitelist(allow_guest=True)
def get_volunteer(email):
    """
    GET /api/method/volunteer_management_frappe_erpnext_app.volunteer_management_frappe_erpnext_app.modules.volunteer_management.rest_api.get_volunteer?email=john@example.com

    Fetches a single volunteer by email. Demonstrates usage of a caching layer.
    """
    cached = get_cached_volunteer_data(email)
    if cached:
        return {
            "status": "success",
            "data": cached,
            "cached": True
        }
    
    volunteer = frappe.db.get_value("Volunteer", {"email": email}, ["name", "email", "skills", "availability"], as_dict=True)
    if volunteer:
        # Cache the data
        cache_volunteer_data(email, volunteer)
        return {
            "status": "success",
            "data": volunteer,
            "cached": False
        }
    else:
        return {
            "status": "error",
            "message": f"No volunteer found with email {email}"
        }
