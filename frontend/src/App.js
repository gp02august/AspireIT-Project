import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Register from './components/Register';
import Login from './components/Login';
import ChildList from './components/ChildList';
import AddChild from './components/AddChild';
import CaregiverList from './components/CaregiverList';

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <div className="container">
          <Routes>
            <Route path="/register" element={<Register />} />
            <Route path="/login" element={<Login />} />
            <Route path="/children" element={<ChildList />} />
            <Route path="/add-child" element={<AddChild />} />
            <Route path="/caregivers" element={<CaregiverList />} />
            <Route path="/" element={<Register />} /> {/* Default to register */}
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;