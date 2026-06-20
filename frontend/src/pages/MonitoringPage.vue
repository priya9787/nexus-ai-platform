<script setup>
const metrics = [
  { label: "Backend API", value: "FastAPI" },
  { label: "Streaming", value: "SSE" },
  { label: "Vector DB", value: "Qdrant" },
  { label: "Evaluation", value: "Planned" },
];

const signals = [
  { name: "Chat stream", status: "Active" },
  { name: "Document upload", status: "Active" },
  { name: "Qdrant vector search", status: "Active" },
  { name: "RAGAS evaluation", status: "Planned" },
  { name: "LangSmith traces", status: "Planned" },
];
</script>

<template>
  <div class="page">
    <header class="page-header">
      <p class="eyebrow">Evaluation and observability</p>
      <h1>Monitoring</h1>
      <p>Track the services that are active in this build, with planned quality evaluation clearly separated.</p>
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
        <p class="panel-note">Sample visualization reserved for future RAGAS or LangSmith evaluation runs.</p>
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
        <div
          v-for="signal in signals"
          :key="signal.name"
          class="signal-row"
        >
          <span>{{ signal.name }}</span>
          <strong :class="signal.status.toLowerCase()">{{ signal.status }}</strong>
        </div>
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

.panel p,
.signal-row {
  padding: 14px;
  border-radius: 12px;
  background: #1e293b;
  color: #cbd5e1;
}

.panel-note {
  margin: -6px 0 18px;
  line-height: 1.5;
}

.signal-row {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 12px;
}

.signal-row strong {
  color: #86efac;
}

.signal-row strong.planned {
  color: #fde68a;
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
