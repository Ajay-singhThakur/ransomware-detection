import React from 'react';

const Login = () => {
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
    backgroundColor: '#28a745',
    color: 'white',
    cursor: 'pointer',
  };

  return (
    <div>
      <h2 style={{ textAlign: 'center' }}>Login</h2>
      <form style={formStyle} onSubmit={(e) => e.preventDefault()}>
        <input type="email" placeholder="Email" style={inputStyle} />
        <input type="password" placeholder="Password" style={inputStyle} />
        <button type="submit" style={buttonStyle}>Sign In</button>
      </form>
    </div>
  );
};

export default Login;