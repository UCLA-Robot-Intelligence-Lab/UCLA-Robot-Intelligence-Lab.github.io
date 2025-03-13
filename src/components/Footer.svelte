<script>
  export let year = new Date().getFullYear();
</script>

<footer>
  <div class="footer-accent"></div>
  <div class="footer-container">
    <p>© {year} UCLA Robot Intelligence Lab. Hosted by GitHub Pages.</p>
  </div>
</footer>

<style>
  footer {
    background-color: var(--card-bg);
    color: var(--text-color);
    padding: 30px 0;
    margin-top: 0px;
    text-align: center;
    transition: all 0.3s ease;
    position: relative;
    border-top: 1px solid rgba(68, 147, 207, 0.1); /* UCLA Light Blue with low opacity */
  }

  .footer-accent {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(
      90deg,
      var(--ucla-yellow) 0%,
      var(--ucla-light-blue) 50%,
      var(--ucla-dark-blue) 100%
    );
  }

  .footer-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 4rem;
  }

  p {
    margin: 0;
    font-size: 1rem;
    font-weight: 500;
  }

  @media (max-width: 767px) {
    .footer-container {
      padding: 0 1.5rem;
    }
  }
</style>
