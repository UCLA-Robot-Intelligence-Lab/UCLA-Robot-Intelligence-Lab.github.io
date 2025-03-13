<script>
  import { onMount } from "svelte";

  // Set up intersection observer for animation on page load
  onMount(() => {
    // Add js-enabled class to html element
    if (typeof document !== "undefined") {
      document.documentElement.classList.add("js-enabled");
      document.documentElement.classList.remove("no-js");
    }

    // Create observer to detect when research areas come into view
    const options = {
      root: null,
      rootMargin: "0px",
      threshold: 0.15, // Element is 15% visible before animating
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          // Add a subtle delay to create a staggered effect
          const delay = Math.random() * 250; // Random delay between 0-250ms
          setTimeout(() => {
            entry.target.classList.add("in-view");
          }, delay);

          // Once animated, no need to observe anymore
          observer.unobserve(entry.target);
        }
      });
    }, options);

    // Observe all research areas
    const researchAreas = document.querySelectorAll(".research-area");
    researchAreas.forEach((area) => {
      observer.observe(area);
    });

    // Observe the main title with a higher threshold
    const headingOptions = {
      root: null,
      rootMargin: "0px",
      threshold: 0.5, // Higher threshold for heading
    };

    const headingObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("heading-visible");
          headingObserver.unobserve(entry.target);
        }
      });
    }, headingOptions);

    const heading = document.querySelector(".research-main-title");
    if (heading) {
      headingObserver.observe(heading);
    }

    const brief = document.querySelector(".research-brief");
    if (brief) {
      headingObserver.observe(brief);
    }
  });
</script>

<section class="content-section">
  <div class="container research-container">
    <div class="heading-group">
      <h1 class="research-main-title">Research Areas</h1>
      <p class="research-brief">
        URIL is dedicated to advancing the development of intelligent robots
        that can be tailored to diverse end-user needs. To achieve this vision,
        our research focuses on two key areas:
      </p>
    </div>
    <div class="research-areas">
      <div class="research-area">
        <div class="research-area-content">
          <div class="research-media">
            <div class="media-wrapper">
              <img
                src="/robot_skills.gif"
                alt="Robot performing manipulation skills"
              />
            </div>
          </div>
          <div class="research-text">
            <h2>Improving Robot Skill Learning</h2>
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
      </div>

      <div class="research-area">
        <div class="research-area-content">
          <div class="research-media">
            <div class="media-wrapper">
              <img
                src="/gestures.gif"
                alt="Human gestures and interaction modeling"
              />
            </div>
          </div>
          <div class="research-text">
            <h2>Advancing Human Modeling</h2>
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
    </div>
  </div>
</section>

<style>
  .content-section {
    padding: 4rem 0;
  }

  .research-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 4rem; /* Increased horizontal padding */
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .heading-group {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 0.5rem;
  }

  .research-main-title {
    text-align: center;
    font-size: 3rem;
    color: var(--heading-color);
    font-weight: 700;
    letter-spacing: -0.03em;
    position: relative;
    margin: 0 0 0.25rem;
    transition: opacity 2s cubic-bezier(0.215, 0.61, 0.355, 1); /* Smooth fade-in */
    opacity: 1;
  }
  
  /* No specific dark mode styles for research title - using default dark mode heading color */

  /* Heading animation */
  :global(html.js-enabled) .research-main-title:not(.heading-visible) {
    opacity: 0;
  }

  :global(html.no-js) .research-main-title {
    opacity: 1;
  }

  /* Removed underline for main research title */

  .research-brief {
    max-width: 700px;
    margin: 0 0 0.5rem 0;
    padding: 0;
    font-size: 0.9rem;
    line-height: 1.4;
    text-align: center;
    color: var(--text-color-secondary, rgba(100, 100, 100, 0.85));
    font-weight: 400;
    font-style: italic;
    transition:
      opacity 1.8s cubic-bezier(0.215, 0.61, 0.355, 1),
      transform 1.6s cubic-bezier(0.165, 0.84, 0.44, 1);
    opacity: 1;
    transform: translateY(0);
  }
  
  /* Dark mode styles for research brief */
  :global(html.dark-mode) .research-brief {
    color: rgba(255, 255, 255, 0.9);
  }

  :global(html.js-enabled) .research-brief:not(.heading-visible) {
    opacity: 0;
    transform: translateY(30px);
  }

  :global(html.no-js) .research-brief {
    opacity: 1;
    transform: translateY(0);
  }

  .research-areas {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 2rem;
    justify-content: space-between;
    margin-top: 0.75rem;
  }

  .research-area {
    flex: 1 1 48%;
    min-width: 300px;
    border-radius: 16px;
    overflow: hidden;
    transition:
      transform 0.3s ease,
      box-shadow 0.3s ease,
      opacity 1.6s cubic-bezier(0.215, 0.61, 0.355, 1);
    opacity: 1;
    transform: translateY(0);
  }

  /* Apply the animation effect only when JavaScript is enabled */
  :global(html.js-enabled) .research-area:not(.in-view) {
    opacity: 0;
    transform: translateY(
      60px
    ); /* Increased distance for more pronounced effect */
  }

  .research-area:hover {
    transform: translateY(
      -5px
    ) !important; /* Important to override animation transform */
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  }

  .research-area:nth-child(1) {
    --index: 1;
  }

  .research-area:nth-child(2) {
    --index: 2;
  }

  .research-area-content {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    align-items: center;
    padding: 1.5rem;
    height: 100%;
    background-color: var(--card-bg);
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    border: 1px solid rgba(68, 147, 207, 0.1); /* UCLA Light Blue with low opacity */
  }

  .research-text {
    flex: 1;
    padding: 1.5rem 0 0.5rem;
    width: 100%;
  }

  .research-text h2 {
    font-size: 2rem;
    color: var(--heading-color);
    margin: 0 0 1.5rem;
    position: relative;
    font-weight: 600;
    letter-spacing: -0.5px;
  }

  /* Removed underline for research area titles */

  .research-text p {
    font-size: 1.1rem;
    line-height: 1.8;
    color: var(--text-color);
    margin: 0;
  }

  .research-media {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .media-wrapper {
    width: 100%;
    max-width: 480px;
    height: auto;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
    transition: transform 0.4s ease;
    border: 1px solid var(--border-color);
  }

  .media-wrapper:hover {
    transform: scale(1.03);
  }

  .media-wrapper img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
  }

  /* Responsive styles */
  @media (min-width: 992px) {
    .research-area-content {
      flex-direction: column;
    }

    .research-text,
    .research-media {
      width: 100%;
    }

    .research-media {
      max-height: 300px;
      overflow: hidden;
    }
  }

  @media (max-width: 991px) {
    .research-main-title {
      font-size: 2.5rem;
    }

    .research-text h2 {
      font-size: 1.8rem;
    }

    .research-areas {
      flex-direction: column;
    }

    .research-area {
      flex: 1 1 100%;
    }
  }

  @media (max-width: 767px) {
    .research-container {
      gap: 3rem;
    }

    .research-main-title {
      font-size: 2.2rem;
    }

    .research-text {
      padding: 1.5rem;
    }

    .research-text h2 {
      font-size: 1.6rem;
    }

    .research-text p {
      font-size: 1rem;
    }
  }
</style>
