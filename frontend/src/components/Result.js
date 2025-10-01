import React from "react";

function Result({ data }) {
  return (
    <div style={{ marginTop: 20, padding: 12, border: "1px solid #ddd", borderRadius: 8 }}>
      <h2>📄 Analysis Result</h2>
      <p><strong>Filename:</strong> {data.filename}</p>
      <p><strong>Prediction:</strong> {data.prediction}</p>
      <p><strong>SHA256:</strong> {data.sha256}</p>
      <p><strong>IPFS Hash:</strong> {data.ipfs_hash || "Not uploaded to IPFS"}</p>
      <p><strong>Blockchain Tx:</strong> {data.blockchain_tx || "Not recorded"}</p>
    </div>
  );
}

export default Result;
