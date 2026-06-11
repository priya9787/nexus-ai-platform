<script setup>
import UploadCard from "../components/UploadCard.vue";

const collections = [
  "HR policies",
  "Security playbooks",
  "Architecture docs",
  "Customer contracts",
];
</script>

<template>
  <div class="page">
    <header class="page-header">
      <p class="eyebrow">Knowledge ingestion</p>
      <h1>Documents</h1>
      <p>Upload, chunk, embed, and index enterprise documents for secure retrieval.</p>
    </header>

    <section class="documents-grid">
      <UploadCard />

      <article class="panel">
        <h2>Knowledge Collections</h2>

        <div class="collection-list">
          <div v-for="item in collections" :key="item">
            <span>{{ item }}</span>
            <strong>Indexed</strong>
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

.page-header {
  margin-bottom: 20px;
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

.documents-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 20px;
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

.collection-list {
  display: grid;
  gap: 12px;
}

.collection-list div {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  padding: 14px;
  border-radius: 12px;
  background: #1e293b;
}

.collection-list strong {
  color: #86efac;
  font-size: 13px;
}

@media (max-width: 900px) {
  .documents-grid {
    grid-template-columns: 1fr;
  }
}
</style>