# volunteer_management_frappe_erpnext_app/volunteer_management_frappe_erpnext_app/tests/test_volunteer_management.py

import frappe
import unittest

class TestVolunteerManagement(unittest.TestCase):

    def setUp(self):
        """
        setUp is run before each test method.
        Create any necessary test data.
        """
        pass

    def tearDown(self):
        """
        tearDown is run after each test method.
        Clean up test data if needed.
        """
        pass

    def test_create_volunteer(self):
        """
        Test the creation of a volunteer via Frappe's doc API.
        """
        doc = frappe.get_doc({
            "doctype": "Volunteer",
            "email": "test_create@example.com",
            "skills": ["Testing"],
            "availability": "Weekdays"
        })
        doc.insert()
        frappe.db.commit()

        self.assertTrue(doc.name)
        # Cleanup
        doc.delete()

    def test_rest_api_create_volunteer(self):
        """
        Test the REST API endpoint that creates a volunteer.
        """
        from volunteer_management_frappe_erpnext_app.volunteer_management_frappe_erpnext_app.modules.volunteer_management.rest_api import create_volunteer
        
        response = create_volunteer(
            name="API Test User",
            email="api_test@example.com",
            skills=["API", "Testing"],
            availability="Always"
        )

        self.assertEqual(response.get("status"), "success")
        self.assertIn("data", response)
        volunteer_doc = frappe.get_doc("Volunteer", {"email": "api_test@example.com"})
        self.assertIsNotNone(volunteer_doc)
        # Cleanup
        volunteer_doc.delete()
        frappe.db.commit()
