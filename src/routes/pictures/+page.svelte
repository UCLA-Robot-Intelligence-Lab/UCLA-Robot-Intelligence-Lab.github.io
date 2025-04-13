<script lang="ts">
  import ParallaxScroll from "../../components/ParallaxScroll.svelte";
  import { onMount } from "svelte";

  // Array of actual lab images
  const labImages = [
    "/lab-pics/lab1.jpg",
    "/lab-pics/lab2.jpg",
    "/lab-pics/lab3.jpg",
    "/lab-pics/lab4.jpg",
    "/lab-pics/lab5.jpg",
    "/lab-pics/lab6.jpg",
    "/lab-pics/lab7.jpg",
    "/lab-pics/lab8.jpg",
    "/lab-pics/lab9.jpg",
    "/lab-pics/lab10.jpg",
    "/lab-pics/lab11.jpg",
    "/lab-pics/lab12.jpg",
  ];

  // Use actual images directly
  let images = labImages;

  let mounted = false;

  onMount(() => {
    mounted = true;
  });
</script>

<svelte:head>
  <title>UCLA Robot Intelligence Lab - Pictures</title>
  <meta
    name="description"
    content="Pictures from the UCLA Robot Intelligence Lab"
  />
</svelte:head>

<div class="min-h-screen bg-white dark:bg-gray-900">
  <div class="container mx-auto px-4 py-8">
    <h1
      class="text-4xl md:text-5xl font-bold text-[#18315b] dark:text-[#fcd804] mb-8 text-center"
    >
      Lab Gallery
    </h1>

    <div class="mb-10 text-center max-w-2xl mx-auto">
      <p class="text-lg text-gray-700 dark:text-gray-300">
        A glimpse into the UCLA Robot Intelligence Lab's activities, research,
        and projects.
      </p>
    </div>

    {#if mounted}
      <ParallaxScroll {images} className="h-full py-8" />
    {:else}
      <div class="flex justify-center items-center h-64">
        <div class="text-[#3490ce] dark:text-[#fcd804] text-xl">
          Loading gallery...
        </div>
      </div>
    {/if}
  </div>
</div>

<style>
  /* Custom styling with UCLA colors */
  :global(.dark) {
    --ucla-yellow: #fcd804;
    --ucla-dark-blue: #18315b;
    --ucla-light-blue: #3490ce;
  }

  :global(body) {
    --ucla-yellow: #fcd804;
    --ucla-dark-blue: #18315b;
    --ucla-light-blue: #3490ce;
  }

  h1 {
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
  }
</style>
