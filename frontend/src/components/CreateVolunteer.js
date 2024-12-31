import React, { useState } from 'react';
import { createVolunteer } from '../api';

function CreateVolunteer() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [skills, setSkills] = useState([]);
  const [message, setMessage] = useState('');

  async function handleCreate(e) {
    e.preventDefault();
    try {
      const skillArray = skills.length ? skills.split(',').map(s => s.trim()) : [];
      const newVolunteer = { name, email, skills: skillArray };
      const data = await createVolunteer(newVolunteer);
      setMessage(data.message || 'Volunteer created');
    } catch (err) {
      setMessage(err.message);
    }
  }

  return (
    <div style={{ marginBottom: '1rem' }}>
      <h2>Create Volunteer</h2>
      <form onSubmit={handleCreate}>
        <div>
          <label>Name: </label>
          <input 
            type="text" 
            value={name} 
            onChange={(e) => setName(e.target.value)} 
            required 
          />
        </div>
        <div>
          <label>Email: </label>
          <input 
            type="email" 
            value={email} 
            onChange={(e) => setEmail(e.target.value)} 
            required 
          />
        </div>
        <div>
          <label>Skills (comma separated): </label>
          <input 
            type="text" 
            value={skills} 
            onChange={(e) => setSkills(e.target.value)} 
          />
        </div>
        <button type="submit">Create</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default CreateVolunteer;
