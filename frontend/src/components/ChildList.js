import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ChildList() {
  const [children, setChildren] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/children', {
      headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
    })
      .then(response => {
        setChildren(response.data.children);
      })
      .catch(error => {
        alert('Error fetching children');
      });
  }, []);

  return (
    <div className="container mt-4">
      <h2>Children List</h2>
      <ul>
        {children.map(child => (
          <li key={child.id}>{child.name} - {child.age} years old</li>
        ))}
      </ul>
    </div>
  );
}

export default ChildList;