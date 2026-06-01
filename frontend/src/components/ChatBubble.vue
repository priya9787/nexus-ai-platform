<script setup>
defineProps({
  message: Object,
});
</script>

<template>
  <div class="p-3 border rounded mb-2">
    <strong>
      {{ message.role }}
    </strong>

    <p>
      {{ message.content }}
    </p>
  </div>
</template>
