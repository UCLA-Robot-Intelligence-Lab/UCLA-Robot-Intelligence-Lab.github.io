<script>
  // Contact information
</script>

<section class="content-section">
  <div class="container contact-container">
    <h1 class="contact-main-title">Contact Us</h1>

    <div class="contact-card">
      <div class="contact-section">
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

      <div class="contact-section">
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

      <div class="contact-section">
        <h2>Summer undergraduate research intern</h2>
        <p>
          Please fill out this
          <a
            href="https://forms.gle/d7uAPSB9nrQQJ3gcA"
            class="text-link"
            target="_blank"
            rel="noopener noreferrer">application form</a
          >
          by March 1st (same year you wish to do a summer internship).
        </p>
      </div>

      <div class="contact-section note">
        <p>
          We especially encourage students from historically underrepresented
          backgrounds in STEM to apply, even if your experience does not align
          precisely with robotics or AI!
        </p>
      </div>
    </div>
  </div>
</section>

<style>
  /* Contact section styles */
  .content-section {
    padding: 30px 0 80px;
    background-color: white;
  }

  .contact-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .contact-main-title {
    text-align: left;
    margin-bottom: 15px;
    margin-top: 0;
    font-size: 2.5rem;
    color: #1a1a1a;
    font-weight: 600;
    letter-spacing: -0.02em;
  }

  .contact-card {
    display: flex;
    flex-direction: column;
    gap: 2.5rem;
  }
  
  .contact-section {
    padding-bottom: 0;
    border-bottom: none;
  }
  
  .contact-section:last-child {
    padding-bottom: 0;
    border-bottom: none;
  }
  
  .contact-section.note {
    margin-top: 0.5rem;
    background-color: #f9f9f9;
    border-left: 3px solid #4493CF;
    border-radius: 4px;
    padding: 0.5rem 1.5rem 0.75rem 1.5rem;
  }

  .contact-card h2 {
    color: #1a1a1a;
    margin-top: 0;
    margin-bottom: 0.75rem;
    font-size: 1.3rem;
    font-weight: 600;
    padding-bottom: 0;
    border-bottom: none;
  }

  .contact-card p {
    margin-bottom: 0;
    line-height: 1.75;
    font-size: 1rem;
    color: #333333;
  }

  .text-link {
    color: #4493CF;
    text-decoration: none;
    transition: color 0.2s ease;
    font-weight: 500;
  }

  .text-link:hover {
    color: #2a7ab8;
    text-decoration: underline;
  }

  @media (max-width: 768px) {
    .contact-main-title {
      font-size: 2rem;
    }

    .contact-card h2 {
      font-size: 1.2rem;
    }

    .contact-card p {
      font-size: 0.95rem;
    }
  }
</style>
