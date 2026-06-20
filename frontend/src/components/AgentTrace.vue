<script setup>
import { computed } from "vue";

const props = defineProps({
  path: Array,
});

const labels = {
  router: "Router",
  retrieval: "Retrieval",
  summarizer: "Summarizer",
  critic: "Critic",
};

const steps = computed(() => {
  return (props.path || []).filter(Boolean);
});
</script>

<template>
  <div class="trace-container">
    <div class="trace-heading">
      <h3>Agent Path</h3>
      <span>{{ steps.length }}</span>
    </div>

    <p
      v-if="!steps.length"
      class="trace-empty"
    >
      Agent path will appear after a response.
    </p>

    <div
      v-for="(item, index) in steps"
      :key="`${item}-${index}`"
      class="trace-item"
    >
      <span class="trace-index">{{ index + 1 }}</span>
      <span>{{ labels[item] || item }}</span>
    </div>
  </div>
</template>

<style scoped>
.trace-container {
  display: grid;
  gap: 12px;
}

.trace-heading {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.trace-heading h3 {
  margin: 0;
  font-size: 20px;
}

.trace-heading span {
  min-width: 30px;
  height: 26px;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: rgba(56, 189, 248, 0.14);
  color: #67e8f9;
  font-size: 13px;
  font-weight: 800;
}

.trace-empty {
  margin: 0;
  color: #94a3b8;
  line-height: 1.5;
}

.trace-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border: 1px solid rgba(148, 163, 184, 0.12);
  border-radius: 8px;
  background: #1e293b;
  color: #e2e8f0;
  font-weight: 700;
}

.trace-index {
  width: 24px;
  height: 24px;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: rgba(34, 197, 94, 0.14);
  color: #86efac;
  font-size: 12px;
}
</style>
