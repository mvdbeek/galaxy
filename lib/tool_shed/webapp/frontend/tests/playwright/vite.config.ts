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
    server: {
        port: 5199,
        strictPort: true,
    },
})
