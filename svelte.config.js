import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		// Using adapter-static for GitHub Pages deployment
		adapter: adapter({
			// GitHub Pages serves from the root
			pages: 'build',
			assets: 'build',
			fallback: 'index.html',
			strict: false
		}),
		// Disable trailing slashes for GitHub Pages compatibility
		trailingSlash: 'never'
	}
};

export default config;
