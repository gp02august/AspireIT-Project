import React, { useState } from 'react';
import axios from 'axios';

function AddChild() {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    caregiver_id: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://127.0.0.1:5000/api/children', formData, {
      headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
    })
      .then(response => {
        alert('Child added successfully');
      })
      .catch(error => {
        alert('Error adding child');
      });
  };

  return (
    <div className="container mt-4">
      <h2>Add Child</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Name</label>
          <input
            type="text"
            className="form-control"
            value={formData.name}
            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
          />
        </div>
        <div className="form-group">
          <label>Age</label>
          <input
            type="number"
            className="form-control"
            value={formData.age}
            onChange={(e) => setFormData({ ...formData, age: e.target.value })}
          />
        </div>
        <div className="form-group">
          <label>Caregiver ID</label>
          <input
            type="text"
            className="form-control"
            value={formData.caregiver_id}
            onChange={(e) => setFormData({ ...formData, caregiver_id: e.target.value })}
          />
        </div>
        <button type="submit" className="btn btn-primary">Add Child</button>
      </form>
    </div>
  );
}

export default AddChild;