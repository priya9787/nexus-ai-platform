<script setup>
import Sidebar from "../components/Sidebar.vue";
</script>

<template>
  <div class="layout">
    <Sidebar />

    <main class="content">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.layout {
  display: flex;
  min-height: 100vh;
  overflow: hidden;
  background: #020617;
}

.content {
  flex: 1;
  min-width: 0;
  height: 100vh;
  padding: 28px;
  overflow: hidden;
}
</style>