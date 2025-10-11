import React, { useState } from 'react';
import api from '../services/api';
import './FileUpload.css';

const FileUpload = () => {
    const [file, setFile] = useState(null);
    const [response, setResponse] = useState(null);
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setResponse(null);
        setError('');
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) {
            setError('Please select a file to upload.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        setIsLoading(true);
        setError('');
        setResponse(null);

        try {
            const res = await api.post('/api/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setResponse(res.data);
        } catch (err) {
            setError(err.response?.data?.error || 'An unexpected error occurred.');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="upload-container">
            <form onSubmit={handleSubmit}>
                <label htmlFor="file-upload" className="custom-file-upload">
                    {file ? file.name : 'Choose File'}
                </label>
                <input id="file-upload" type="file" onChange={handleFileChange} />
                <button type="submit" disabled={!file || isLoading}>
                    {isLoading ? 'Analyzing...' : 'Upload & Analyze'}
                </button>
            </form>

            {error && <p className="error-message">{error}</p>}
            
            {response && (
                <div className="response-card">
                    <h3>Analysis Complete!</h3>
                    <p>
                        <strong>Result:</strong> 
                        <span className={response.ml_result.includes('Malicious') ? 'malicious' : 'safe'}>{response.ml_result}</span>
                    </p>
                    <p>
                        <strong>IPFS CID:</strong> 
                        <span>{response.ipfs_cid}</span>
                    </p>
                    <p>
                        <strong>File Hash:</strong> 
                        <span>{response.file_hash.substring(0, 40)}...</span>
                    </p>
                    <p>
                        <strong>Blockchain TX:</strong> 
                        <span>{response.blockchain_tx.substring(0, 40)}...</span>
                    </p>
                </div>
            )}
        </div>
    );
};

export default FileUpload;