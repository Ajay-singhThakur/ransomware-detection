import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Import components and pages
import Navbar from './components/Navbar.jsx';
import Home from './pages/Home.jsx';             // <-- Add .jsx
import Analyze from './pages/Analyze.jsx';       // <-- Add .jsx
import Dashboard from './pages/Dashboard.jsx';   // <-- Add .jsx
import Login from './pages/Login.jsx';           // <-- Add .jsx
import Register from './pages/Register.jsx';     // <-- Add .jsx
import './App.css';

function App() {
  return (
    <Router>
      <div className="container">
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/analyze" element={<Analyze />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;