<script setup>
const metrics = [
  { label: "Faithfulness", value: "0.87" },
  { label: "Answer relevancy", value: "0.91" },
  { label: "P95 latency", value: "1.4s" },
  { label: "Token cost", value: "$12.40" },
];
</script>

<template>
  <div class="page">
    <header class="page-header">
      <p class="eyebrow">Evaluation and observability</p>
      <h1>Monitoring</h1>
      <p>Track RAG quality, latency, agent execution, and production reliability.</p>
    </header>

    <section class="metrics-grid">
      <article v-for="metric in metrics" :key="metric.label" class="metric-card">
        <p>{{ metric.label }}</p>
        <h2>{{ metric.value }}</h2>
      </article>
    </section>

    <section class="monitor-grid">
      <article class="panel large">
        <h2>Quality Trend</h2>
        <div class="chart-bars">
          <span style="height: 45%"></span>
          <span style="height: 62%"></span>
          <span style="height: 58%"></span>
          <span style="height: 74%"></span>
          <span style="height: 82%"></span>
          <span style="height: 88%"></span>
        </div>
      </article>

      <article class="panel">
        <h2>Live Signals</h2>
        <p>LangSmith traces</p>
        <p>RAGAS evaluation</p>
        <p>Redis cache health</p>
        <p>Qdrant vector search</p>
      </article>
    </section>
  </div>
</template>

<style scoped>
.page {
  height: 100%;
  overflow-y: auto;
}

.eyebrow {
  margin: 0 0 8px;
  color: #38bdf8;
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
}

h1 {
  margin: 0;
  color: white;
  font-size: 34px;
}

.page-header p:last-child {
  margin: 10px 0 0;
  color: #94a3b8;
}

.metrics-grid,
.monitor-grid {
  display: grid;
  gap: 20px;
  margin-top: 20px;
}

.metrics-grid {
  grid-template-columns: repeat(4, 1fr);
}

.monitor-grid {
  grid-template-columns: 1.5fr 1fr;
}

.metric-card,
.panel {
  padding: 24px;
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 18px;
  background: #111827;
  color: white;
}

.metric-card p {
  margin: 0;
  color: #94a3b8;
  font-weight: 800;
}

.metric-card h2 {
  margin: 12px 0 0;
  font-size: 34px;
}

.panel h2 {
  margin: 0 0 20px;
}

.panel p {
  padding: 14px;
  border-radius: 12px;
  background: #1e293b;
  color: #cbd5e1;
}

.chart-bars {
  height: 260px;
  display: flex;
  align-items: end;
  gap: 14px;
  padding: 20px;
  border-radius: 14px;
  background: #0f172a;
}

.chart-bars span {
  flex: 1;
  border-radius: 10px 10px 0 0;
  background: linear-gradient(180deg, #38bdf8, #2563eb);
}

@media (max-width: 1000px) {
  .metrics-grid,
  .monitor-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 700px) {
  .metrics-grid,
  .monitor-grid {
    grid-template-columns: 1fr;
  }
}
</style>