<script lang="ts">
  import { onMount } from "svelte";
  import { fade, fly, scale } from "svelte/transition";
  import { cubicOut } from "svelte/easing";
  import { browser } from "$app/environment";

  // Define image interface
  interface GalleryImage {
    url: string;
    caption: string;
    alt: string;
  }

  // Array of lab images with descriptions
  const labImages: GalleryImage[] = [
    {
      url: "/lab-pics/lab1.jpg",
      caption: "CORL Submission Celebration",
      alt: "CORL Submission Celebration",
    },
    {
      url: "/lab-pics/lab2.jpg",
      caption: "Lab Meeting Social",
      alt: "Lab MeetingSocial",
    },
    {
      url: "/lab-pics/lab3.jpg",
      caption: "Lab dinner 😋",
      alt: "Lab dinner",
    },
    {
      url: "/lab-pics/lab4.jpg",
      caption: "Lab dinner v2",
      alt: "Lab dinner v2",
    },
    {
      url: "/lab-pics/lab5.jpg",
      caption: "Lab dinner v3",
      alt: "Lab dinner v3",
    },
    {
      url: "/lab-pics/lab6.jpg",
      caption: "Lab Kayaking Trip",
      alt: "Lab Kayaking Trip",
    },
    {
      url: "/lab-pics/lab7.jpg",
      caption: "Lab Picnic Social",
      alt: "Lab Picnic Social",
    },
    {
      url: "/lab-pics/lab8.jpg",
      caption: "Lab birthday celebration",
      alt: "Lab birthday celebration",
    },
    {
      url: "/lab-pics/lab9.jpg",
      caption: "Hard at Work",
      alt: "Hard at Work",
    },
    {
      url: "/lab-pics/lab10.jpg",
      caption: "Lab BBQ Social",
      alt: "Lab BBQ Social",
    },
  ];

  // Lightbox state
  let lightboxOpen = false;
  let currentImageIndex = 0;
  let transitioning = false;
  let galleryLoaded = false;
  let scrollPosition = 0; // Store scroll position

  // Categories (could be expanded in the future)
  const categories = ["All", "Research", "Equipment", "Team"];
  let selectedCategory = "All";

  // Loading sequence
  let imagesLoaded = 0;
  $: loadProgress = (imagesLoaded / labImages.length) * 100;

  // Masonry layout helpers
  let masonryColumns = 3;

  // Handle image click to open lightbox
  function openLightbox(index: number): void {
    if (browser) {
      // Store current scroll position
      scrollPosition = window.scrollY;
      currentImageIndex = index;
      lightboxOpen = true;
      // Prevent scrolling when lightbox is open
      document.body.style.overflow = "hidden";
      document.body.classList.add("lightbox-active");
      // Hide navbar
      const navbar = document.querySelector("header");
      if (navbar) {
        navbar.style.display = "none";
      }
      // Add keyboard listener
      window.addEventListener("keydown", handleKeydown);
    }
  }

  // Close lightbox
  function closeLightbox() {
    lightboxOpen = false;
    if (browser) {
      document.body.style.overflow = "";
      document.body.classList.remove("lightbox-active");
      // Restore navbar
      const navbar = document.querySelector("header");
      if (navbar) {
        navbar.style.display = "";
      }
      // Add ability to close with Escape key for better accessibility
      window.removeEventListener("keydown", handleKeydown);
    }
  }

  // Navigate to next image
  function nextImage() {
    if (transitioning) return;
    transitioning = true;
    setTimeout(() => {
      currentImageIndex = (currentImageIndex + 1) % labImages.length;
      transitioning = false;
    }, 300);
  }

  // Navigate to previous image
  function prevImage() {
    if (transitioning) return;
    transitioning = true;
    setTimeout(() => {
      currentImageIndex =
        (currentImageIndex - 1 + labImages.length) % labImages.length;
      transitioning = false;
    }, 300);
  }

  // Handle key presses for navigation
  function handleKeydown(event: KeyboardEvent): void {
    if (!lightboxOpen) return;

    if (event.key === "Escape") {
      closeLightbox();
    } else if (event.key === "ArrowRight") {
      nextImage();
    } else if (event.key === "ArrowLeft") {
      prevImage();
    }
  }

  // Filter images by category (placeholder function - could be expanded)
  function filterByCategory(category: string): void {
    selectedCategory = category;
    // In a real app, you would filter the images based on category
  }

  // Track image loading progress
  function imageLoaded() {
    imagesLoaded++;
    if (imagesLoaded === labImages.length) {
      galleryLoaded = true;
    }
  }

  // Responsive columns adjustment
  function updateMasonryColumns() {
    if (window.innerWidth < 640) {
      // Small mobile
      masonryColumns = 1;
    } else if (window.innerWidth < 768) {
      // Mobile
      masonryColumns = 2;
    } else {
      // Tablet and above
      masonryColumns = 3;
    }
  }

  onMount(() => {
    // Set up responsive columns
    updateMasonryColumns();
    window.addEventListener("resize", updateMasonryColumns);

    // Add keyboard listener only when lightbox is open
    if (lightboxOpen) {
      window.addEventListener("keydown", handleKeydown);
    }

    // Cleanup on component destruction
    return () => {
      window.removeEventListener("keydown", handleKeydown);
      window.removeEventListener("resize", updateMasonryColumns);
      document.body.style.overflow = "";
    };
  });

  // Watch for lightbox state changes
  $: if (browser && lightboxOpen) {
    // Add keyboard listener when lightbox opens
    window.addEventListener("keydown", handleKeydown);
  }

  // Distribute images into columns for masonry effect
  $: columnImages = Array.from({ length: masonryColumns }, (_, i) =>
    labImages.filter((_, index) => index % masonryColumns === i),
  );
