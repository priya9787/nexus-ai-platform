import { defineStore } from "pinia";

export const useChatStore = defineStore("chat", {
  state: () => ({
    messages: [],

    sources: [],

    agentPath: [],

    loading: false,
  }),

  actions: {
    addMessage(msg) {
      this.messages.push(msg);
    },

    setSources(data) {
      this.sources = data;
    },

    setPath(data) {
      this.agentPath = data;
    },

    setLoading(value) {
      this.loading = value;
    },
  },
});
