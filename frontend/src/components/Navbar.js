import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        <Link className="navbar-brand" to="/">Home</Link>
        <div className="collapse navbar-collapse">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/register">Register</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/login">Login</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/children">Children</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/add-child">Add Child</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/caregivers">Caregivers</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;