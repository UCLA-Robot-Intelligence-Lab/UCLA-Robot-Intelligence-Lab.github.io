<script>
  // Contact information
</script>

<section class="content-section">
  <div class="container contact-container">
    <h1 class="contact-main-title">Contact Us</h1>

    <div class="contact-card">
      <h2>Prospective PhD students</h2>
      <p>
        Our lab is actively seeking motivated PhD students, ideally with
        experience in robotics and/or artificial intelligence. If you have a
        relevant background and are interested in joining URIL, please apply
        directly to the
        <a
          href="https://www.cs.ucla.edu/graduate-admissions/"
          class="text-link"
          target="_blank"
          rel="noopener noreferrer">UCLA CS PhD program.</a
        >
      </p>
    </div>

    <div class="contact-card">
      <h2>UCLA Master and Undergraduate students</h2>
      <p>
        Please fill out this
        <a
          href="https://forms.gle/d7uAPSB9nrQQJ3gcA"
          class="text-link"
          target="_blank"
          rel="noopener noreferrer">application form</a
        >
        to indicate your interest.
      </p>
    </div>

    <div class="contact-card">
      <h2>Summer undergraduate research intern</h2>
      <p>
        Please fill out this
        <a
          href="https://forms.gle/d7uAPSB9nrQQJ3gcA"
          class="text-link"
          target="_blank"
          rel="noopener noreferrer">application form</a
        >
        by March 1st (same year you wish to do a summer intern).
      </p>
    </div>

    <div class="contact-card">
      <p>
        We especially encourage students from historically underrepresented
        backgrounds in STEM to apply, even if your experience does not align
        precisely with robotics or AI!
      </p>
    </div>
  </div>
</section>

<style>
  /* Contact section styles */
  .content-section {
    padding: 4rem 0;
  }

  .contact-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 4rem;
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .contact-main-title {
    text-align: center;
    margin-bottom: 1rem;
    margin-top: 1rem;
    font-size: 2.5rem;
    color: var(--heading-color);
    font-weight: 700;
    letter-spacing: -0.03em;
    position: relative;
  }

  /* Removed underline for main contact title */

  .contact-card {
    background-color: var(--card-bg);
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    border: 1px solid rgba(68, 147, 207, 0.1); /* UCLA Light Blue with low opacity */
    transition:
      transform 0.3s ease,
      box-shadow 0.3s ease;
  }

  .contact-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.12);
  }

  .contact-card h2 {
    color: var(--heading-color);
    margin-top: 0;
    margin-bottom: 1.25rem;
    font-size: 1.6rem;
    position: relative;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid rgba(68, 147, 207, 0.1); /* UCLA Light Blue with opacity */
  }

  .contact-card p {
    margin-bottom: 0.75rem;
    line-height: 1.8;
    font-size: 1.1rem;
    color: var(--text-color);
  }

  .text-link {
    color: var(--ucla-light-blue);
    text-decoration: underline;
    transition: all 0.2s ease;
    font-weight: 500;
  }

  .text-link:hover {
    color: var(--ucla-dark-blue);
    text-decoration-color: var(--ucla-yellow);
  }

  @media (max-width: 767px) {
    .contact-container {
      padding: 0 1.5rem;
    }

    .contact-main-title {
      font-size: 2.2rem;
    }

    .contact-card {
      padding: 1.5rem;
    }
  }
</style>
