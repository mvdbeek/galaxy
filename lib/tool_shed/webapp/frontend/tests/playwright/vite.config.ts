import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"
import { resolve } from "path"

export default defineConfig({
    plugins: [vue()],
    root: __dirname,
    resolve: {
        alias: {
            "@": resolve(__dirname, "../../src"),
        },
    },
    build: {
        rollupOptions: {
            input: {
                "test-harness": resolve(__dirname, "test-harness.html"),
                "schema-viewer": resolve(__dirname, "schema-viewer.html"),
            },
        },
    },
    server: {
        port: 5199,
        strictPort: true,
    },
})
