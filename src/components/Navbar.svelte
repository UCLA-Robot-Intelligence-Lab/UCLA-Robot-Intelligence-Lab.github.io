<script lang="ts">
  import { page } from "$app/stores";
  import ThemeToggle from "./ThemeToggle.svelte";
  import { onMount } from "svelte";
  import { tweened } from "svelte/motion";
  import { cubicOut } from "svelte/easing";
  import { slide, fly } from "svelte/transition";
  import { quintOut } from "svelte/easing";
  import { theme } from "$lib/stores/theme";

  // Import icons this way instead
  import HomeIcon from "lucide-svelte/icons/home";
  import UsersIcon from "lucide-svelte/icons/users";
  import FileTextIcon from "lucide-svelte/icons/file-text";
  import BookIcon from "lucide-svelte/icons/book";
  import MailIcon from "lucide-svelte/icons/mail";

  // Logo image path is now hardcoded
  const logoSrc = "/full_logo.png";

  // Get the current theme for conditional styling
  let currentTheme = 'light';
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
  
  // Navigation links with their properties
  const navLinks: NavLink[] = [
    {
      name: "Home",
      href: "/",
      id: "home",
      icon: HomeIcon,
      gradient: getActiveGradient(currentTheme === 'light'),
      iconColor: getActiveIconColor(currentTheme === 'light'),
    },
    {
      name: "People",
      href: "/people",
      id: "people",
      icon: UsersIcon,
      gradient: getActiveGradient(currentTheme === 'light'),
      iconColor: getActiveIconColor(currentTheme === 'light'),
    },
    {
      name: "Research",
      href: "/research",
      id: "research",
      icon: FileTextIcon,
      gradient: getActiveGradient(currentTheme === 'light'),
      iconColor: getActiveIconColor(currentTheme === 'light'),
    },
    {
      name: "Publications",
      href: "/publications",
      id: "publications",
      icon: BookIcon,
      gradient: getActiveGradient(currentTheme === 'light'),
      iconColor: getActiveIconColor(currentTheme === 'light'),
    },
    {
      name: "Contact",
      href: "/contact",
      id: "contact",
      icon: MailIcon,
      gradient: getActiveGradient(currentTheme === 'light'),
      iconColor: getActiveIconColor(currentTheme === 'light'),
    },
  ];

  // Define the interface for our navigation links
  interface NavLink {
    name: string;
    href: string;
    id: string;
    icon: any; // Using 'any' for Svelte component type
    gradient: string;
    iconColor: string;
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
        <img
          src="/original-uril.png"
          alt="UCLA Robot Intelligence Lab Logo"
          class="logo"
        />
      </div>

      <nav class="modern-nav">
        <div class="nav-menu-container">
          <div class="nav-glow-background"></div>
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
                  <!-- Glow effect that scales on hover (only in dark mode) -->
                  <div
                    class="glow"
                    style="
                    background: {link.gradient}; 
                    opacity: {(hoveredItem === link.id || isActive(link)) && currentTheme === 'dark'
                      ? 0.7
                      : 0};
                    transform: scale({(hoveredItem === link.id || isActive(link)) && currentTheme === 'dark'
                      ? 1.4
                      : 0.8});
                    box-shadow: 0 0 15px 0 rgba(252,215,41,{(hoveredItem === link.id || isActive(link)) && currentTheme === 'dark'
                      ? 0.3
                      : 0});
                  "
                  ></div>

                  <!-- Front face of the menu item -->
                  <a
                    href={link.href}
                    class="nav-item-front"
                    class:active={isActive(link)}
                    style="
                    transform: rotateX({hoveredItem === link.id
                      ? '-90deg'
                      : '0deg'}); 
                    opacity: {hoveredItem === link.id ? 0 : 1};
                  "
                  >
                    <svelte:component
                      this={link.icon}
                      size="20"
                      color={hoveredItem === link.id || isActive(link)
                        ? currentTheme === 'light' ? "var(--ucla-light-blue)" : "var(--ucla-yellow)"
                        : "currentColor"}
                      style="filter: {hoveredItem === link.id && currentTheme === 'dark'
                        ? 'drop-shadow(0 0 3px rgba(252,215,41,0.7))'
                        : 'none'}; transform: {hoveredItem === link.id
                        ? 'scale(1.1)'
                        : 'scale(1)'}; transition: all 0.3s ease; font-weight: {isActive(link) && currentTheme === 'light' ? '700' : 'normal'};"
                    />
                    <span style="font-weight: {isActive(link) && currentTheme === 'light' ? '700' : 'normal'};">{link.name}</span>
                  </a>

                  <!-- Back face of the menu item (shows on hover) -->
                  <a
                    href={link.href}
                    class="nav-item-back"
                    class:active={isActive(link)}
                    style="
                    transform: rotateX({hoveredItem === link.id
                      ? '0deg'
                      : '90deg'}); 
                    opacity: {hoveredItem === link.id ? 1 : 0};
                  "
                  >
                    <svelte:component
                      this={link.icon}
                      size="20"
                      color={hoveredItem === link.id || isActive(link)
                        ? currentTheme === 'light' ? "var(--ucla-light-blue)" : "var(--ucla-yellow)"
                        : "currentColor"}
                      style="filter: {hoveredItem === link.id && currentTheme === 'dark'
                        ? 'drop-shadow(0 0 3px rgba(252,215,41,0.7))'
                        : 'none'}; transform: {hoveredItem === link.id
                        ? 'scale(1.1)'
                        : 'scale(1)'}; transition: all 0.3s ease; font-weight: {isActive(link) && currentTheme === 'light' ? '700' : 'normal'};"
                    />
                    <span style="font-weight: {isActive(link) && currentTheme === 'light' ? '700' : 'normal'};">{link.name}</span>
                  </a>
                </div>
              </li>
            {/each}
          </ul>
        </div>
      </nav>

      <div class="theme-toggle-container">
        <ThemeToggle />
      </div>
    </div>
  </div>
  <div class="navbar-accent"></div>
