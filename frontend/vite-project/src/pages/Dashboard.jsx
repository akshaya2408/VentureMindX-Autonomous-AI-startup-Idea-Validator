import ScoreCard from "../components/ScoreCard";
import RadarChart from "../components/RadarChart";
import RAGSearch from "../components/RAGSearch";

export default function Dashboard({ data }) {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Startup Analysis Dashboard</h1>

      <ScoreCard score={data.score} />

      <RadarChart data={data.radar} />

      <h3>Market Analysis</h3>
      <p>{data.market_analysis}</p>

      <h3>SWOT Analysis</h3>
      <pre>{JSON.stringify(data.swot, null, 2)}</pre>

      <h3>Competitors</h3>
      <ul>
        {data.competitors?.map((c, i) => (
          <li key={i}>{c}</li>
        ))}
      </ul>

      <RAGSearch />
    </div>
  );
}