import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import Result from "./components/Result";
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>🔐 AI-Powered Ransomware Detection</h1>
      <FileUpload setResult={setResult} />
      {result && <Result data={result} />}
      <ToastContainer position="top-right" autoClose={3000} />
    </div>
  );
}

export default App;
