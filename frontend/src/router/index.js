import { createRouter, createWebHistory } from "vue-router";

import DashboardPage from "../pages/DashboardPage.vue";
import DocumentsPage from "../pages/DocumentsPage.vue";
import ChatPage from "../pages/ChatPage.vue";
import MonitoringPage from "../pages/MonitoringPage.vue";
import SettingsPage from "../pages/SettingsPage.vue";

const routes = [
  {
    path: "/",
    component: DashboardPage,
  },

  {
    path: "/documents",
    component: DocumentsPage,
  },

  {
    path: "/chat",
    component: ChatPage,
  },

  {
    path: "/monitoring",
    component: MonitoringPage,
  },

  {
    path: "/settings",
    component: SettingsPage,
  },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});