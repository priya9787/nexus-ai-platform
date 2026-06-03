<script setup>
defineProps({
  path: Array,
});
</script>

<template>
 <div class="trace-container">
  <h3>Agent Path</h3>

  <div
    v-for="item in path"
    :key="item"
    class="trace-item"
  >
    ↓ {{ item }}
  </div>
</div>
</template>
