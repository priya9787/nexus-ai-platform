<script setup>
defineProps({
  path: Array,
});
</script>

<template>
  <div>
    <h3>Agent Path</h3>

    <div v-for="item in path" :key="item">
      ↓

      {{ item }}
    </div>
  </div>
</template>
