<script>
  import Container from '../components/Container.svelte';
  import VideoHero from '../components/VideoHero.svelte';
</script>

<VideoHero 
  videoSrc="/uril.mov"
  height="500px"
/>

<section class="about">
  <Container>
    <p class="fade-in">
      At the UCLA Robot Intelligence Lab (URIL), we are committed to 
      advancing the fields of robotics and
      artificial intelligence through innovative research. Our goal is to develop 
      intelligent systems that can adapt, learn efficiently, and collaborate effectively 
      with humans. We focus on both robot skill learning
      and human-robot interaction, aiming to address practical challenges and contribute to 
      meaningful applications. At URIL, we seek to bridge technical advancements with 
      human-centered design, working toward a future where 
      intelligent robots seamlessly integrate into and enhance everyday life.
    </p>
  </Container>
</section>

<style>

  
  /* About section */
  .about {
    padding: 60px 0;
  }

  .about p {
    font-size: 1.1rem;
    line-height: 1.8;
    max-width: 900px;
    margin: 0 auto;
  }
  
  /* Animation classes */
  .fade-in {
    animation: fadeIn 1s ease-in;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>