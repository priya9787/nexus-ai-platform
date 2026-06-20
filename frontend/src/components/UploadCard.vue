<script setup>
import { ref } from "vue";

const uploadStatus = ref("");
const uploadError = ref("");
const isUploading = ref(false);
const roleOptions = ["admin", "hr", "engineering", "finance"];
const allowedRoles = ref(["admin"]);

const uploadFiles = async (event) => {
  const files = Array.from(event.target.files || []);

  if (!files.length || !allowedRoles.value.length) {
    uploadError.value = "Select at least one role before uploading.";
    return;
  }

  uploadStatus.value = "";
  uploadError.value = "";
  isUploading.value = true;

  try {
    for (const file of files) {
      const formData = new FormData();
      formData.append("file", file);
      formData.append("allowed_roles", allowedRoles.value.join(","));

      const response = await fetch("/api/v1/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(errorText || `Upload failed for ${file.name}`);
      }
    }

    uploadStatus.value = `${files.length} file${files.length === 1 ? "" : "s"} uploaded and processed.`;
  } catch (error) {
    uploadError.value = error.message || "Upload failed. Please try again.";
  } finally {
    isUploading.value = false;
    event.target.value = "";
  }
};
</script>

<template>
  <article class="upload-card">
    <div class="drop-zone">
      <div class="upload-icon">UP</div>
      <h2>Upload enterprise documents</h2>
      <p>PDF files are prepared for chunking, embedding, and role-aware retrieval.</p>

      <div class="role-picker">
        <span>Accessible to</span>

        <label
          v-for="role in roleOptions"
          :key="role"
          class="role-option"
        >
          <input
            v-model="allowedRoles"
            type="checkbox"
            :value="role"
            :disabled="isUploading"
          />
          {{ role }}
        </label>
      </div>

      <label :class="{ disabled: isUploading || !allowedRoles.length }">
        {{ isUploading ? "Uploading..." : "Select files" }}
        <input
          type="file"
          multiple
          :disabled="isUploading || !allowedRoles.length"
          @change="uploadFiles"
        />
      </label>

      <p v-if="uploadStatus" class="status success">{{ uploadStatus }}</p>
      <p v-if="uploadError" class="status error">{{ uploadError }}</p>
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

label.disabled {
  cursor: wait;
  opacity: 0.75;
}

input {
  display: none;
}

.role-picker {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin: 0 0 20px;
}

.role-picker span {
  width: 100%;
  color: #cbd5e1;
  font-size: 13px;
  font-weight: 800;
}

.role-option {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 10px;
  border: 1px solid rgba(148, 163, 184, 0.18);
  border-radius: 8px;
  background: #1e293b;
  color: #dbeafe;
  font-size: 13px;
}

.role-option input {
  display: inline-block;
}

.status {
  margin: 16px 0 0;
  font-size: 14px;
}

.success {
  color: #86efac;
}

.error {
  color: #fca5a5;
}
</style>
