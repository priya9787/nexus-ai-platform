<script setup>
import ChatBubble from "./ChatBubble.vue";

defineProps({
  messages: Array,
});
</script>

<template>
  <div>
    <ChatBubble v-for="(msg, index) in messages" :key="index" :message="msg" />
  </div>
</template>
