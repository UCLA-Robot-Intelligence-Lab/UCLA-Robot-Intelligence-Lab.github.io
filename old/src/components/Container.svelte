<script>
  // This component provides a consistent container for content across the site
</script>

<div class="container">
  <slot />
</div>

<style>
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }

  @media (max-width: 768px) {
    .container {
      padding: 0 16px;
    }
  }

  @media (max-width: 480px) {
    .container {
      padding: 0 12px;
    }
  }
</style>
