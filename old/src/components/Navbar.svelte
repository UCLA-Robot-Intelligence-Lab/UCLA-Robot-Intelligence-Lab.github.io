<script lang="ts">
  import { page } from "$app/stores";
  // import ThemeToggle from "./ThemeToggle.svelte";
  import { onMount } from "svelte";
  import { tweened } from "svelte/motion";
  import { cubicOut } from "svelte/easing";
  import { slide, fly } from "svelte/transition";
  import { quintOut } from "svelte/easing";
  import { theme } from "../lib/stores/theme.js";
  import { browser } from "$app/environment";

  // Import icons this way instead
  import UsersIcon from "lucide-svelte/icons/users";
  import FileTextIcon from "lucide-svelte/icons/file-text";
  import BookIcon from "lucide-svelte/icons/book";
  import CameraIcon from "lucide-svelte/icons/camera";
  import MailIcon from "lucide-svelte/icons/mail";
  import GithubIcon from "lucide-svelte/icons/github";

  // Dynamic logo based on theme
  $: logoSrc = currentTheme === "dark" ? "/Yellow Outline Logo.png" : "/original-uril.png";

  // Get the current theme for conditional styling
  // Default to system preference or 'light' during SSR
  let currentTheme = (browser && localStorage.getItem("theme")) || "light";
  theme.subscribe((value: string) => {
    currentTheme = value;
  });

  // Helper function to get the appropriate gradient based on theme
  function getActiveGradient(isLightMode: boolean): string {
    return isLightMode
      ? "radial-gradient(circle, rgba(49,64,98,0.25) 0%, rgba(49,64,98,0.15) 50%, rgba(49,64,98,0) 100%)"
      : "radial-gradient(circle, rgba(252,215,41,0.25) 0%, rgba(252,215,41,0.15) 50%, rgba(252,215,41,0) 100%)";
  }

  // Helper function to get the appropriate active icon color based on theme
  function getActiveIconColor(isLightMode: boolean): string {
    return isLightMode ? "var(--ucla-light-blue)" : "var(--ucla-yellow)";
  }

  // Force theme sync when page changes
  $: {
    $page.url.pathname; // Track changes to pathname
    if (browser) {
      // Re-sync the theme on page changes
      const savedTheme = localStorage.getItem("theme") || "light";
      if (savedTheme !== currentTheme) {
        currentTheme = savedTheme;
      }
    }
  }

  // Navigation links with their properties
  const navLinks: NavLink[] = [
    {
      name: "People",
      href: "/people",
      id: "people",
      icon: UsersIcon,
    },
    {
      name: "Publications",
      href: "/publications",
      id: "publications",
      icon: BookIcon,
    },
    {
      name: "Contact",
      href: "/contact",
      id: "contact",
      icon: MailIcon,
    },
  ];

  // Define the interface for our navigation links
  interface NavLink {
    name: string;
    href: string;
    id: string;
    icon: any; // Using 'any' for Svelte component type
  }

  // Manage hover states for each nav item
  let hoveredItem: string | null = null;

  // Helper to check if a link is active
  const isActive = (link: NavLink): boolean => {
    if (!link || !link.href) return false;
    return link.href === "/"
      ? $page.url.pathname === "/"
      : $page.url.pathname.startsWith(link.href);
  };

  // Keyboard navigation support
  function handleKeyDown(event: KeyboardEvent, link: NavLink): void {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      window.location.href = link.href;
    }
  }

  // Define helper functions for hover state
  function setHoveredItem(id: string): void {
    hoveredItem = id;
  }

  function clearHoveredItem(): void {
    hoveredItem = null;
  }

  let mounted = false;
  let mobileMenuOpen = false;

  // Toggle mobile menu
  function toggleMobileMenu() {
    mobileMenuOpen = !mobileMenuOpen;
    if (browser) {
      // Prevent scrolling when menu is open
      if (mobileMenuOpen) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = '';
      }
    }
  }

  // Close mobile menu when clicking a link
  function closeMobileMenu() {
    mobileMenuOpen = false;
    if (browser) {
      document.body.style.overflow = '';
    }
  }

  onMount(() => {
    mounted = true;
    
    // Close menu on window resize if open
    const handleResize = () => {
      if (window.innerWidth > 768 && mobileMenuOpen) {
        closeMobileMenu();
      }
    };
    
    window.addEventListener('resize', handleResize);
    
    return () => {
      window.removeEventListener('resize', handleResize);
      document.body.style.overflow = '';
    };
  });
