import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis
} from "recharts";

export default function RadarChartComp({ data }) {

  const swot = data?.swot || {};

  const chartData = [
    { subject: "Strength", value: swot.strength || 50 },
    { subject: "Weakness", value: swot.weakness || 50 },
    { subject: "Opportunity", value: swot.opportunity || 50 },
    { subject: "Threat", value: swot.threat || 50 }
  ];

  return (
    <RadarChart outerRadius={90} width={500} height={300} data={chartData}>
      <PolarGrid />
      <PolarAngleAxis dataKey="subject" />
      <PolarRadiusAxis />
      <Radar dataKey="value" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
    </RadarChart>
  );
}