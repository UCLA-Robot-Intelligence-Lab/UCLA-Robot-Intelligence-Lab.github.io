<script>
  import { onMount } from 'svelte';
  import Container from '../components/Container.svelte';
  import ExternalLink from 'lucide-svelte/icons/external-link';

  const newsItems = [
    {
      date: 'Jan 23, 2026',
      description: '2 papers submitted to ICML!'
    },
    {
      date: 'Oct 20, 2025',
      parts: [
        { text: 'Max', link: '/people#maximilian-gilles' },
        { text: ' joins URIL as visiting student from Germany!' }
      ]
    },
    {
      date: 'Sep 22, 2024',
      parts: [
        { text: 'Omar', link: '/people#omar-rayyan' },
        { text: ' joins the lab as a PhD student' }
      ]
    }
  ];

  onMount(() => {
    // Add js-enabled class to html element
    if (typeof document !== 'undefined') {
      document.documentElement.classList.add('js-enabled');
      document.documentElement.classList.remove('no-js');
    }

    // Create observer for scroll animations
    const options = {
      root: null,
      rootMargin: '0px',
      threshold: 0.15
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const delay = Math.random() * 150;
          setTimeout(() => {
            entry.target.classList.add('in-view');
          }, delay);
          observer.unobserve(entry.target);
        }
      });
    }, options);

    // Observe elements
    const newsItems = document.querySelectorAll('.news-item');
    newsItems.forEach(item => observer.observe(item));

    const researchAreas = document.querySelectorAll('.research-area');
    researchAreas.forEach(area => observer.observe(area));

    // Observe headings
    const headingOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.5
    };

    const headingObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('heading-visible');
          headingObserver.unobserve(entry.target);
        }
      });
    }, headingOptions);

    const headings = document.querySelectorAll('.section-heading');
    headings.forEach(heading => headingObserver.observe(heading));

    const hero = document.querySelector('.hero-content');
    if (hero) headingObserver.observe(hero);
  });
</script>

<section class="hero">
  <Container>
    <div class="hero-content">
      <div class="hero-image-wrapper">
        <img src="/lab-pics/labphoto.jpg" alt="UCLA Robot Intelligence Lab" class="hero-image" />
      </div>
      <div class="hero-description">
        <p>
          At the UCLA Robot Intelligence Lab (URIL), we are committed to 
          advancing the fields of robotics and artificial intelligence through innovative research. 
          Our goal is to develop intelligent systems that can adapt, learn efficiently, and collaborate effectively 
          with humans. We focus on both robot skill learning and human-robot interaction, aiming to address 
          practical challenges and contribute to meaningful applications. At URIL, we seek to bridge technical 
          advancements with human-centered design, working toward a future where intelligent robots seamlessly 
          integrate into and enhance everyday life.
        </p>
      </div>
    </div>
  </Container>
</section>