</script>

<header>
  <div class="container">
    <div class="navbar-container">
      <div class="logo-container">
        <a 
          href="/" 
          aria-label="Go to home page"
        >
          <img
            src={logoSrc}
            alt="UCLA Robot Intelligence Lab Logo"
            class="logo"
          />
        </a>
      </div>

      <!-- Desktop Navigation -->
      <nav class="modern-nav desktop-nav">
        <ul class="nav-items-container">
          {#each navLinks as link, i}
              <li>
                <div
                  class="menu-item-wrapper"
                  on:mouseenter={() => setHoveredItem(link.id)}
                  on:mouseleave={clearHoveredItem}
                  on:keydown={(e) => handleKeyDown(e, link)}
                  role="button"
                  tabindex="0"
                  aria-label={`${link.name} navigation item`}
                >
                  <a
                    href={link.href}
                    class="nav-item-front"
                    class:active={isActive(link)}
                  >
                    <svelte:component
                      this={link.icon}
                      size="20"
                      color={isActive(link)
                        ? currentTheme === "light"
                          ? "var(--ucla-dark-blue)"
                          : "var(--ucla-yellow)"
                        : hoveredItem === link.id
                          ? currentTheme === "light"
                            ? "var(--ucla-light-blue)"
                            : "var(--ucla-yellow)"
                          : "currentColor"}
                      class="nav-icon {isActive(link)
                        ? 'active-icon'
                        : ''} {currentTheme === 'dark'
                        ? 'dark-theme-icon'
                        : 'light-theme-icon'}"
                    />
                    <span
                      style="font-weight: {isActive(link)
                        ? '700'
                        : 'normal'}; color: {isActive(link)
                        ? currentTheme === 'light'
                          ? 'var(--ucla-dark-blue)'
                          : 'var(--ucla-yellow)'
                        : hoveredItem === link.id
                          ? currentTheme === 'light'
                            ? 'var(--ucla-light-blue)'
                            : 'var(--ucla-yellow)'
                          : 'inherit'};">{link.name}</span
                    >
                  </a>
                </div>
              </li>
            {/each}
          </ul>
      </nav>

      <!-- Desktop Social Icons -->
      <div class="social-icons desktop-only">
        <a href="https://github.com/UCLA-Robot-Intelligence-Lab" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="GitHub">
          <GithubIcon size={24} />
        </a>
        <a href="/pictures" class="social-icon" aria-label="Photos">
          <CameraIcon size={24} />
        </a>
      </div>

      <!-- Mobile Hamburger Button -->
      <button 
        class="hamburger-button mobile-only"
        on:click={toggleMobileMenu}
        aria-label={mobileMenuOpen ? "Close menu" : "Open menu"}
        aria-expanded={mobileMenuOpen}
      >
        <span class="hamburger-line" class:open={mobileMenuOpen}></span>
        <span class="hamburger-line" class:open={mobileMenuOpen}></span>
        <span class="hamburger-line" class:open={mobileMenuOpen}></span>
      </button>
    </div>
  </div>
</header>

