import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  const containerStyle = {
    textAlign: 'center',
    padding: '2rem'
  };

  const buttonStyle = {
    display: 'inline-block',
    marginTop: '1.5rem',
    padding: '12px 24px',
    backgroundColor: '#007bff',
    color: 'white',
    textDecoration: 'none',
    borderRadius: '5px',
    fontSize: '1rem',
    fontWeight: 'bold'
  };

  return (
    <div style={containerStyle}>
      <h2>Welcome to the Decentralized File Analyzer</h2>
      <p>
        Securely analyze your files for threats. All results are logged immutably
        on a decentralized network.
      </p>
      <Link to="/analyze" style={buttonStyle}>
        Get Started
      </Link>
    </div>
  );
};

export default Home;