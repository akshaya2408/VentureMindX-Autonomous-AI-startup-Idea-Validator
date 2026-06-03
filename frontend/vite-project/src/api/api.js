import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const analyzeStartup = (idea) => {
  return API.post("/analyze", { idea });
};

export const ragSearch = (query) => {
  return API.post("/rag-search", { query });
};