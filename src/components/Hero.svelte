<script>
  import { onMount } from "svelte";

  export let title = "Title";
  export let subtitle = "";
  export let backgroundImage = "";
  export let overlayOpacity = 0.8;
  export let height = "400px";

  let animationStarted = false;
  let animationComplete = false;
  let logoVisible = false;

  onMount(() => {
    // Start the animation after a short delay
    setTimeout(() => {
      // Start with the letter animation
      animationStarted = true;

      // Complete the animation by condensing letters
      setTimeout(() => {
        animationComplete = true;

        // Fade in the logo at the very end
        setTimeout(() => {
          logoVisible = true;
        }, 800);
      }, 1500);
    }, 1000);
  });
</script>

<section
  class="hero"
  style="--background-image: url('{backgroundImage}'); --overlay-opacity: {overlayOpacity}; --height: {height};"
>
  <div class="hero-accent"></div>
  <div class="hero-content">
    <slot name="before-title"></slot>

    <div
      class="title-container {animationStarted
        ? 'animation-started'
        : ''} {animationComplete ? 'animation-complete' : ''}"
    >
      {#if title.includes("UCLA")}
        <!-- Animation container with logo and text -->
        <div class="animation-wrapper">
          <div class="logo-container {logoVisible ? 'visible' : ''}">
            <!-- Logo that fades in at the very end -->
            <img
              src="/Artboard 1 copy@4x.png"
              alt="URIL Logo"
              class="logo-image {logoVisible ? 'visible' : ''}"
            />
          </div>

          <!-- Title with highlighted letters that will form URIL -->
          <div class="full-title">
            <span class="letter-u">U</span><span class="rest-ucla">CLA</span>
            <span class="letter-r">R</span><span class="rest-robot">obot</span>
            <span class="letter-i">I</span><span class="rest-intelligence"
              >ntelligence</span
            >
            <span class="letter-l">L</span><span class="rest-lab">ab</span>
          </div>
        </div>
      {:else}
        <h1>{title}</h1>
      {/if}
    </div>

    {#if subtitle}
      <p class="tagline">{subtitle}</p>
    {/if}
    <slot></slot>
  </div>
</section>

<style>
  .hero {
    height: var(--height);
    background-color: var(--hero-bg);
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: background-color 0.3s ease;
  }

  .hero::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: linear-gradient(
        rgba(255, 255, 255, var(--overlay-opacity)),
        rgba(255, 255, 255, var(--overlay-opacity))
      ),
      var(--background-image);
    background-size: cover;
    background-position: center;
    z-index: -1;
  }

  .hero-accent {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 6px;
    background: linear-gradient(
      90deg,
      var(--ucla-yellow) 0%,
      var(--ucla-light-blue) 100%
    );
  }

  .hero-content {
    width: 100%;
    padding: 0 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  /* Animation container */
  .title-container {
    position: relative;
    font-size: 4.5rem;
    font-weight: bold;
    margin-bottom: 2rem;
    height: 9rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .full-title {
    position: absolute;
    white-space: nowrap;
    transition: all 1.5s cubic-bezier(0.68, -0.55, 0.27, 1.55);
  }

  .animation-wrapper {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
  }

  .logo-container {
    width: 45rem;
    display: flex;
    justify-content: flex-end;
    z-index: 2;
    position: absolute;
    left: calc(50% - 45rem); /* Position it more to the left */
    opacity: 0;
    transition: opacity 0.8s ease;
  }

  /* Only show logo container when logo is visible */
  .logo-container.visible {
    opacity: 1;
  }

  /* Animation classes */
  .animation-started .full-title {
    transform: translateX(150px);
  }

  .animation-started .rest-ucla,
  .animation-started .rest-robot,
  .animation-started .rest-intelligence,
  .animation-started .rest-lab {
    opacity: 0;
    transform: translateX(-20px);
    transition:
      opacity 1s,
      transform 1s;
  }

  /* When animation is complete, adjust spacing between letters */
  .animation-complete .letter-u,
  .animation-complete .letter-r,
  .animation-complete .letter-i,
  .animation-complete .letter-l {
    margin: 25px;
    transform: scale(3);
    transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }

  /* Move everything to the left after animation completes */
  .animation-complete .animation-wrapper {
    transform: translateX(-100px);
    transition: transform 0.01s ease;
  }

  /* Add extra space between U and R */
  .animation-complete .letter-u {
    margin-right: 60px;
  }

  /* Only apply the growth when the animation completes */
  .animation-started:not(.animation-complete) .letter-u,
  .animation-started:not(.animation-complete) .letter-r,
  .animation-started:not(.animation-complete) .letter-i,
  .animation-started:not(.animation-complete) .letter-l {
    transform: scale(1);
  }

  .animation-complete .rest-ucla,
  .animation-complete .rest-robot,
  .animation-complete .rest-intelligence,
  .animation-complete .rest-lab {
    display: none;
  }

  /* Letter styling */
  .letter-u {
    color: var(--ucla-light-blue);
    font-weight: bold;
    display: inline-block;
    transition: transform 1.5s cubic-bezier(0.68, -0.55, 0.27, 1.55);
  }

  .letter-r,
  .letter-i,
  .letter-l {
    color: var(--ucla-dark-blue);
    font-weight: bold;
    display: inline-block;
    transition: transform 1.5s cubic-bezier(0.68, -0.55, 0.27, 1.55);
  }

  .rest-ucla,
  .rest-robot,
  .rest-intelligence,
  .rest-lab {
    display: inline-block;
    transition: all 1s ease;
  }

  .rest-ucla {
    color: var(--ucla-light-blue);
    font-weight: bold;
  }

  .rest-robot,
  .rest-intelligence,
  .rest-lab {
    color: var(--ucla-dark-blue);
  }

  /* Logo image */
  .logo-image {
    height: 24rem;
    opacity: 0;
    transform: translateX(-20px);
    transition:
      opacity 0.8s,
      transform 0.8s;
    display: inline-block;
  }

  .logo-image.visible {
    opacity: 1;
    transform: translateX(0);
  }

  .tagline {
    font-size: 1.5rem;
    color: var(--text-color);
    transition: color 0.3s ease;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @media (max-width: 768px) {
    .title-container {
      font-size: 2.5rem;
    }

    .tagline {
      font-size: 1.2rem;
    }

    .logo-image {
      height: 3.5rem;
    }
  }

  @media (max-width: 480px) {
    .title-container {
      font-size: 2rem;
      height: 4rem;
    }

    .logo-image {
      height: 3rem;
    }
  }
</style>
