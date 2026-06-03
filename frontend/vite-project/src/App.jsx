import { useState } from "react";
import StartupForm from "./components/StartupForm";
import Dashboard from "./pages/Dashboard";
import { analyzeStartup } from "./api/api";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleAnalyze = async (idea) => {
    setLoading(true);
    try {
      const res = await analyzeStartup(idea);
      setResult(res.data);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div>
      {!result ? (
        <StartupForm onSubmit={handleAnalyze} loading={loading} />
      ) : (
        <Dashboard data={result} />
      )}
    </div>
  );
}