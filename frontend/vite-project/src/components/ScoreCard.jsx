export default function ScoreCard({ data }) {

  const score = data?.investor?.vc_score || 0;

  return (
    <div style={{ marginTop: 20 }}>
      <h2>🧠 VC Readiness Score</h2>

      <div style={{
        fontSize: "40px",
        fontWeight: "bold",
        color: score > 70 ? "green" : "orange"
      }}>
        {score}/100
      </div>
    </div>
  );
}