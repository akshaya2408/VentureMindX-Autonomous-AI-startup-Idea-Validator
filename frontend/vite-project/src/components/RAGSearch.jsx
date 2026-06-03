import { useState } from "react";
import { ragSearch } from "../api/api";

export default function RAGSearch() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const res = await ragSearch(query);
    setResults(res.data.results);
  };

  return (
    <div>
      <h3>Find Similar Startups</h3>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={handleSearch}>Search</button>

      <ul>
        {results.map((r, i) => (
          <li key={i}>{r}</li>
        ))}
      </ul>
    </div>
  );
}