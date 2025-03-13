<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import '../app.css';
  import Navbar from '../components/Navbar.svelte';
  import Footer from '../components/Footer.svelte';
  import { initTheme } from '../lib/stores/theme.js';
  
  // Function to check if we're on the home page
  $: isHomePage = $page.url.pathname === '/';
  
  // Initialize theme on mount
  onMount(() => {
    initTheme();
  });
</script>

<Navbar />

<main>
  <slot />
</main>

{#if !isHomePage}
  <Footer />
{/if}

<style>
  /* Main content */
  main {
    min-height: calc(100vh - 200px);
  }
</style>
