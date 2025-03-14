<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import '../app.css';
  import Navbar from '../components/Navbar.svelte';
  import Footer from '../components/Footer.svelte';
  import { initTheme } from '../lib/stores/theme.js';
  
  // SEO metadata
  const siteTitle = 'UCLA Robot Intelligence Lab';
  const siteDescription = 'UCLA Robot Intelligence Lab (URIL) focuses on advancing robotics and artificial intelligence through research in robot skill learning and human-robot interaction.';
  const siteUrl = 'https://robot.cs.ucla.edu';
  
  // Generate page-specific metadata
  $: pageTitle = $page.data.title 
    ? `${$page.data.title} | ${siteTitle}` 
    : siteTitle;
    
  $: pageDescription = $page.data.description || siteDescription;
  $: pageUrl = siteUrl + $page.url.pathname;
  $: pageImage = $page.data.image || `${siteUrl}/uril-small.jpg`;
  
  // Function to check if we're on the home page
  $: isHomePage = $page.url.pathname === '/';
  
  // Initialize theme on mount and scroll to top on page load/reload
  onMount(() => {
    initTheme();
    
    // Ensure page starts at the top on reload
    if (typeof window !== 'undefined') {
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'auto' // Use 'auto' instead of 'smooth' for immediate jump on reload
      });
    }
  });
</script>

<svelte:head>
  <!-- Primary Meta Tags -->
  <title>{pageTitle}</title>
  <meta name="title" content={pageTitle}>
  <meta name="description" content={pageDescription}>
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content={pageUrl}>
  <meta property="og:title" content={pageTitle}>
  <meta property="og:description" content={pageDescription}>
  <meta property="og:image" content={pageImage}>
  
  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content={pageUrl}>
  <meta property="twitter:title" content={pageTitle}>
  <meta property="twitter:description" content={pageDescription}>
  <meta property="twitter:image" content={pageImage}>
  
  <!-- Canonical URL -->
  <link rel="canonical" href={pageUrl}>
</svelte:head>

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
