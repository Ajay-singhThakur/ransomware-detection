import React from 'react';

const Register = () => {
  const formStyle = {
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem',
    maxWidth: '400px',
    margin: '0 auto',
  };
  const inputStyle = {
    padding: '10px',
    borderRadius: '4px',
    border: '1px solid #ccc',
  };
  const buttonStyle = {
    padding: '10px',
    borderRadius: '4px',
    border: 'none',
    backgroundColor: '#007bff',
    color: 'white',
    cursor: 'pointer',
  };

  return (
    <div>
      <h2 style={{ textAlign: 'center' }}>Register</h2>
      <form style={formStyle} onSubmit={(e) => e.preventDefault()}>
        <input type="text" placeholder="Username" style={inputStyle} />
        <input type="email" placeholder="Email" style={inputStyle} />
        <input type="password" placeholder="Password" style={inputStyle} />
        <button type="submit" style={buttonStyle}>Create Account</button>
      </form>
    </div>
  );
};

export default Register;