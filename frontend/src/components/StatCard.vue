<script setup>
defineProps({
  title: String,
  value: String,
  meta: String,
});
</script>

<template>
  <article class="stat-card">
    <p>{{ title }}</p>
    <h2>{{ value }}</h2>
    <span>{{ meta }}</span>
  </article>
</template>

<style scoped>
.stat-card {
  padding: 22px;
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 16px;
  background: #111827;
  color: white;
}

p {
  margin: 0;
  color: #94a3b8;
  font-size: 13px;
  font-weight: 800;
}

h2 {
  margin: 12px 0 8px;
  font-size: 34px;
}

span {
  color: #64748b;
  font-size: 13px;
  line-height: 1.4;
}
</style>