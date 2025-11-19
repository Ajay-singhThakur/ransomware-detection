import React, { useState, useEffect } from 'react';
import api from '../services/api'; // Your API service
import './Dashboard.css'; // We will create this file for styling

const Dashboard = () => {
  const [files, setFiles] = useState([]);
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(true);

  // Get the IP address for the gateway from the browser's URL
  const gatewayBaseUrl = `http://${window.location.hostname}:8080/ipfs/`;

  useEffect(() => {
    const fetchFiles = async () => {
      try {
        setIsLoading(true);
        setError('');
        const response = await api.get('/api/files');
        setFiles(response.data);
      } catch (err) {
        setError('Failed to fetch files. Please try again later.');
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchFiles();
  }, []);

  if (isLoading) {
    return <h2 style={{ textAlign: 'center' }}>Loading file list...</h2>;
  }

  if (error) {
    return <h2 style={{ textAlign: 'center', color: 'red' }}>{error}</h2>;
  }

  return (
    <div className="dashboard-container">
      <h2 style={{ textAlign: 'center' }}>Uploaded File Dashboard</h2>
      
      {files.length === 0 ? (
        <p style={{ textAlign: 'center' }}>No files uploaded yet.</p>
      ) : (
        <table className="file-table">
          <thead>
            <tr>
              <th>File Name</th>
              <th>Type</th>
              <th>Size</th>
              <th>CID (Hash)</th>
              <th>Gateway Link</th>
            </tr>
          </thead>
          <tbody>
            {files.map((file) => (
              <tr key={file.Hash}>
                <td>{file.Name}</td>
                <td>{file.Type === 0 ? 'File' : 'Directory'}</td>
                <td>{(file.Size / 1024).toFixed(2)} KB</td>
                <td className="cid-cell">{file.Hash}</td>
                <td>
                  <a 
                    href={`${gatewayBaseUrl}${file.Hash}`} 
                    target="_blank" 
                    rel="noopener noreferrer"
                  >
                    Open File
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default Dashboard;