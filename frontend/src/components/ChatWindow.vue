<script setup>
import ChatBubble from "./ChatBubble.vue";

defineProps({
  messages: Array,
});
</script>

<template>
  <div class="chat-window">
    <ChatBubble
      v-for="(msg,index) in messages"
      :key="index"
      :message="msg"
    />
  </div>
</template>