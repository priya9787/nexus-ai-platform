<script setup>
defineProps({
  message: Object,
});
</script>

<template>
  <div
    class="chat-row"
    :class="message.role"
  >
    <div
      class="chat-bubble"
      :class="message.role"
    >
      <div class="role">
        {{ message.role }}
      </div>

      <div class="message-text">
        {{ message.content }}
      </div>
    </div>
  </div>
</template>