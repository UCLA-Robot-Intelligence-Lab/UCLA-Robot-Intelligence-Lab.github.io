<section class="content-section">
  <div class="container research-container">
    <h1 class="research-main-title">Research Areas</h1>

    <div class="research-intro">
      <div class="research-intro-content">
        <p>
          URIL is dedicated to advancing the development of intelligent robots
          that can be tailored to diverse end-user needs. To achieve this
          vision, our research focuses on two key areas:
        </p>
      </div>
    </div>

    <div class="research-areas">
      <div class="research-area">
        <div class="research-area-content">
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
          <div class="research-media">
            <div class="media-wrapper">
              <img
                src="/robot_skills.gif"
                alt="Robot performing manipulation skills"
              />
            </div>
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
  }

  .research-container {
    display: flex;
    flex-direction: column;
    gap: 4rem;
  }

  .research-main-title {
    text-align: center;
    margin-bottom: 2rem;
    font-size: 2.5rem;
    color: var(--heading-color);
    font-weight: 700;
    letter-spacing: -0.03em;
    position: relative;
    margin: 0 auto -2rem;
  }

  /* Removed underline for main research title */

  .research-intro {
    max-width: 900px;
    margin: 0 auto 2rem;
    padding: 2rem;
    background-color: var(--card-bg);
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    border: 1px solid var(--border-color);
  }

  .research-intro-content p {
    font-size: 1.25rem;
    line-height: 1.7;
    text-align: center;
    color: var(--text-color);
    margin: 0;
    font-weight: 400;
  }

  .research-areas {
    display: flex;
    flex-direction: column;
    gap: 4rem;
  }

  .research-area {
    width: 100%;
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
    gap: 2rem;
    align-items: center;
    padding: 0;
  }

  .research-text {
    flex: 1;
    padding: 2rem;
    background-color: var(--card-bg);
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    border: 1px solid rgba(68, 147, 207, 0.1); /* UCLA Light Blue with low opacity */
    transition:
      transform 0.4s ease,
      box-shadow 0.4s ease;
  }

  .research-text:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
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
      flex-direction: row;
    }

    .research-area:nth-child(even) .research-area-content {
      flex-direction: row-reverse;
    }

    .research-text,
    .research-media {
      width: calc(50% - 1rem);
    }
  }

  @media (max-width: 991px) {
    .research-main-title {
      font-size: 2.5rem;
    }

    .research-intro-content p {
      font-size: 1.15rem;
    }

    .research-text h2 {
      font-size: 1.8rem;
    }
  }

  @media (max-width: 767px) {
    .research-container {
      gap: 3rem;
    }

    .research-main-title {
      font-size: 2.2rem;
    }

    .research-intro {
      padding: 1.5rem;
    }

    .research-intro-content p {
      font-size: 1.1rem;
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
