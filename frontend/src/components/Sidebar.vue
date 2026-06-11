<script setup>
const items = [
  { name: "Dashboard", path: "/", icon: "DA" },
  { name: "Documents", path: "/documents", icon: "DO" },
  { name: "Chat", path: "/chat", icon: "CH" },
  { name: "Monitoring", path: "/monitoring", icon: "MO" },
  { name: "Settings", path: "/settings", icon: "SE" },
];
</script>

<template>
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-mark">N</div>
      <div>
        <h1>NexusAI</h1>
        <p>Enterprise AI OS</p>
      </div>
    </div>

    <nav class="nav-list">
      <RouterLink
        v-for="item in items"
        :key="item.path"
        :to="item.path"
        class="nav-link"
      >
        <span>{{ item.icon }}</span>
        {{ item.name }}
      </RouterLink>
    </nav>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 280px;
  height: 100vh;
  padding: 24px;
  background: #0f172a;
  border-right: 1px solid rgba(148, 163, 184, 0.14);
}

.brand {
  display: flex;
  gap: 14px;
  align-items: center;
  margin-bottom: 36px;
}

.brand-mark {
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  background: linear-gradient(135deg, #2563eb, #06b6d4);
  color: white;
  font-weight: 900;
}

.brand h1 {
  margin: 0;
  color: #f8fafc;
  font-size: 24px;
}

.brand p {
  margin: 2px 0 0;
  color: #94a3b8;
  font-size: 12px;
}

.nav-list {
  display: grid;
  gap: 8px;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 13px 14px;
  border-radius: 12px;
  color: #94a3b8;
  text-decoration: none;
  font-weight: 700;
}

.nav-link span {
  width: 30px;
  height: 30px;
  display: grid;
  place-items: center;
  border-radius: 9px;
  background: rgba(148, 163, 184, 0.1);
  color: #cbd5e1;
  font-size: 11px;
}

.nav-link:hover,
.nav-link.router-link-active {
  background: rgba(37, 99, 235, 0.16);
  color: #f8fafc;
}

.nav-link.router-link-active span {
  background: #2563eb;
  color: white;
}
</style>