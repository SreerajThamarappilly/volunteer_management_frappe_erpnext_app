# volunteer_management_frappe_erpnext_app/volunteer_management_frappe_erpnext_app/modules/volunteer_management/doctype/volunteer/volunteer.py

import frappe
from frappe.model.document import Document

class Volunteer(Document):
    """
    Volunteer DocType extends the Frappe 'Document' class.
    This class uses OOP concepts: 
      - We add custom methods for business logic related to volunteers.
    """
    
    def validate(self):
        """
        Frappe calls this method automatically during the validation stage
        of the document lifecycle.
        """
        # Example validation: Email must not be empty
        if not self.email:
            frappe.throw("Email is mandatory.")
        
        # Example: Check if email is already registered
        if frappe.db.exists("Volunteer", {"email": self.email, "name": ["!=", self.name]}):
            frappe.throw(f"Volunteer with email {self.email} already exists.")
    
    def before_save(self):
        """
        Called before saving the document to the DB. 
        Useful to set some default values or transformations.
        """
        if not self.availability:
            self.availability = "Flexible"

    def on_update(self):
        """
        Called after the document is updated. 
        Could trigger notifications, logs, or audit events.
        """
        frappe.logger().info(f"Volunteer {self.name} has been updated.")