</script>

<svelte:head>
  <title>UCLA Robot Intelligence Lab - Picture Gallery</title>
  <meta
    name="description"
    content="Interactive polaroid-style gallery showcasing the UCLA Robot Intelligence Lab's activities, research, and projects"
  />
  <!-- Add Google font for handwritten polaroid effect -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
  <link
    href="https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap"
    rel="stylesheet"
  />
</svelte:head>

<div class="gallery-container">
  <div class="gallery-header">
    <h1>Lab Gallery</h1>
    <p class="gallery-subtitle">
      A glimpse into the UCLA Robot Intelligence Lab's activities, research, and
      projects.
    </p>
  </div>

  <!-- Categories removed as requested -->

  <!-- Loading indicator -->
  {#if !galleryLoaded}
    <div class="loading-container">
      <div class="loading-bar">
        <div class="loading-progress" style="width: {loadProgress}%"></div>
      </div>
      <p>Loading gallery... {Math.round(loadProgress)}%</p>
    </div>
  {/if}

  <!-- Gallery masonry grid -->
  <div class="gallery-grid" style="--columns: {masonryColumns}">
    {#each columnImages as column, colIndex}
      <div class="gallery-column">
        {#each column as image, rowIndex}
          {@const imageIndex = colIndex + rowIndex * masonryColumns}
          <div
            class="gallery-item"
            in:fade={{ delay: 100 * imageIndex, duration: 800 }}
          >
            <button
              class="image-container"
              on:click={() => openLightbox(imageIndex)}
              on:keydown={(e) => e.key === "Enter" && openLightbox(imageIndex)}
              aria-label={image.caption}
              style="--random-rotate: {Math.random() * 6 - 3}"
            >
              <img
                src={image.url}
                alt={image.alt}
                on:load={imageLoaded}
                loading="lazy"
              />
            </button>
          </div>
        {/each}
      </div>
    {/each}
  </div>
</div>

<!-- Lightbox - Create portal to render directly to body -->
{#if lightboxOpen}
  <div class="lightbox-wrapper" transition:fade={{ duration: 300 }}>
    <button
      class="lightbox-backdrop"
      on:click={closeLightbox}
      on:keydown={(e) => e.key === "Escape" && closeLightbox()}
      aria-label="Close lightbox"
    ></button>
    <div
      class="lightbox-content"
      on:click|stopPropagation
      on:keydown|stopPropagation
      role="presentation"
    >
      <button
        class="lightbox-close"
        on:click={closeLightbox}
        aria-label="Close lightbox"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <line x1="18" y1="6" x2="6" y2="18" />
          <line x1="6" y1="6" x2="18" y2="18" />
        </svg>
      </button>

      <button
        class="lightbox-nav prev"
        on:click={prevImage}
        aria-label="Previous image"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <polyline points="15 18 9 12 15 6" />
        </svg>
      </button>

      <button
        class="lightbox-nav next"
        on:click={nextImage}
        aria-label="Next image"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <polyline points="9 18 15 12 9 6" />
        </svg>
      </button>

      <div class="lightbox-image-container">
        {#key currentImageIndex}
          <img
            src={labImages[currentImageIndex].url}
            alt={labImages[currentImageIndex].alt}
            in:scale={{
              duration: 300,
              opacity: 0,
              start: 0.8,
              easing: cubicOut,
            }}
          />
        {/key}
        <div class="lightbox-caption">
          <p>{labImages[currentImageIndex].caption}</p>
          <span class="lightbox-counter"
            >{currentImageIndex + 1} / {labImages.length}</span
          >
        </div>
      </div>
    </div>
  </div>
{/if}

<style>
  /* Ensure lightbox is above everything */
  :global(body.lightbox-active) {
    overflow: hidden !important;
  }

  /* Hide unused CSS selector warning */
  :global(.category-btn) {
    display: none;
  }

  /* UCLA color variables */
  :global(:root) {
    --ucla-yellow: #fcd804;
    --ucla-yellow-light: rgba(252, 215, 4, 0.15);
    --ucla-dark-blue: #18315b;
    --ucla-light-blue: #3490ce;
    --ucla-light-blue-15: rgba(52, 144, 206, 0.15);
    --ucla-light-blue-30: rgba(52, 144, 206, 0.3);
    --text-color: #333;
    --text-light: #fff;
    --bg-color: #fff;
    --overlay-color: rgba(24, 49, 91, 0.7);
  }

  :global(.dark) {
    --text-color: #eee;
    --bg-color: #1a1a1a;
    --overlay-color: rgba(252, 215, 4, 0.8);
  }

  /* Gallery container */
  .gallery-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 2rem 1.5rem 4rem;
  }

  /* Gallery header */
  .gallery-header {
    text-align: center;
    margin-bottom: 2.5rem;
  }

  h1 {
    font-size: 3rem;
    font-weight: 700;
    color: var(--heading-color);
    margin-bottom: 0.5rem;
    letter-spacing: -0.03em;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
  }

  .gallery-subtitle {
    font-size: 1.25rem;
    color: var(--text-color);
    max-width: 700px;
    margin: 0 auto;
    line-height: 1.6;
  }

  :global(.dark-mode) .gallery-subtitle {
    color: white;
  }

  /* Categories section removed */

  /* Loading indicator */
  .loading-container {
    text-align: center;
    padding: 3rem 0;
  }

  .loading-bar {
    height: 8px;
    background-color: #eee;
    border-radius: 4px;
    margin: 0 auto 1rem;
    max-width: 300px;
    overflow: hidden;
  }

  .loading-progress {
    height: 100%;
    background-color: var(--ucla-light-blue);
    transition: width 0.3s ease;
  }

  :global(.dark-mode) .loading-progress {
    background-color: var(--ucla-yellow);
  }

  /* Gallery grid - Masonry layout */
  .gallery-grid {
    display: grid;
    grid-template-columns: repeat(var(--columns), 1fr);
    gap: 2.5rem;
    width: 100%;
    padding: 1rem;
  }

  .gallery-column {
    display: flex;
    flex-direction: column;
    gap: 2.5rem;
  }

  .gallery-item {
    break-inside: avoid;
    margin-bottom: 2rem;
    perspective: 1000px;
  }

  .image-container {
    position: relative;
    cursor: pointer;
    transition: all 0.3s ease;
    /* Make it look like a div not a button */
    background: white;
    border: none;
    padding: 0;
    width: 100%;
    text-align: left;
    /* Polaroid effect */
    border: 12px solid white;
    border-bottom: 45px solid white;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
    /* Random slight rotation */
    transform: rotate(calc(var(--random-rotate) * 1deg));
  }

  :global(.dark-mode) .image-container {
    background: #f0f0f0;
    border-color: #f0f0f0;
  }

  .image-container:hover {
    transform: rotate(calc(var(--random-rotate) * 1deg)) translateY(-10px);
    box-shadow: 0 15px 26px rgba(0, 0, 0, 0.25);
  }

  .image-container img {
    width: 100%;
    display: block;
    transition: all 0.3s ease;
    filter: saturate(1.1) contrast(1.1);
  }

  .image-container:after {
    content: attr(aria-label);
    position: absolute;
    bottom: -35px;
    left: 0;
    width: 100%;
    text-align: center;
    font-family: "Indie Flower", cursive, sans-serif;
    font-size: 1rem;
    color: #333;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  :global(.dark-mode) .image-container:after {
    color: #222;
  }

  /* Overlay effects */
  /* Remove overlay effects in favor of the polaroid style */

  /* Lightbox */
  .lightbox-wrapper {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 100000; /* Extremely high z-index */
    pointer-events: all;
  }

  .lightbox-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.95);
    z-index: 99999;
    /* Make it look like a div, not a button */
    border: none;
    margin: 0;
    padding: 0;
    cursor: pointer;
    appearance: none;
    width: 100%;
    height: 100%;
  }

  .lightbox-content {
    position: relative;
    width: 90%;
    height: 90%;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 100001; /* Even higher than the wrapper */
  }

  .lightbox-image-container {
    position: relative;
    max-width: 100%;
    max-height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .lightbox-image-container img {
    max-width: 100%;
    max-height: 80vh;
    object-fit: contain;
    border-radius: 4px;
  }

  .lightbox-caption {
    color: white;
    text-align: center;
    padding: 1rem;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .lightbox-caption p {
    font-size: 1.1rem;
    margin: 0;
  }

  .lightbox-counter {
    font-size: 0.9rem;
    opacity: 0.7;
  }

  .lightbox-close {
    position: fixed; /* Changed from absolute to fixed */
    top: 1.5rem;
    right: 1.5rem;
    background: var(--ucla-dark-blue);
    border: 2px solid white;
    color: white;
    font-size: 2rem;
    cursor: pointer;
    z-index: 100002; /* Higher than lightbox content */
    width: 46px;
    height: 46px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    transition: all 0.3s ease;
  }

  .lightbox-close:hover {
    background-color: #e74c3c; /* Red color on hover for better visibility */
    transform: scale(1.1);
  }

  .lightbox-close svg {
    width: 24px;
    height: 24px;
  }

  .lightbox-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0, 0, 0, 0.5);
    color: white;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background-color 0.3s ease;
    z-index: 100002; /* Match with close button */
    border: none;
    padding: 0;
  }

  .lightbox-nav:hover {
    background-color: rgba(0, 0, 0, 0.8);
  }

  .lightbox-nav.prev {
    left: 1rem;
  }

  .lightbox-nav.next {
    right: 1rem;
  }

  .lightbox-nav svg {
    width: 30px;
    height: 30px;
  }

  /* Responsive adjustments */
  @media (max-width: 768px) {
    .gallery-container {
      padding: 1.5rem 1rem 3rem;
    }

    h1 {
      font-size: 2.5rem;
    }

    .gallery-subtitle {
      font-size: 1.1rem;
    }

    .lightbox-nav {
      width: 40px;
      height: 40px;
    }

    .lightbox-nav svg {
      width: 24px;
      height: 24px;
    }
  }

  @media (max-width: 640px) {
    h1 {
      font-size: 2rem;
    }

    .gallery-subtitle {
      font-size: 1rem;
    }

    .category-btn {
      padding: 0.4rem 1rem;
      font-size: 0.9rem;
    }

    .lightbox-caption {
      flex-direction: column;
      gap: 0.5rem;
    }

    .lightbox-caption p {
      font-size: 1rem;
    }
  }
</style>
