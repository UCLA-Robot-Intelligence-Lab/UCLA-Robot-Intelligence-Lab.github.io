<script>
  export let year = new Date().getFullYear();
</script>

<footer>
  <div class="footer-accent"></div>
  <div class="container">
    <p>© {year} <span class="accent">UCLA</span> Robot Intelligence Lab. Hosted by GitHub Pages.</p>
  </div>
</footer>

<style>
  footer {
    background-color: var(--footer-bg);
    color: var(--footer-text);
    padding: 20px 0;
    margin-top: 50px;
    text-align: center;
    transition: background-color 0.3s ease, color 0.3s ease;
    position: relative;
  }
  
  .footer-accent {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, var(--ucla-yellow) 0%, var(--ucla-light-blue) 100%);
  }
  
  .accent {
    color: var(--ucla-yellow);
    font-weight: bold;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }
</style>
