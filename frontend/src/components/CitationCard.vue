<script setup>
import { computed } from "vue";

const props = defineProps({
  source: Object,
});

const title = computed(() => {
  return props.source?.source?.split(/[\\/]/).pop() || "Uploaded document";
});

const page = computed(() => {
  const rawPage = props.source?.page;
  return Number.isInteger(rawPage) ? rawPage + 1 : rawPage;
});
</script>

<template>
  <article class="source-card">
    <div class="source-title">
      {{ title }}
    </div>

    <div class="source-meta">
      <span v-if="page">Page {{ page }}</span>
      <span v-if="source?.total_pages">{{ source.total_pages }} pages</span>
    </div>
  </article>
</template>

<style scoped>
.source-card {
  display: grid;
  gap: 8px;
  padding: 14px;
  margin-top: 10px;
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 8px;
  background: #1e293b;
}

.source-title {
  color: #f8fafc;
  font-size: 14px;
  font-weight: 800;
  overflow-wrap: anywhere;
}

.source-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  color: #94a3b8;
  font-size: 12px;
}

.source-meta span {
  padding: 4px 8px;
  border-radius: 999px;
  background: rgba(15, 23, 42, 0.75);
}
</style>
