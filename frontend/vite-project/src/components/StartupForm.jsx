import { useState } from "react";

export default function StartupForm({ onSubmit, loading }) {
  const [idea, setIdea] = useState("");

  return (
    <div style={{ padding: "20px" }}>
      <h2>Startup Idea Analyzer</h2>

      <textarea
        rows={5}
        cols={50}
        placeholder="Enter startup idea..."
        value={idea}
        onChange={(e) => setIdea(e.target.value)}
      />

      <br />

      <button
        onClick={() => onSubmit(idea)}
        disabled={loading}
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </div>
  );
}