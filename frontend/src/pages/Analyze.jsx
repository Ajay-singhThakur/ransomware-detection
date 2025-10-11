import React from 'react';
import FileUpload from '../components/FileUpload';

const Analyze = () => {
  return (
    <div>
      <h2 style={{ textAlign: 'center', marginBottom: '2rem' }}>Analyze a New File</h2>
      <FileUpload />
    </div>
  );
};

export default Analyze;