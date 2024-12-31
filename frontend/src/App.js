import React from 'react';
import VolunteersList from './components/VolunteersList';
import CreateVolunteer from './components/CreateVolunteer';

function App() {
  return (
    <div style={{ margin: '1rem' }}>
      <h1>Volunteer Management</h1>
      <CreateVolunteer />
      <VolunteersList />
    </div>
  );
}

export default App;
