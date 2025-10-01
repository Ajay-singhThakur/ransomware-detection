import React from "react";
import { uploadFile } from "../api";
import { toast } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';

toast.configure();

function FileUpload({ setResult }) {
  const handleSubmit = async (e) => {
    e.preventDefault();
    const file = e.target.file.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const { data } = await uploadFile(formData);
      setResult(data);

      toast.success("File uploaded successfully!");
      if (data.prediction === "Ransomware") {
        toast.error("⚠️ Ransomware detected!");
      } else {
        toast.info("File is clean ✅");
      }

    } catch (err) {
      toast.error("Upload failed ❌");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" name="file" required />
      <button type="submit">Upload</button>
    </form>
  );
}

export default FileUpload;
