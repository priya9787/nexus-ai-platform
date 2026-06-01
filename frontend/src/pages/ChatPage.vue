<script setup>
import { ref } from "vue";

import ChatWindow from "../components/ChatWindow.vue";

import CitationCard from "../components/CitationCard.vue";

import AgentTrace from "../components/AgentTrace.vue";

import TypingIndicator from "../components/TypingIndicator.vue";

import { useChatStore } from "../stores/chatStore";

const chatStore = useChatStore();

const input = ref("");

const sessionId = "test-session";

function sendMessage() {
  chatStore.addMessage({
    role: "user",

    content: input.value,
  });

  chatStore.setLoading(true);

  chatStore.addMessage({
    role: "assistant",

    content: "",
  });

  const assistantIndex = chatStore.messages.length - 1;

  const source = new EventSource(
    `http://localhost:8000/api/v1/stream?query=${encodeURIComponent(input.value)}&session_id=${sessionId}`,
  );

  source.addEventListener(
    "message",

    (event) => {
      chatStore.messages[assistantIndex].content += event.data;
    },
  );

  source.addEventListener(
    "sources",

    (event) => {
      chatStore.setSources(JSON.parse(event.data.replace(/'/g, '"')));
    },
  );

  source.addEventListener(
    "path",

    (event) => {
      chatStore.setPath(JSON.parse(event.data.replace(/'/g, '"')));
    },
  );

  source.addEventListener(
    "done",

    () => {
      chatStore.setLoading(false);

      source.close();
    },
  );

  input.value = "";
}
</script>

<template>
  <div class="p-8">
    <h1>NexusAI</h1>

    <ChatWindow :messages="chatStore.messages" />

    <TypingIndicator v-if="chatStore.loading" />

    <input v-model="input" class="border p-2" />

    <button @click="sendMessage">Send</button>

    <h2>Sources</h2>

    <CitationCard
      v-for="(src, index) in chatStore.sources"
      :key="index"
      :source="src"
    />

    <AgentTrace :path="chatStore.agentPath" />
  </div>
</template>