<section class="news">
  <Container>
    <div class="news-header section-heading">
      <h2>News</h2>
      <p class="news-subtitle">Recent updates from our lab</p>
    </div>
    
    <div class="news-list">
      {#each newsItems as item}
        <div class="news-item">
          <div class="news-date">{item.date}</div>
          <div class="news-description">
            {#if item.description}
              <span>{item.description}</span>
            {:else if item.parts}
              {#each item.parts as part}
                {#if part.link}
                  <a href={part.link} class="news-text-link">{part.text}</a>
                {:else}
                  <span>{part.text}</span>
                {/if}
              {/each}
            {/if}
          </div>
        </div>
      {/each}
    </div>
  </Container>
</section>

<section class="research">
  <Container>
    <div class="research-header section-heading">
      <h2>Research Areas</h2>
      <p class="research-brief">
        URIL is dedicated to advancing the development of intelligent robots
        that can be tailored to diverse end-user needs. To achieve this vision,
        our research focuses on two key areas:
      </p>
    </div>
    
    <div class="research-areas">
      <div class="research-area">
        <div class="research-media">
          <img src="/robot_skills.gif" alt="Robot performing manipulation skills" />
        </div>
        <div class="research-text">
          <h3>Improving Robot Skill Learning</h3>
          <p>
            We aim to improve the efficiency and adaptability of robots by
            enabling few-shot and zero-shot learning capabilities. Our
            approach includes developing structured learning frameworks such
            as novel action representations that facilitate efficient
            learning, and intermediate representations of motion that bridge
            visual representation and low-level motions.
          </p>
        </div>
      </div>

      <div class="research-area">
        <div class="research-media">
          <img src="/gestures.gif" alt="Human gestures and interaction modeling" />
        </div>
        <div class="research-text">
          <h3>Advancing Human Modeling</h3>
          <p>
            We draw inspiration from human interaction with the physical world
            and other agents to design learning algorithms that improve
            human-robot collaboration. Our efforts focus on designing
            algorithms that mirror how humans interact with the environment,
            and leverage multimodal human cues for human-robot interaction, in
            both shared and full autonomy settings.
          </p>
        </div>
      </div>
    </div>
  </Container>
</section>

<style>
  /* Hero section */
  .hero {
    padding: 50px 0 30px 0;
    background: linear-gradient(180deg, 
      rgba(68, 147, 207, 0.02) 0%, 
      rgba(255, 255, 255, 1) 100%);
    position: relative;
  }

  .hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, 
      transparent 0%, 
      rgba(68, 147, 207, 0.2) 50%, 
      transparent 100%);
  }

  .hero-content {
    opacity: 1;
    transform: translateY(0);
    transition: opacity 1.5s cubic-bezier(0.215, 0.61, 0.355, 1),
                transform 1.5s cubic-bezier(0.165, 0.84, 0.44, 1);
  }

  :global(html.js-enabled) .hero-content:not(.heading-visible) {
    opacity: 0;
    transform: translateY(30px);
  }

  .hero-image-wrapper {
    width: 100%;
    max-width: 900px;
    margin: 0 auto 35px auto;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(68, 147, 207, 0.15),
                0 2px 8px rgba(0, 0, 0, 0.1);
    position: relative;
  }

  .hero-image-wrapper::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: 12px;
    box-shadow: inset 0 0 0 1px rgba(68, 147, 207, 0.1);
    pointer-events: none;
  }

  .hero-image {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.4s ease;
  }

  .hero-image-wrapper:hover .hero-image {
    transform: scale(1.02);
  }

  .hero-description {
    max-width: 900px;
    margin: 0 auto;
    text-align: left;
    padding: 0 20px;
  }

  .hero-description p {
    font-size: 1.1rem;
    line-height: 1.85;
    color: #2d2d2d;
    margin: 0;
    font-weight: 400;
    letter-spacing: 0.01em;
  }

  @media (max-width: 768px) {
    .hero {
      padding: 40px 0 50px 0;
    }

    .hero-image-wrapper {
      margin-bottom: 30px;
      border-radius: 10px;
    }

    .hero-description {
      padding: 0 15px;
    }

    .hero-description p {
      font-size: 1rem;
      line-height: 1.75;
    }

    .research-areas {
      grid-template-columns: 1fr;
      gap: 30px;
    }

    .research-text h3 {
      font-size: 1.2rem;
    }

    .research-text p {
      font-size: 0.9rem;
    }
  }
  /* News section */
  .news {
    padding: 50px 0 40px 0;
    background-color: white;
    position: relative;
  }

  .news::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 80%;
    max-width: 900px;
    height: 1px;
    background: linear-gradient(90deg, 
      transparent 0%, 
      rgba(68, 147, 207, 0.15) 50%, 
      transparent 100%);
  }

  .news-header {
    max-width: 900px;
    margin: 0 auto 30px auto;
    padding: 0 20px;
    opacity: 1;
    transform: translateY(0);
    transition: opacity 1.5s cubic-bezier(0.215, 0.61, 0.355, 1),
                transform 1.5s cubic-bezier(0.165, 0.84, 0.44, 1);
  }

  :global(html.js-enabled) .news-header.section-heading:not(.heading-visible) {
    opacity: 0;
    transform: translateY(30px);
  }

  .news-header h2 {
    font-size: 2.25rem;
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 8px;
    letter-spacing: -0.03em;
    position: relative;
    display: inline-block;
  }

  .news-header h2::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 60px;
    height: 3px;
    background: linear-gradient(90deg, 
      var(--ucla-light-blue) 0%, 
      var(--ucla-dark-blue) 100%);
    border-radius: 2px;
  }

  .news-subtitle {
    font-size: 1.05rem;
    color: #666666;
    margin: 12px 0 0 0;
    font-weight: 400;
    letter-spacing: 0.01em;
  }

  .news-list {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .news-item {
    display: grid;
    grid-template-columns: 140px 1fr;
    gap: 40px;
    align-items: baseline;
    padding: 16px 0;
    line-height: 1.75;
    border-bottom: 1px solid rgba(68, 147, 207, 0.08);
    opacity: 1;
    transform: translateY(0);
    transition: opacity 1.2s cubic-bezier(0.215, 0.61, 0.355, 1),
                transform 1.2s cubic-bezier(0.165, 0.84, 0.44, 1),
                background-color 0.3s ease;
  }

  :global(html.js-enabled) .news-item:not(.in-view) {
    opacity: 0;
    transform: translateY(20px);
  }

  .news-item:hover {
    background-color: rgba(68, 147, 207, 0.02);
  }

  .news-item:last-child {
    border-bottom: none;
  }

  .news-date {
    color: #666666;
    font-size: 0.95rem;
    font-weight: 500;
    text-align: right;
    letter-spacing: 0.02em;
  }

  .news-description {
    font-size: 1.05rem;
    line-height: 1.75;
    text-align: left;
    color: #2d2d2d;
  }

  .news-description span {
    color: #2d2d2d;
  }

  .news-text-link {
    color: var(--ucla-light-blue);
    text-decoration: none;
    transition: all 0.2s ease;
    font-weight: 500;
    position: relative;
  }

  .news-text-link::after {
    content: '';
    position: absolute;
    bottom: -1px;
    left: 0;
    width: 0;
    height: 2px;
    background: linear-gradient(90deg, 
      var(--ucla-light-blue) 0%, 
      var(--ucla-dark-blue) 100%);
    transition: width 0.3s ease;
  }

  .news-text-link:hover {
    color: #2a7ab8;
  }

  .news-text-link:hover::after {
    width: 100%;
  }

  /* Research section */
  .research {
    padding: 50px 0 60px 0;
    background: linear-gradient(180deg, 
      rgba(255, 255, 255, 1) 0%, 
      rgba(68, 147, 207, 0.02) 100%);
    position: relative;
  }

  .research::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 80%;
    max-width: 900px;
    height: 1px;
    background: linear-gradient(90deg, 
      transparent 0%, 
      rgba(68, 147, 207, 0.15) 50%, 
      transparent 100%);
  }

  .research-header {
    max-width: 900px;
    margin: 0 auto 35px auto;
    padding: 0 20px;
    opacity: 1;
    transform: translateY(0);
    transition: opacity 1.5s cubic-bezier(0.215, 0.61, 0.355, 1),
                transform 1.5s cubic-bezier(0.165, 0.84, 0.44, 1);
  }

  :global(html.js-enabled) .research-header.section-heading:not(.heading-visible) {
    opacity: 0;
    transform: translateY(30px);
  }

  .research-header h2 {
    font-size: 2.25rem;
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 16px;
    letter-spacing: -0.03em;
    position: relative;
    display: inline-block;
  }

  .research-header h2::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 60px;
    height: 3px;
    background: linear-gradient(90deg, 
      var(--ucla-light-blue) 0%, 
      var(--ucla-dark-blue) 100%);
    border-radius: 2px;
  }

  .research-brief {
    font-size: 1.05rem;
    color: #666666;
    margin: 12px 0 0 0;
    line-height: 1.7;
    text-align: left;
    font-weight: 400;
    letter-spacing: 0.01em;
  }

  .research-areas {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 35px;
    max-width: 900px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .research-area {
    display: flex;
    flex-direction: column;
    gap: 20px;
    background: linear-gradient(135deg, 
      rgba(249, 249, 249, 1) 0%, 
      rgba(255, 255, 255, 1) 100%);
    border-radius: 16px;
    padding: 28px;
    box-shadow: 0 4px 16px rgba(68, 147, 207, 0.12),
                0 2px 4px rgba(0, 0, 0, 0.06);
    position: relative;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    opacity: 1;
    transform: translateY(0);
    border: 1px solid rgba(68, 147, 207, 0.08);
  }

  :global(html.js-enabled) .research-area:not(.in-view) {
    opacity: 0;
    transform: translateY(40px);
  }

  .research-area::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, 
      var(--ucla-light-blue) 0%, 
      var(--ucla-dark-blue) 100%);
    border-radius: 16px 16px 0 0;
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .research-area:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 24px rgba(68, 147, 207, 0.2),
                0 4px 8px rgba(0, 0, 0, 0.08);
  }

  .research-area:hover::before {
    opacity: 1;
  }

  .research-media {
    width: 100%;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    position: relative;
  }

  .research-media::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: 10px;
    box-shadow: inset 0 0 0 1px rgba(68, 147, 207, 0.1);
    pointer-events: none;
  }

  .research-media img {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.4s ease;
  }

  .research-area:hover .research-media img {
    transform: scale(1.05);
  }

  .research-text h3 {
    font-size: 1.4rem;
    font-weight: 600;
    color: #314062;
    margin: 0 0 14px 0;
    letter-spacing: -0.02em;
  }

  .research-text p {
    font-size: 1rem;
    line-height: 1.7;
    color: #333333;
    margin: 0;
    letter-spacing: 0.01em;
  }

  @media (max-width: 768px) {
    .news {
      padding: 40px 0 35px 0;
    }

    .news-header {
      margin-bottom: 25px;
      padding: 0 15px;
    }

    .news-header h2 {
      font-size: 2rem;
    }

    .news-subtitle {
      font-size: 1rem;
    }

    .news-list {
      padding: 0 15px;
    }

    .news-item {
      grid-template-columns: 1fr;
      gap: 8px;
      padding: 18px 0;
    }

    .news-date {
      font-size: 0.9rem;
      text-align: left;
      font-weight: 600;
      color: var(--ucla-light-blue);
    }

    .news-description {
      font-size: 1rem;
    }

    .research {
      padding: 40px 0 50px 0;
    }

    .research-header {
      margin-bottom: 30px;
      padding: 0 15px;
    }

    .research-header h2 {
      font-size: 2rem;
    }

    .research-brief {
      font-size: 1rem;
    }

    .research-areas {
      grid-template-columns: 1fr;
      gap: 25px;
      padding: 0 15px;
    }

    .research-area {
      padding: 24px;
    }

    .research-text h3 {
      font-size: 1.25rem;
    }

    .research-text p {
      font-size: 0.95rem;
    }
  }

  @media (max-width: 480px) {
    .news-header h2,
    .research-header h2 {
      font-size: 1.75rem;
    }

    .research-area {
      padding: 20px;
    }
  }
</style>