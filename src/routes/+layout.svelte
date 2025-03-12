<script>
  import { onMount } from 'svelte';
  import '../app.css';
  import Navbar from '../components/Navbar.svelte';
  import Footer from '../components/Footer.svelte';
  import { initTheme } from '$lib/stores/theme';
  
  // We no longer need logoSrc as it's now hardcoded in the Navbar component
  
  // Initialize theme on mount
  onMount(() => {
    initTheme();
  });
</script>

<Navbar />

<main>
  <slot />
</main>

<Footer />

<style>
  /* Main content */
  main {
    min-height: calc(100vh - 200px);
  }
</style>
