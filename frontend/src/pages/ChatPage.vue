<script setup>
import { computed, onMounted, ref } from "vue";

import ChatWindow from "../components/ChatWindow.vue";
import CitationCard from "../components/CitationCard.vue";
import AgentTrace from "../components/AgentTrace.vue";
import TypingIndicator from "../components/TypingIndicator.vue";

import { useChatStore } from "../stores/chatStore";

const chatStore = useChatStore();

const CHAT_HISTORY_KEY = "nexus-ai-chat-sessions";

const input = ref("");

const eventSource = ref(null);

const sessionId = ref(
  crypto.randomUUID()
);

const roleOptions = ["admin", "hr", "engineering", "finance"];
const activeRole = ref("admin");

const savedChats = ref([]);

const currentSessionTitle = computed(() => {
  const firstUserMessage = chatStore.messages.find(
    (message) => message.role === "user",
  );

  return firstUserMessage?.content?.slice(0, 48) || "Untitled chat";
});

function cloneData(value) {
  return JSON.parse(JSON.stringify(value));
}

function saveChatHistory() {
  localStorage.setItem(
    CHAT_HISTORY_KEY,
    JSON.stringify(savedChats.value),
  );
}

function loadChatHistory() {
  try {
    const chats = JSON.parse(
      localStorage.getItem(CHAT_HISTORY_KEY) || "[]",
    );

    savedChats.value = chats.map((chat) => ({
      ...chat,
      messages: chat.messages || [],
      sources: chat.sources || [],
      agentPath: chat.agentPath || [],
      role: chat.role || "admin",
    }));
  } catch {
    savedChats.value = [];
  }
}

function persistCurrentSession() {
  if (!chatStore.messages.length) return;

  const existingIndex = savedChats.value.findIndex(
    (chat) => chat.id === sessionId.value,
  );

  const session = {
    id: sessionId.value,
    title: currentSessionTitle.value,
    updatedAt: new Date().toISOString(),
    messages: cloneData(chatStore.messages),
    sources: cloneData(chatStore.sources),
    agentPath: cloneData(chatStore.agentPath),
    role: activeRole.value,
  };

  if (existingIndex >= 0) {
    savedChats.value.splice(existingIndex, 1, session);
  } else {
    savedChats.value.unshift(session);
  }

  savedChats.value.sort(
    (a, b) => new Date(b.updatedAt) - new Date(a.updatedAt),
  );

  savedChats.value = savedChats.value.slice(0, 10);

  saveChatHistory();
}

function loadSession(chat) {
  eventSource.value?.close();
  eventSource.value = null;

  sessionId.value = chat.id;
  activeRole.value = chat.role || "admin";

  chatStore.messages = cloneData(chat.messages || []);
  chatStore.sources = cloneData(chat.sources || []);
  chatStore.agentPath = cloneData(chat.agentPath || []);
  chatStore.setLoading(false);
}

function formatChatTime(value) {
  return new Intl.DateTimeFormat(undefined, {
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
  }).format(new Date(value));
}

onMounted(() => {
  loadChatHistory();
});

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
  chatStore.setSources([]);
  chatStore.setPath([]);

  chatStore.addMessage({
    role: "assistant",
    content: "",
  });

  const assistantIndex =
    chatStore.messages.length - 1;

  eventSource.value = new EventSource(
    `/api/v1/stream?query=${encodeURIComponent(query)}&session_id=${sessionId.value}&role=${activeRole.value}`,
  );

  eventSource.value.addEventListener(
    "message",
    (event) => {
      chatStore.messages[
        assistantIndex
      ].content += event.data;

      persistCurrentSession();
    },
  );

  eventSource.value.addEventListener(
    "sources",
    (event) => {
      try {
        chatStore.setSources(
          JSON.parse(event.data),
        );

        persistCurrentSession();
      } catch (error) {
        console.error("Unable to parse sources event", error);
      }
    },
  );

  eventSource.value.addEventListener(
    "path",
    (event) => {
      try {
        chatStore.setPath(
          JSON.parse(event.data),
        );

        persistCurrentSession();
      } catch (error) {
        console.error("Unable to parse path event", error);
      }
    },
  );

  eventSource.value.addEventListener(
    "done",
    () => {
      chatStore.setLoading(false);

      eventSource.value?.close();

      eventSource.value = null;

      persistCurrentSession();
    },
  );

  eventSource.value.onerror = () => {
    chatStore.setLoading(false);

    eventSource.value?.close();

    eventSource.value = null;
  };

  input.value = "";

  persistCurrentSession();
}

function newChat() {

  persistCurrentSession();

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

      <div class="role-bar">
        <span>Active role</span>
        <select
          v-model="activeRole"
          :disabled="chatStore.loading"
        >
          <option
            v-for="role in roleOptions"
            :key="role"
            :value="role"
          >
            {{ role }}
          </option>
        </select>
      </div>

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
          <h3>Recent Chats</h3>
          <span>{{ savedChats.length }}</span>
        </div>

        <p
          v-if="!savedChats.length"
          class="panel-empty"
        >
          Previous conversations will appear here.
        </p>

        <button
          v-for="chat in savedChats"
          :key="chat.id"
          type="button"
          class="session-item"
          :class="{ active: chat.id === sessionId }"
          @click="loadSession(chat)"
        >
          <span>{{ chat.title }}</span>
          <small>
            {{ formatChatTime(chat.updatedAt) }}
            · {{ chat.role || "admin" }}
            · {{ chat.sources?.length || 0 }} sources
            · {{ chat.agentPath?.length || 0 }} steps
          </small>
        </button>
      </div>

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

.role-bar {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;
  padding: 12px 28px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.14);
  background: #0f172a;
}

.role-bar span {
  color: #94a3b8;
  font-size: 13px;
  font-weight: 800;
}

.role-bar select {
  min-width: 150px;
  height: 36px;
  border: 1px solid rgba(148, 163, 184, 0.18);
  border-radius: 8px;
  background: #1e293b;
  color: #f8fafc;
  padding: 0 10px;
  font-weight: 800;
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

.session-item {
  width: 100%;
  display: grid;
  gap: 6px;
  margin-top: 10px;
  padding: 12px;
  border: 1px solid rgba(148, 163, 184, 0.12);
  border-radius: 8px;
  background: #1e293b;
  color: #f8fafc;
  text-align: left;
  cursor: pointer;
}

.session-item:hover,
.session-item.active {
  border-color: rgba(56, 189, 248, 0.55);
  background: rgba(37, 99, 235, 0.22);
}

.session-item span {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-weight: 800;
}

.session-item small {
  color: #94a3b8;
  font-size: 12px;
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
