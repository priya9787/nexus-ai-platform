<script setup>
import { ref } from "vue";

import ChatWindow from "../components/ChatWindow.vue";
import CitationCard from "../components/CitationCard.vue";
import AgentTrace from "../components/AgentTrace.vue";
import TypingIndicator from "../components/TypingIndicator.vue";

import { useChatStore } from "../stores/chatStore";

const chatStore = useChatStore();

const input = ref("");

const eventSource = ref(null);

const sessionId = "test-session";

function sendMessage() {
  if (!input.value.trim() || chatStore.loading) return;

  /*
    IMPORTANT:
    close old SSE connection first
  */
  if (eventSource.value) {
    eventSource.value.close();

    eventSource.value = null;
  }

  const query = input.value;

  chatStore.addMessage({
    role: "user",
    content: query,
  });

  chatStore.setLoading(true);

  chatStore.addMessage({
    role: "assistant",
    content: "",
  });

  const assistantIndex =
    chatStore.messages.length - 1;

  eventSource.value = new EventSource(
    `http://localhost:8000/api/v1/stream?query=${encodeURIComponent(query)}&session_id=${sessionId}`,
  );

  eventSource.value.addEventListener(
    "message",
    (event) => {
      chatStore.messages[
        assistantIndex
      ].content += event.data;
    },
  );

  eventSource.value.addEventListener(
    "sources",
    (event) => {
      try {
        chatStore.setSources(
          JSON.parse(
            event.data.replace(/'/g, '"'),
          ),
        );
      } catch {}
    },
  );

  eventSource.value.addEventListener(
    "path",
    (event) => {
      try {
        chatStore.setPath(
          JSON.parse(
            event.data.replace(/'/g, '"'),
          ),
        );
      } catch {}
    },
  );

  eventSource.value.addEventListener(
    "done",
    () => {
      chatStore.setLoading(false);

      eventSource.value?.close();

      eventSource.value = null;
    },
  );

  eventSource.value.onerror = () => {
    chatStore.setLoading(false);

    eventSource.value?.close();

    eventSource.value = null;
  };

  input.value = "";
}
</script>

<template>
  <div class="app-container">
    <h1 class="app-title">
      NexusAI
    </h1>

    <ChatWindow
      :messages="chatStore.messages"
    />

    <TypingIndicator
      v-if="chatStore.loading"
    />

    <div class="input-container">
      <input
        v-model="input"
        class="chat-input"
        placeholder="Ask something..."
        @keyup.enter="sendMessage"
      />

      <button
        class="send-btn"
        :disabled="chatStore.loading"
        @click="sendMessage"
      >
        Send
      </button>
    </div>

    <div class="sources-section">
      <h2>Sources</h2>

      <CitationCard
        v-for="(src,index) in chatStore.sources"
        :key="index"
        :source="src"
      />
    </div>

    <AgentTrace
      :path="chatStore.agentPath"
    />
  </div>
</template>