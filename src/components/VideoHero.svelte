<script lang="ts">
  import { onMount } from 'svelte';
  
  // Only export the height property as we're now using static file paths
  export let height = "500px";
  
  let videoElement: HTMLVideoElement;
  
  onMount(() => {
    if (videoElement) {
      // When the video reaches the end, pause on the last frame
      videoElement.addEventListener('ended', () => {
        // Slightly rewind to ensure the last frame is shown completely
        videoElement.currentTime = videoElement.duration - 0.01;
      });
    }
  });
</script>

<section class="hero-container" style="height:{height}">
  <!-- Directly embed video with simpler markup -->
  <div class="video-wrapper">
    <video 
      bind:this={videoElement}
      autoplay 
      muted 
      playsinline 
      preload="auto" 
      class="alpha-video">
      <!-- WebM format with alpha channel support -->
      <source src="/cropped-uril.webm" type="video/webm">
      <!-- Fallback to MOV format -->
      <source src="/Adobe/Untitled Project_AME/cropped-uril.mov" type="video/quicktime">
      Your browser does not support video playback.
    </video>
  </div>
</section>

<style>
  /* Container with transparent background */
  .hero-container {
    position: relative;
    width: 100%;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: transparent; /* Fully transparent background */
  }
  
  /* Video container */
  .video-wrapper {
    position: relative;
    z-index: 1;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  /* Video with alpha transparency */
  .alpha-video {
    max-width: 80%;
    max-height: 90%;
    object-fit: contain;
  }
  

  
  @media (max-width: 768px) {
    .alpha-video {
      max-width: 95%;
    }
  }
</style>
