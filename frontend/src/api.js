import axios from 'axios';

// Example: if your Frappe site is running at http://localhost:8000
// Adjust to match your local or production URL
const BASE_URL = 'http://localhost:8000';

export async function fetchAllVolunteers() {
  const url = `${BASE_URL}/api/method/volunteer_management_app.volunteer_management_app.modules.volunteer_management.rest_api.get_all_volunteers`;
  const response = await axios.get(url);
  return response.data;
}

export async function createVolunteer(volunteerData) {
  const url = `${BASE_URL}/api/method/volunteer_management_app.volunteer_management_app.modules.volunteer_management.rest_api.create_volunteer`;
  const response = await axios.post(url, volunteerData);
  return response.data;
}
