import React, { useEffect, useState } from 'react';
import axios from 'axios';

function CaregiverList() {
  const [caregivers, setCaregivers] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/caregivers', {
      headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
    })
      .then(response => {
        setCaregivers(response.data);
      })
      .catch(error => {
        alert('Error fetching caregivers');
      });
  }, []);

  return (
    <div className="container mt-4">
      <h2>Caregiver List</h2>
      <ul>
        {caregivers.map(caregiver => (
          <li key={caregiver.id}>{caregiver.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default CaregiverList;