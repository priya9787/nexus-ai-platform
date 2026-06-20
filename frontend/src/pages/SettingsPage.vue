<script setup>
const security = [
  ["CORS", "Enabled for local frontend"],
  ["Grounding", "Answers restricted to retrieved context"],
  ["Upload validation", "Basic FastAPI file handling"],
  ["RBAC / PII controls", "Planned"],
];

const modelConfig = [
  ["Model", "Llama 3.3 70B via Groq"],
  ["Embeddings", "all-MiniLM-L6-v2"],
  ["Retriever", "Qdrant vector search"],
  ["Reranker", "Planned"],
  ["Temperature", "0.0"],
  ["Top K", "5"],
  ["Chunking", "500 size / 100 overlap"],
];
</script>

<template>
  <div class="page">
    <header class="page-header">
      <p class="eyebrow">System configuration</p>
      <h1>Settings</h1>
      <p>Review model, retrieval, security, and observability controls for the AI platform.</p>
    </header>

    <section class="settings-grid">
      <article class="panel">
        <h2>Model and Retrieval</h2>

        <div class="config-list">
          <div v-for="[label, value] in modelConfig" :key="label">
            <span>{{ label }}</span>
            <strong>{{ value }}</strong>
          </div>
        </div>
      </article>

      <article class="panel">
        <h2>Enterprise Security</h2>

        <div class="security-list">
          <div v-for="[label, value] in security" :key="label">
            <span>{{ label }}</span>
            <strong>{{ value }}</strong>
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

.settings-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 20px;
  margin-top: 20px;
}

.panel {
  padding: 24px;
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 18px;
  background: #111827;
  color: white;
}

.panel h2 {
  margin: 0 0 20px;
}

.config-list,
.security-list {
  display: grid;
  gap: 12px;
}

.config-list div,
.security-list div {
  padding: 14px;
  border-radius: 12px;
  background: #1e293b;
}

.config-list div,
.security-list div {
  display: flex;
  justify-content: space-between;
  gap: 16px;
}

.config-list span,
.security-list span {
  color: #94a3b8;
}

.config-list strong,
.security-list strong {
  text-align: right;
}

@media (max-width: 900px) {
  .settings-grid {
    grid-template-columns: 1fr;
  }
}
</style>
