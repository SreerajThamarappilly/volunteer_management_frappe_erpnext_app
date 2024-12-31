// frontend/src/api.js

import axios from 'axios';
import CONFIG from './config/config';

// Base API URL from config.js
const BASE_URL = CONFIG.API_BASE_URL;

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
