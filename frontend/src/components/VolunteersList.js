import React, { useEffect, useState } from 'react';
import { fetchAllVolunteers } from '../api';

function VolunteersList() {
  const [volunteers, setVolunteers] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    loadVolunteers();
  }, []);

  async function loadVolunteers() {
    try {
      setError('');
      const data = await fetchAllVolunteers();
      if (data.status === 'success') {
        setVolunteers(data.data);
      } else {
        setError(data.message || 'Error fetching volunteers');
      }
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <div>
      <h2>Volunteers</h2>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <ul>
        {volunteers.map((v) => (
          <li key={v.name}>
            <strong>{v.name}</strong> - {v.email} - Skills: {JSON.stringify(v.skills)}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default VolunteersList;