<!-- Mobile Menu Overlay -->
{#if mobileMenuOpen}
  <div 
    class="mobile-menu-overlay"
    transition:fly={{ y: -20, duration: 300 }}
    on:click={closeMobileMenu}
    on:keydown={(e) => e.key === 'Escape' && closeMobileMenu()}
    role="presentation"
  >
    <nav class="mobile-nav" on:click|stopPropagation on:keydown|stopPropagation role="presentation">
      <ul>
        {#each navLinks as link}
          <li>
            <a
              href={link.href}
              class="mobile-nav-link"
              class:active={isActive(link)}
              on:click={closeMobileMenu}
            >
              <svelte:component
                this={link.icon}
                size="24"
                color={isActive(link)
                  ? currentTheme === "light"
                    ? "var(--ucla-light-blue)"
                    : "var(--ucla-yellow)"
                  : "currentColor"}
              />
              <span>{link.name}</span>
            </a>
          </li>
        {/each}
        
        <!-- Social links in mobile menu -->
        <li class="mobile-menu-divider"></li>
        <li>
          <a 
            href="https://github.com/UCLA-Robot-Intelligence-Lab" 
            target="_blank" 
            rel="noopener noreferrer"
            class="mobile-nav-link"
            on:click={closeMobileMenu}
          >
            <GithubIcon size={24} />
            <span>GitHub</span>
          </a>
        </li>
        <li>
          <a 
            href="/pictures"
            class="mobile-nav-link"
            on:click={closeMobileMenu}
          >
            <CameraIcon size={24} />
            <span>Photos</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
{/if}

<style>
  header {
    background-color: var(--nav-bg);
    color: var(--nav-text);
    padding: 0;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 100;
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    transform: translateZ(0);
    will-change: transform;
  }

  .container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
  }

  @media (max-width: 768px) {
    .container {
      padding: 0 12px;
    }
  }

  @media (max-width: 480px) {
    .container {
      padding: 0 8px;
    }
  }

  .navbar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0;
  }

  .logo-container {
    display: flex;
    align-items: center;
    padding: 8px;
  }

  .logo {
    height: 60px;
  }

  @media (max-width: 768px) {
    .logo {
      height: 50px;
    }
  }

  /* .theme-toggle-container {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    z-index: 5;
    grid-column: 3;
    justify-self: end;
  } */

  /* Modern navigation styling */
  .modern-nav {
    position: relative;
    display: flex;
    justify-content: flex-end;
    padding: 8px;
    overflow: visible; /* Allow glow to extend beyond boundaries */
    min-width: 0; /* Allow flex container to shrink below content size */
    width: 100%;
  }

  .modern-nav ul {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 2px 10px; /* Reduced vertical padding */
    justify-content: center;
    gap: 8px;
    position: relative;
    z-index: 2;
    flex-wrap: nowrap; /* Prevent wrapping to keep horizontal layout */
  }

  .modern-nav li {
    margin: 0;
    list-style: none;
  }

  .menu-item-wrapper {
    position: relative;
    display: block;
    perspective: 600px;
    border-radius: 10px;
    overflow: visible;
    cursor: pointer;
    margin: 2px;
    min-height: 36px;
    min-width: 110px;
  }

  .nav-item-front {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: 10px;
    text-decoration: none;
    color: var(--nav-text);
    font-weight: 500;
    transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    backface-visibility: hidden;
    position: relative;
    z-index: 1;
    width: 100%;
    box-sizing: border-box;
    white-space: nowrap;
    font-size: 0.95rem;
  }

  .nav-item-front.active {
    font-weight: 600;
    color: var(--active-nav-color);
    text-shadow: var(--active-nav-shadow);
  }

  /* Define active color based on theme */
  :global(:root) {
    --active-nav-color: var(--ucla-dark-blue);
    --active-nav-shadow: none; /* No text shadow in light mode */
  }

  :global(.dark-mode) {
    --active-nav-color: var(--ucla-yellow);
    --active-nav-shadow: 0 0 5px rgba(252, 215, 41, 0.3); /* Keep glow in dark mode */
  }

  /* Hide mobile elements on desktop */
  .mobile-only {
    display: none;
  }

  .desktop-only {
    display: flex;
  }

  /* Hamburger button */
  .hamburger-button {
    display: none;
    flex-direction: column;
    justify-content: space-around;
    width: 32px;
    height: 32px;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 4px;
    z-index: 101;
  }

  .hamburger-line {
    width: 24px;
    height: 2px;
    background-color: var(--nav-text);
    border-radius: 2px;
    transition: all 0.3s ease;
    transform-origin: center;
  }

  .hamburger-line.open:nth-child(1) {
    transform: translateY(7px) rotate(45deg);
  }

  .hamburger-line.open:nth-child(2) {
    opacity: 0;
  }

  .hamburger-line.open:nth-child(3) {
    transform: translateY(-7px) rotate(-45deg);
  }

  /* Mobile menu overlay */
  .mobile-menu-overlay {
    display: none;
    position: fixed;
    top: 76px;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 99;
    backdrop-filter: blur(4px);
  }

  .mobile-nav {
    background-color: var(--nav-bg);
    max-width: 300px;
    width: 90%;
    margin: 0 auto;
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    margin-top: 20px;
  }

  .mobile-nav ul {
    list-style: none;
    padding: 12px 0;
    margin: 0;
  }

  .mobile-nav li {
    margin: 0;
  }

  .mobile-nav-link {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 16px 24px;
    color: var(--nav-text);
    text-decoration: none;
    font-size: 1.1rem;
    font-weight: 500;
    transition: all 0.2s ease;
  }

  .mobile-nav-link:hover {
    background-color: rgba(68, 147, 207, 0.1);
  }

  .mobile-nav-link.active {
    color: var(--ucla-light-blue);
    background-color: rgba(68, 147, 207, 0.05);
    font-weight: 600;
  }

  :global(.dark-mode) .mobile-nav-link.active {
    color: var(--ucla-yellow);
    background-color: rgba(252, 215, 41, 0.1);
  }

  .mobile-menu-divider {
    height: 1px;
    background-color: rgba(0, 0, 0, 0.1);
    margin: 8px 16px;
  }

  :global(.dark-mode) .mobile-menu-divider {
    background-color: rgba(255, 255, 255, 0.1);
  }

  /* Make the component responsive */
  @media (max-width: 960px) {
    /* Icons-only mode */
    .nav-item-front span {
      display: none; /* Hide text on smaller screens */
    }

    .nav-item-front {
      padding: 6px; /* Reduce padding when only showing icons */
    }

    .nav-item-front :global(svg) {
      width: 20px;
      height: 20px;
    }

    .menu-item-wrapper {
      min-width: 44px; /* Reduce width to fit icon only */
    }
  }

  @media (max-width: 768px) {
    .navbar-container {
      justify-content: space-between;
    }

    /* Hide desktop navigation and social icons */
    .desktop-nav,
    .desktop-only {
      display: none !important;
    }

    /* Show mobile hamburger menu */
    .mobile-only {
      display: flex;
    }

    .hamburger-button {
      display: flex;
    }

    .mobile-menu-overlay {
      display: block;
    }

    .logo {
      height: 50px;
    }
  }

  /* Social icons section */
  .social-icons {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 8px;
  }

  .social-icon {
    color: var(--nav-text);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: color 0.3s ease;
    text-decoration: none;
  }

  .social-icon:hover {
    color: var(--ucla-light-blue);
  }

  :global(.dark-mode) .social-icon:hover {
    color: var(--ucla-yellow);
  }



  @media (max-width: 480px) {
    .logo {
      height: 45px;
    }

    .mobile-nav {
      width: 95%;
    }

    .mobile-nav-link {
      padding: 14px 20px;
      font-size: 1rem;
    }
  }
  /* Icon styles to ensure proper theme colors */
  :global(.nav-icon) {
    transition: all 0.3s ease;
  }

  :global(.active-icon.light-theme-icon) {
    color: var(--ucla-light-blue) !important;
  }

  :global(.active-icon.dark-theme-icon) {
    color: var(--ucla-yellow) !important;
  }

  /* Extra small screens (very small phones) */
  @media (max-width: 380px) {
    .logo {
      height: 40px;
    }

    .hamburger-button {
      width: 28px;
      height: 28px;
    }

    .hamburger-line {
      width: 20px;
    }

    .mobile-nav-link {
      padding: 12px 16px;
      font-size: 0.95rem;
      gap: 12px;
    }

    .mobile-nav-link :global(svg) {
      width: 20px;
      height: 20px;
    }
  }

</style>
