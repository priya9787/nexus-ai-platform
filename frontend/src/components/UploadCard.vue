<template>
  <article class="upload-card">
    <div class="drop-zone">
      <div class="upload-icon">UP</div>
      <h2>Upload enterprise documents</h2>
      <p>PDF, DOCX, TXT, and policy files are prepared for chunking, embedding, and role-aware retrieval.</p>

      <label>
        Select files
        <input type="file" multiple />
      </label>
    </div>
  </article>
</template>

<style scoped>
.upload-card {
  padding: 24px;
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 18px;
  background: #111827;
  color: white;
}

.drop-zone {
  min-height: 320px;
  display: grid;
  place-items: center;
  align-content: center;
  text-align: center;
  padding: 32px;
  border: 1px dashed rgba(148, 163, 184, 0.35);
  border-radius: 16px;
  background: rgba(15, 23, 42, 0.7);
}

.upload-icon {
  width: 54px;
  height: 54px;
  display: grid;
  place-items: center;
  margin-bottom: 16px;
  border-radius: 16px;
  background: rgba(37, 99, 235, 0.18);
  color: #93c5fd;
  font-weight: 900;
}

h2 {
  margin: 0;
}

p {
  max-width: 460px;
  margin: 10px 0 20px;
  color: #94a3b8;
  line-height: 1.6;
}

label {
  padding: 12px 16px;
  border-radius: 12px;
  background: #2563eb;
  color: white;
  cursor: pointer;
  font-weight: 800;
}

input {
  display: none;
}
</style>