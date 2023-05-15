import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vite-plugin
import vuetify from 'vite-plugin-vuetify'

import fs from 'fs';
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
		vue(),
		vuetify({ autoImport: true }),
	],
	server: {
		https: {
			key: fs.readFileSync('./certs/localhost-key.pem'),
			cert: fs.readFileSync('./certs/localhost.pem'),
		},
	},
})
