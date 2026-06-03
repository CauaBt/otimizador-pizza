import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  base: '/',
  build: {
    outDir: path.resolve(__dirname, '../backend/dist'),
    emptyOutDir: true
  },
  server: {
    host: '0.0.0.0'
  }
})
