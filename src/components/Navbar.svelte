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

  onMount(() => {
    mounted = true;
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

      <nav class="modern-nav">
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

      <div class="social-icons">
        <a href="https://github.com/UCLA-Robot-Intelligence-Lab" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="GitHub">
          <GithubIcon size={24} />
        </a>
        <a href="/pictures" class="social-icon" aria-label="Photos">
          <CameraIcon size={24} />
        </a>
      </div>

      <!-- <div class="theme-toggle-container">
        <ThemeToggle />
      </div> -->
    </div>
  </div>
</header>

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

  /* Make the component responsive */
  @media (max-width: 960px) {
    /* Icons-only mode */
    .nav-item-front span {
      display: none; /* Hide text on smaller screens */
    }

    .nav-item-front {
      padding: 6px; /* Reduce padding when only showing icons */
    }

    .menu-item-wrapper {
      min-width: 44px; /* Reduce width to fit icon only */
    }
  }

  @media (max-width: 768px) {
    .navbar-container {
      flex-direction: row; /* Keep horizontal layout */
      flex-wrap: nowrap; /* Prevent wrapping */
      gap: 8px;
      justify-content: space-between;
    }

    .modern-nav {
      justify-content: center;
      flex: 0 1 auto; /* Allow shrinking but not growing */
    }

    .modern-nav ul {
      gap: 4px;
      flex-wrap: nowrap; /* Prevent wrapping to keep horizontal */
    }

    .logo {
      height: 90px; /* Keep logo bigger even on smaller screens */
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
    .logo-container {
      padding: 3px; /* Reduce padding */
    }

    .nav-item-front {
      padding: 6px; /* Further reduce padding */
    }

    .menu-item-wrapper {
      margin: 2px; /* Reduce margin between items */
      min-width: 36px; /* Even smaller for very small screens */
    }

    /* .theme-toggle-container {
      transform: scale(0.9);
    } */
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

</style>
