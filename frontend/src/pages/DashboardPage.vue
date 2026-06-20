<script setup>
import StatCard from "../components/StatCard.vue";

const stats = [
  { title: "Vector Store", value: "Qdrant", meta: "Stores document chunks and embeddings" },
  { title: "Retriever Top K", value: "5", meta: "Nearest-neighbor search per question" },
  { title: "Chunking", value: "500 / 100", meta: "Recursive chunk size and overlap" },
  { title: "RBAC Retrieval", value: "Enabled", meta: "Qdrant filters by active user role" },
];

const agents = ["Router Agent", "Retrieval Agent", "Summarizer Agent", "Critic Agent"];
const pipeline = ["PDF loading", "Recursive chunking", "MiniLM embeddings", "Qdrant retrieval", "Groq grounded answer"];
</script>

<template>
  <div class="page">
    <header class="page-header">
      <div>
        <p class="eyebrow">System overview</p>
        <h1>Enterprise AI operating system</h1>
        <p>
          Document ingestion, role-aware vector retrieval, multi-agent routing, and streamed answers over uploaded enterprise knowledge.
        </p>
      </div>

      <div class="status-pill">Demo ready</div>
    </header>

    <section class="stats-grid">
      <StatCard
        v-for="stat in stats"
        :key="stat.title"
        :title="stat.title"
        :value="stat.value"
        :meta="stat.meta"
      />
    </section>

    <section class="dashboard-grid">
      <article class="panel large">
        <div class="panel-header">
          <h2>RAG Pipeline</h2>
          <span>Live flow</span>
        </div>

        <div class="timeline">
          <div v-for="step in pipeline" :key="step" class="timeline-item">
            <span></span>
            <p>{{ step }}</p>
          </div>
        </div>
      </article>

      <article class="panel">
        <div class="panel-header">
          <h2>Agent Fabric</h2>
          <span>LangGraph</span>
        </div>

        <div class="agent-list">
          <div v-for="agent in agents" :key="agent">
            {{ agent }}
          </div>
        </div>
      </article>
    </section>
  </div>
</template>

<style scoped>
.page {
  height: 100%;
  overflow-y: auto;
  padding-right: 4px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  gap: 24px;
  padding: 28px;
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.18), rgba(15, 23, 42, 1));
}

.eyebrow {
  margin: 0 0 8px;
  color: #38bdf8;
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
}

.page-header h1 {
  margin: 0;
  color: white;
  font-size: 34px;
}

.page-header p:last-child {
  max-width: 760px;
  margin: 12px 0 0;
  color: #cbd5e1;
  line-height: 1.6;
}

.status-pill {
  height: fit-content;
  padding: 10px 14px;
  border-radius: 999px;
  background: rgba(34, 197, 94, 0.14);
  color: #86efac;
  font-weight: 800;
  white-space: nowrap;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin-top: 20px;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 20px;
  margin-top: 20px;
}

.panel {
  min-height: 300px;
  padding: 24px;
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 18px;
  background: #111827;
  color: white;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.panel-header h2 {
  margin: 0;
  font-size: 20px;
}

.panel-header span {
  color: #38bdf8;
  font-size: 13px;
  font-weight: 800;
}

.timeline,
.agent-list {
  display: grid;
  gap: 14px;
  margin-top: 24px;
}

.timeline-item,
.agent-list div {
  padding: 16px;
  border-radius: 14px;
  background: rgba(30, 41, 59, 0.8);
  color: #dbeafe;
}

.timeline-item {
  display: flex;
  align-items: center;
  gap: 12px;
}

.timeline-item span {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: #38bdf8;
}

.timeline-item p {
  margin: 0;
}

@media (max-width: 1100px) {
  .stats-grid,
  .dashboard-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 760px) {
  .page-header,
  .stats-grid,
  .dashboard-grid {
    grid-template-columns: 1fr;
  }

  .page-header {
    flex-direction: column;
  }
}
</style>
