<script setup>
import StatCard from "../components/StatCard.vue";

const stats = [
  { title: "Indexed Documents", value: "128", meta: "RBAC filtered knowledge base" },
  { title: "Chat Sessions", value: "2,304", meta: "Streaming RAG conversations" },
  { title: "Avg Latency", value: "0.7s", meta: "FastAPI plus Redis cache" },
  { title: "Faithfulness", value: "0.87", meta: "Tracked with RAGAS" },
];

const agents = ["Research Agent", "Retrieval Agent", "Compliance Agent", "Critic Agent"];
const pipeline = ["Semantic chunking", "Hybrid retrieval", "Cross-encoder reranking", "Grounded answer"];
</script>

<template>
  <div class="page">
    <header class="page-header">
      <div>
        <p class="eyebrow">Production overview</p>
        <h1>Enterprise AI operating system</h1>
        <p>
          Secure document intelligence, multi-agent workflow automation, and role-aware retrieval over private enterprise knowledge.
        </p>
      </div>

      <div class="status-pill">Production ready</div>
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
          <span>Hybrid search</span>
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