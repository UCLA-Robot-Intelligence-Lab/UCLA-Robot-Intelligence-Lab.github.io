<script>
  import { theme, toggleTheme } from '$lib/stores/theme';
  
  // Icons for light/dark mode
  const sunIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`;
  
  const moonIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`;
</script>

<button 
  class="theme-toggle" 
  on:click={toggleTheme} 
  aria-label={$theme === 'light' ? 'Switch to dark mode' : 'Switch to light mode'}
>
  {#if $theme === 'light'}
    {@html moonIcon}
  {:else}
    {@html sunIcon}
  {/if}
</button>

<style>
  .theme-toggle {
    background: none;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    color: var(--nav-text);
    background-color: var(--nav-active);
    transition: all 0.3s ease;
    padding: 0;
  }

  .theme-toggle:hover {
    transform: scale(1.1);
    background-color: rgba(255, 255, 255, 0.2);
  }

  :global(.dark-mode) .theme-toggle {
    background-color: rgba(255, 255, 255, 0.15);
  }

  :global(.dark-mode) .theme-toggle:hover {
    background-color: rgba(255, 255, 255, 0.25);
  }
</style>
