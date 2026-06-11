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

const sessionId = ref(
  crypto.randomUUID()
);

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
    `http://localhost:8000/api/v1/stream?query=${encodeURIComponent(query)}&session_id=${sessionId.value}`,
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

function newChat() {

  eventSource.value?.close();

  eventSource.value = null;

  sessionId.value =
    crypto.randomUUID();

  chatStore.messages = [];

  chatStore.sources = [];

  chatStore.agentPath = [];

  chatStore.setLoading(false);

}
</script>

<template>
  <div class="chat-page">
    <section class="chat-shell">
      <header class="chat-header">
        <div>
          <p class="chat-eyebrow">NexusAI Assistant</p>
          <h2>Chat</h2>
        </div>

        <button class="new-chat-btn" @click="newChat">
          New Chat
        </button>
      </header>

      <div class="conversation">
        <div
          v-if="!chatStore.messages.length"
          class="empty-chat"
        >
          <div class="empty-icon">✦</div>
          <h3>Start a conversation</h3>
          <p>Ask a question and NexusAI will search, reason, and show its sources.</p>
        </div>

        <ChatWindow
          v-else
          :messages="chatStore.messages"
        />

        <TypingIndicator v-if="chatStore.loading" />
      </div>

      <form class="chat-input-bar" @submit.prevent="sendMessage">
        <input
          v-model="input"
          placeholder="Ask anything..."
          :disabled="chatStore.loading"
        />

        <button
          type="submit"
          :disabled="chatStore.loading || !input.trim()"
        >
          Send
        </button>
      </form>
    </section>

    <aside class="sidebar-panel">
      <div class="panel-card">
        <div class="panel-heading">
          <h3>Sources</h3>
          <span>{{ chatStore.sources.length }}</span>
        </div>

        <p
          v-if="!chatStore.sources.length"
          class="panel-empty"
        >
          Sources will appear here after a response.
        </p>

        <CitationCard
          v-for="(src, index) in chatStore.sources"
          :key="index"
          :source="src"
        />
      </div>

      <div class="panel-card">
        <AgentTrace
          :path="chatStore.agentPath"
        />
      </div>
    </aside>
  </div>
</template>
<style>
.chat-page {
  height: calc(100vh - 50px);
  display: grid;
  grid-template-columns: minmax(0, 1fr) 360px;
  gap: 24px;
  padding: 8px 0 0;
  overflow: hidden;
}

.chat-shell,
.panel-card {
  background: #111827;
  border: 1px solid rgba(148, 163, 184, 0.16);
  box-shadow: 0 24px 70px rgba(0, 0, 0, 0.28);
}

.chat-shell {
  min-width: 0;
  display: flex;
  flex-direction: column;
  border-radius: 18px;
  overflow: hidden;
}

.chat-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  padding: 22px 28px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.14);
}

.chat-eyebrow {
  margin: 0 0 4px;
  color: #38bdf8;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0;
  text-transform: uppercase;
}

.chat-header h2 {
  margin: 0;
  color: #f8fafc;
  font-size: 24px;
}

.new-chat-btn {
  border: 1px solid rgba(96, 165, 250, 0.35);
  padding: 10px 14px;
  border-radius: 10px;
  background: rgba(37, 99, 235, 0.18);
  color: #bfdbfe;
  cursor: pointer;
  font-weight: 700;
}

.new-chat-btn:hover {
  background: rgba(37, 99, 235, 0.28);
}

.conversation {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  padding: 28px;
  background:
    radial-gradient(circle at top left, rgba(56, 189, 248, 0.08), transparent 32%),
    #0f172a;
}

.empty-chat {
  height: 100%;
  min-height: 360px;
  display: grid;
  place-content: center;
  justify-items: center;
  text-align: center;
  color: #94a3b8;
}

.empty-icon {
  width: 52px;
  height: 52px;
  display: grid;
  place-items: center;
  margin-bottom: 16px;
  border-radius: 16px;
  background: linear-gradient(135deg, #2563eb, #06b6d4);
  color: white;
  font-size: 28px;
}

.empty-chat h3 {
  margin: 0 0 8px;
  color: #f8fafc;
  font-size: 22px;
}

.empty-chat p {
  max-width: 420px;
  margin: 0;
  line-height: 1.6;
}

.chat-input-bar {
  display: flex;
  gap: 12px;
  padding: 18px;
  background: #111827;
  border-top: 1px solid rgba(148, 163, 184, 0.14);
}

.chat-input-bar input {
  flex: 1;
  min-width: 0;
  height: 48px;
  padding: 0 16px;
  border: 1px solid rgba(148, 163, 184, 0.18);
  border-radius: 12px;
  outline: none;
  background: #1e293b;
  color: #f8fafc;
  font-size: 15px;
}

.chat-input-bar input:focus {
  border-color: rgba(56, 189, 248, 0.75);
  box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.12);
}

.chat-input-bar button {
  height: 48px;
  padding: 0 22px;
  border: none;
  border-radius: 12px;
  background: #2563eb;
  color: white;
  cursor: pointer;
  font-weight: 800;
}

.chat-input-bar button:hover {
  background: #1d4ed8;
}

.chat-input-bar button:disabled,
.chat-input-bar input:disabled {
  opacity: 0.55;
  cursor: not-allowed;
}

.sidebar-panel {
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 24px;
  overflow-y: auto;
}

.panel-card {
  border-radius: 18px;
  padding: 24px;
  color: white;
}

.panel-heading {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.panel-heading h3 {
  margin: 0;
  font-size: 20px;
}

.panel-heading span {
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

.panel-empty {
  margin: 0;
  color: #94a3b8;
  line-height: 1.5;
}

@media (max-width: 1100px) {
  .chat-page {
    grid-template-columns: 1fr;
    overflow-y: auto;
  }

  .sidebar-panel {
    overflow: visible;
  }
}

@media (max-width: 640px) {
  .chat-header,
  .chat-input-bar {
    padding: 16px;
  }

  .chat-header {
    align-items: flex-start;
    flex-direction: column;
  }

  .conversation {
    padding: 18px;
  }

  .chat-input-bar {
    flex-direction: column;
  }

  .chat-input-bar button {
    width: 100%;
  }
}
</style>