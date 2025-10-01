import axios from "axios";

const BASE = process.env.REACT_APP_API || "http://localhost:5000";
const API = axios.create({ baseURL: BASE });

export const uploadFile = (formData) =>
  API.post("/upload", formData, { headers: { "Content-Type": "multipart/form-data" } });