</header>

<style>
  header {
    background-color: var(--nav-bg);
    color: var(--nav-text);
    padding: 6px 0;
    transition:
      background-color 0.3s ease,
      color 0.3s ease;
    position: relative;
    z-index: 100;
    backdrop-filter: blur(10px);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .navbar-container {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    align-items: center;
    padding: 1px 0;
  }

  .logo-container {
    display: flex;
    align-items: center;
    padding: 2px;
    position: relative;
    z-index: 5;
    grid-column: 1;
    justify-self: start;
  }

  .logo {
    height: 13vh;
  }

  .theme-toggle-container {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    z-index: 5;
    grid-column: 3;
    justify-self: end;
  }

  /* Modern navigation styling */
  .modern-nav {
    position: relative;
    display: flex;
    justify-content: center;
    padding: 2px 2px;
    overflow: visible; /* Allow glow to extend beyond boundaries */
    min-width: 0; /* Allow flex container to shrink below content size */
    grid-column: 2;
    width: 100%;
  }

  .nav-glow-background {
    position: absolute;
    inset: 0;
    border-radius: 1rem;
    background: linear-gradient(
      to right,
      rgba(252, 215, 41, 0.03),
      rgba(252, 215, 41, 0.05),
      rgba(252, 215, 41, 0.03)
    );
    backdrop-filter: blur(8px);
    z-index: 0;
    pointer-events: none;
  }

  .nav-menu-container {
    position: relative;
    display: inline-flex;
    margin: 0 auto;
    padding: 0;
    border-radius: 1rem;
    overflow: visible;
    border: 1px solid rgba(252, 215, 41, 0.15); /* Add a subtle border */
    box-shadow:
      0 4px 12px rgba(0, 0, 0, 0.05),
      0 0 2px rgba(252, 215, 41, 0.2);
    background: linear-gradient(
      to bottom,
      var(--nav-bg-light) 0%,
      var(--nav-bg-dark) 100%
    );
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

  .glow {
    position: absolute;
    inset: 0; /* Removed negative inset to prevent visible border */
    border-radius: 12px; /* Match exactly with the menu item border radius */
    opacity: 0;
    transform: scale(0.8);
    transition:
      opacity 0.3s ease,
      transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    z-index: 0;
    pointer-events: none;
    will-change: transform, opacity;
    filter: blur(8px); /* Increased blur to create glow without visible edges */
  }

  .nav-item-front,
  .nav-item-back {
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

  .nav-item-front {
    transform-origin: center bottom;
  }

  .nav-item-back {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    transform-origin: center top;
    height: 100%;
  }

  .nav-item-front.active,
  .nav-item-back.active {
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
    .nav-item-front span,
    .nav-item-back span {
      display: none; /* Hide text on smaller screens */
    }

    .nav-item-front,
    .nav-item-back {
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
      height: 75px; /* Keep logo bigger even on smaller screens */
    }
  }

  /* Gradient accent line at the bottom of navbar */
  .navbar-accent {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(
      90deg,
      var(--ucla-yellow) 0%,
      var(--ucla-light-blue) 100%
    );
    z-index: 10;
  }

  @media (max-width: 480px) {
    .logo-container {
      padding: 3px; /* Reduce padding */
    }

    .nav-item-front,
    .nav-item-back {
      padding: 6px; /* Further reduce padding */
    }

    .menu-item-wrapper {
      margin: 2px; /* Reduce margin between items */
      min-width: 36px; /* Even smaller for very small screens */
    }

    .theme-toggle-container {
      transform: scale(0.9); /* Slightly smaller theme toggle */
    }
  }
</style>
