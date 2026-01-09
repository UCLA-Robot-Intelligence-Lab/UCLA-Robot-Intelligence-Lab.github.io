<script lang="ts">
  import { onMount } from "svelte";
  import { fade, scale, fly } from "svelte/transition";
  

// People data
const people: PeopleData = {
    faculty: [
      {
        name: "Yuchen Cui",
        title: "Lab Director, Assistant Professor",
        image: "/about-people/yuchen-cui.jpg",
        bio: "Yuchen is an Assistant Professor in the Computer Science Department. Yuchen's research lies at the intersection of machine learning, robotics, and human-robot interaction. Her work focuses on developing algorithms, frameworks, and systems that facilitate efficient robot learning from human interactions.",
        website: "https://yuchencui.cc/",
        linkedin: "https://www.linkedin.com/in/yuchen-cui-4702a548/",
      },
    ],
    grad_students: [
      {
        name: "Xu Kristen Yan",
        title: "PhD student in ECE",
        image: "/about-people/xu.jpg",
        bio: "Xu is a PhD student in Electrical and Computer Engineering department. Her current research interests lie in leveraging physiological signals for seamless human-robot interactions. Outside of academics, she likes tennis, skating, and cooking.",
        linkedin: "https://www.linkedin.com/in/xukristenyan",
      },
      {
        name: "Omar Rayyan",
        title: "PhD student in CS",
        image: "/about-people/omar.jpg",
        bio: "Omar Rayyan is a first-year CS PhD student doing research at the intersection of machine learning and robotics. His work currently focuses on imitation learning and sim2real manipulation. Before joining the lab, Omar was an undergrad at NYU advised by Lerrel Pinto. Outside of research, he enjoys discovering new music and playing squash.",
        website: "https://orayyan.com/",
        linkedin: "https://www.linkedin.com/in/omar-rayyan/",
      },
      {
        name: "Maximilian Gilles",
        title: "Visiting Researcher (PhD student at KIT)",
        image: "/about-people/max.jpg",
        bio: "Maximilian Gilles is a doctoral researcher at the Karlsruhe Institute of Technology (KIT), specializing in robot perception and grasp learning. Currently, he is a visiting researcher at the URIL Lab (Fall Quarter 2025 - Winter Quarter 2026).",
        linkedin: "https://www.linkedin.com/in/maximilian-g1/",
      },
      {
        name: "Metin Alp Dogan",
        title: "Master’s student in ECE",
        image: "/about-people/alp.jpg",
        bio: "Alp is a Master’s student in ECE, specializing in artificial intelligence, particularly inverse reinforcement learning techniques. He has research experience in control systems, optimization, and intelligent systems, with a focus on surgical robotics, and is a recipient of the Fulbright Scholarship. Alp enjoys snowboarding, hiking, and working out.",
        linkedin: "https://www.linkedin.com/in/metinalpdogan/",
      },
      {
        name: "Yuanhong Zeng",
        title: "Master’s student in ECE",
        image: "/about-people/yuanhong.jpeg",
        bio: "Yuanhong a first-year master’s student in the ECE department with a passion for optimization, computer vision, and robot learning. His current research involves developing an embodiment-agnostic manipulation policy using 3D flow generation. Outside of my academic pursuits, he is also a professionally trained chef and he enjoys exploring new food.",
        linkedin: "https://www.linkedin.com/in/yuanhong-zeng/",
      },
    ],
    undergrad_students: [
     
      {
        name: "Raayan Dhar",
        title: "Undergraduate Student in CS",
        image: "/about-people/raayan-dhar.jpg",
        bio: "Raayan is an undergraduate studying computer science. He is especially interested in deep learning systems for the real world, in robotics or otherwise. In his free time, he enjoys hiking and running.",
        website: "https://raayandhar.github.io/",
        linkedin: "https://www.linkedin.com/in/raayan-dhar-4909051b1/",
      },
      {
        name: "Edward Sun",
        title: "Undergraduate Student in CS",
        image: "/about-people/Edward Sun.jpg",
        bio: "Edward is interested in generative models for robotics. Specifically, he is interested in developing robotic agents that can interact with humans better using natural language. In his free time, he likes to do pencil sketches, listen to music, and snowboard",
        website: "https://edwardosunny.github.io/",
        linkedin: "https://www.linkedin.com/in/edward-sun-208b73203/",
      },
      {
        name: "William Jiang",
        title: "Undergraduate Student in CSE",
        image: "/about-people/william-jiang.jpg",
        bio: "William is an undergraduate student pursuing a degree in Computer Science and Engineering at UCLA. His work centers on robot policy learning using gaze data from Meta's Aria glasses and innovative applications in computer vision. In addition to his academic pursuits, William designed and developed this website. He is also a member of UCLA's Division II hockey team.",
        website: "https://williamjiang.dev/",
        linkedin: "https://www.linkedin.com/in/williamjiang9/",
      },
      {
        name: "Jonathan Ouyang",
        title: "Undergraduate Student in CS",
        image: "/about-people/Jonathan.jpg",
        bio: "Jonathan is an undergraduate student researching Computer Vision and its applications in Robot Policy Learning and Athletic Training. He previously worked with SJSU's AI/Deep Learning lab to utilize computer vision for swimmers in collaboration with the SJSU D1 swim team. He also won a $200k car from Google. In his free time, Jonathan likes to watch anime with Daniel and annoy William",
        linkedin: "https://www.linkedin.com/in/jon-ouyang/",
      },
      {
        name: "Daniel Wu",
        title: "Undergraduate Student in CSE",
        image: "/about-people/daniel-wu.jpg",
        bio: "Daniel is an undergraduate studying CSE at UCLA and researching robot policy learning using computer vision. He is also on the UCLA Badminton Team. In his free time, he enjoys singing karaoke and watching anime with Jonathan and William.",
        website: "https://dwu006.github.io/",
        linkedin: "https://www.linkedin.com/in/danielwu06/",
      },
      {
        name: "Aadit Gupta",
        title: "Undergraduate Student in CE",
        image: "/about-people/aadit.jpg",
        bio: "Aadit is an undergraduate studying Computer Engineering and is interested in robotics, the applications of natural language processing and computer vision. Aside from academics, he enjoys playing basketball, pickleball, and surfing.",
        linkedin: "https://www.linkedin.com/in/aadit-gupta/",
      },
      {
        name: "Yike Shi",
        title: "Undergraduate Student in CE",
        image: "/about-people/yike.jpg",
        bio: "Yike is a sophomore at UCLA majoring in Computer Engineering. He is deeply fascinated by both classical control and AI in robotics, with a focus on robotics learning, algorithms, and vision. His research interests also include exploring privacy and security challenges in AI models. Coming from Nanjing, China, Yike is skilled at cooking authentic Chinese cuisine and enjoys playing soccer and badminton.",
        linkedin: "https://www.linkedin.com/in/yike-shi-996304264/",
      },
      {
        name: "Amit Rand",
        title: "Undergraduate Student in Math & CS",
        image: "/about-people/amit.jpg",
        bio: "Amit is a senior at UCLA majoring in Mathematics and Computer Science. His work focuses on imitation and reinforcement learning, with an emphasis on policy optimization for data-efficient robotic learning and zero-shot generalization. Outside of research, he enjoys cooking, reading, and climbing.",
        website: "https://amitsite.vercel.app/",
        linkedin: "https://www.linkedin.com/in/amit-rand-361b30218/",
     },
    ],
    alumni: [
      {
        name: "Soham Kulkarni",
        title: "Master’s student in CS",
        image: "/about-people/soham.jpg",
        bio: "Soham is a second-year Master's student in Computer Science with a background and broad interests in robot learning and perception. His current research focuses on developing efficient data quality metrics for imitation learning. Beyond research, he enjoys wildlife photography, swimming, martial arts, and hiking to recharge.",
        website: "https://stochasticritic.github.io/",
        linkedin: "https://www.linkedin.com/in/sohamkulkarni11/",
      },
       {
        name: "Tracey Tay",
        title: "Undergraduate Student in EE",
        image: "/about-people/tracey-tay.jpg",
        bio: "Tracey is an exchange student from Imperial College London. She is passionate about the intersection of AI and robotics, with a particular focus on advancing intelligent systems. Her experience includes exploring innovative applications of natural language processing (NLP) and retrieval-augmented generation (RAG). Aside from academics, she enjoys being outdoors, doing a mixture of sports, music, cooking and getting to know people :)",
        linkedin: "http://www.linkedin.com/in/traceytayyeehsin",
      },
    ]
    //collaborators: [
    //  {
    //   name: "Chenggong (Alex) Zhang",
    //    title: "PhD student in ECE",
     //   image: "/about-people/alex.jpg",
    //    bio: "Alex is a first year PhD student in ECE department from Yangtze River area, working on deep generative model and reinforcement learning. Currently, he is collaborating with Professor Cui on a project with policy learning for manipulation. Out of academia, he enjoys sprinting and listening to Spotify.",
    //    website: "https://www.linkedin.com/in/chenggong-zhang-1a3aa6252/",
    //  },
    //],
  };



  // State for detailed modal view
  let selectedPerson: Person | null = null;
  let modalOpen = false;

  // Add JS class to html element for animation support
  onMount(() => {
    document.documentElement.classList.add("js-enabled");
  });

  // Define person interface
  interface Person {
    name: string;
    title: string;
    image: string;
    bio?: string;
    website?: string;
    linkedin?: string;
  }

  // Define people data structure
  interface PeopleData {
    faculty: Person[];
    collaborators?: Person[];
    grad_students: Person[];
    undergrad_students: Person[];
    alumni: Person[];
  }

  // Animation with Intersection Observer
  // Define a variable to control whether animations should run
  let animationsEnabled = false;

  onMount(() => {
    // Set animations as enabled after component is mounted
    animationsEnabled = true;

    // Use Intersection Observer to trigger animations
    const options = {
      root: null,
      rootMargin: "0px",
      threshold: 0.15, // Slightly higher threshold to start animation when more of card is visible
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          // Add a subtle delay to create a staggered effect
          const delay = Math.random() * 250; // Extended random delay between 0-250ms for more staggered effect
          setTimeout(() => {
            entry.target.classList.add("in-view");
          }, delay);
          observer.unobserve(entry.target);
        }
      });
    }, options);

    // Observe all cards and section headings
    const cards = document.querySelectorAll(".person-card");
    cards.forEach((card) => {
      observer.observe(card);
    });

    // Observe section headings with a separate observer for just fade effect
    const headingOptions = {
      root: null,
      rootMargin: "0px",
      threshold: 0.5, // Higher threshold for headings
    };

    const headingObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("heading-visible");
          headingObserver.unobserve(entry.target);
        }
      });
    }, headingOptions);

    const headings = document.querySelectorAll(".section-heading");
    headings.forEach((heading) => {
      headingObserver.observe(heading);
    });
  });

  // Generate JSON-LD structured data for organization and team
  $: jsonLdData = {
    "@context": "https://schema.org",
    "@type": "ResearchOrganization",
    name: "UCLA Robot Intelligence Lab",
    url: "https://robot.cs.ucla.edu",
    logo: "https://robot.cs.ucla.edu/logo.png",
    member: [
      ...people.faculty.map((person) => ({
        "@type": "Person",
        name: person.name,
        jobTitle: person.title,
        image: `https://robot.cs.ucla.edu${person.image}`,
        url: person.website,
        worksFor: {
          "@type": "Organization",
          name: "UCLA Robot Intelligence Lab",
        },
      })),
      ...people.grad_students.map((person) => ({
        "@type": "Person",
        name: person.name,
        jobTitle: person.title,
        image: `https://robot.cs.ucla.edu${person.image}`,
        url: person.website,
      })),
      ...people.undergrad_students.map((person) => ({
        "@type": "Person",
        name: person.name,
        jobTitle: person.title,
        image: `https://robot.cs.ucla.edu${person.image}`,
        url: person.website,
      })),
      ...(people.collaborators ? people.collaborators.map((person) => ({
        "@type": "Person",
        name: person.name,
        jobTitle: person.title,
        image: `https://robot.cs.ucla.edu${person.image}`,
        url: person.website,
      })) : []),
      ...people.alumni.map((person) => ({
        "@type": "Person",
        name: person.name,
        jobTitle: person.title,
        image: `https://robot.cs.ucla.edu${person.image}`,
        url: person.website,
      })),
    ],
  };
</script>

<svelte:head>
  <script type="application/ld+json">
    {JSON.stringify(jsonLdData)}
  </script>
</svelte:head>

<section class="content-section">
  <div class="container people-container">
    <div class="title-container">
    <div class="title-wrapper">
      <h1 class="people-main-title">People</h1>
      <a href="/pictures" class="camera-icon-link" aria-label="View lab photo gallery">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="camera-icon">
          <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
          <circle cx="12" cy="13" r="4" />
        </svg>
      </a>
    </div>
  </div>

    <h2 class="section-heading">Faculty</h2>
    <div class="people-grid">
      {#each people.faculty as person}
        <button
          type="button"
          class="person-card clickable"
          on:click={() => {
            selectedPerson = person;
            modalOpen = true;
          }}
        >
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <h3>{person.name}</h3>
            <p class="person-title">{person.title}</p>
          </div>
        </button>
      {/each}
    </div>

    <h2 class="section-heading">Grad Students</h2>
    <div class="people-grid">
      {#each people.grad_students as person}
        <button
          type="button"
          class="person-card clickable"
          on:click={() => {
            selectedPerson = person;
            modalOpen = true;
          }}
        >
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <h3>{person.name}</h3>
            <p class="person-title">{person.title}</p>
          </div>
        </button>
      {/each}
    </div>

    <h2 class="section-heading">Undergrad Students</h2>
    <div class="people-grid">
      {#each people.undergrad_students as person}
        <button
          type="button"
          class="person-card clickable"
          on:click={() => {
            selectedPerson = person;
            modalOpen = true;
          }}
        >
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <h3>{person.name}</h3>
            <p class="person-title">{person.title}</p>
          </div>
        </button>
      {/each}
    </div>

    <h2 class="section-heading">Alumni</h2>
    <div class="people-grid">
      {#each people.alumni as person}
        <button
          type="button"
          class="person-card clickable"
          on:click={() => {
            selectedPerson = person;
            modalOpen = true;
          }}
        >
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <h3>{person.name}</h3>
            <p class="person-title">{person.title}</p>
          </div>
        </button>
      {/each}
    </div>
  </div>
</section>

<!-- Modal dialog -->
{#if modalOpen && selectedPerson}
  <div 
    class="modal-backdrop" 
    transition:fade={{ duration: 200 }}
    on:click={() => modalOpen = false}
    on:keydown={(e) => e.key === 'Escape' && (modalOpen = false)}
    role="presentation"
  ></div>
  
  <div 
    class="modal-container"
    transition:scale={{ duration: 300, start: 0.95 }}
    on:click={() => modalOpen = false}
    on:keydown={(e) => e.key === 'Escape' && (modalOpen = false)}
    role="presentation"
  >
    <div 
      class="modal-content" 
      on:click|stopPropagation
      on:keydown={(e) => e.key === 'Escape' && (modalOpen = false)}
      role="dialog"
      aria-labelledby="modal-title"
      tabindex="0"
    >
      <button class="modal-close" on:click={() => modalOpen = false} aria-label="Close modal">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
      
      <div class="modal-person-info">
        <div class="modal-person-image-container">
          <img 
            src={selectedPerson.image || "/placeholder.svg"}
            alt={selectedPerson.name || "Person profile"}
            class="modal-person-image"
          />
        </div>
        
        <div class="modal-person-details">
          <h2 id="modal-title" class="modal-person-name">{selectedPerson.name}</h2>
          <p class="modal-person-title">{selectedPerson.title}</p>
          
          {#if selectedPerson.bio}
            <div class="modal-person-bio">{selectedPerson.bio}</div>
          {/if}
          
          <div class="modal-person-links">
            {#if selectedPerson.website}
              <a 
                href={selectedPerson.website} 
                class="modal-person-link website-link"
                target="_blank"
                rel="noopener noreferrer"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="link-icon">
                  <circle cx="12" cy="12" r="10"></circle>
                  <line x1="2" y1="12" x2="22" y2="12"></line>
                  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                </svg>
                Personal Website
              </a>
            {/if}
            
            {#if selectedPerson.linkedin}
              <a 
                href={selectedPerson.linkedin} 
                class="modal-person-link linkedin-link"
                target="_blank"
                rel="noopener noreferrer"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="link-icon">
                  <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                  <rect x="2" y="9" width="4" height="12"></rect>
                  <circle cx="4" cy="4" r="2"></circle>
                </svg>
                LinkedIn
              </a>
            {/if}
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}

<style>
  /* People section */
  .title-container {
    text-align: center;
    margin-bottom: -0.5rem;
  }
  
  .title-wrapper {
    display: inline-flex;
    align-items: center;
    position: relative;
  }

  .people-main-title {
    margin-bottom: 0;
    margin-top: 0;
    font-size: 3rem;
    color: var(--heading-color);
    font-weight: 700;
    letter-spacing: -0.03em;
  }

  .camera-icon-link {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: 12px;
    opacity: 0.2;
    transition: opacity 0.3s ease, transform 0.3s ease;
  }

  .title-wrapper:hover .camera-icon-link {
    opacity: 1;
    transform: scale(1.1);
  }

  .camera-icon {
    width: 24px;
    height: 24px;
    color: var(--heading-color);
  }

  .content-section {
    padding: 2.5rem 0 4rem;
  }

  .people-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 4rem; /* Increased horizontal padding */
  }

  .people-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-bottom: 50px;
    width: 100%;
  }

  .person-card {
    background-color: var(--card-bg);
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    transition:
      transform 0.3s cubic-bezier(0.17, 0.67, 0.83, 0.67),
      box-shadow 0.3s ease-out,
      border-color 0.3s ease;
    color: var(--text-color);
    cursor: pointer;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0;
    width: 100%;
    height: 100%;
    border: 1px solid rgba(68, 147, 207, 0.1); /* UCLA Light Blue with low opacity */
    background: none;
    text-align: left;
    font-family: inherit;
    appearance: none;
  }

  /* Animation styles - applied to all person cards */
  .person-card {
    opacity: 1;
    transform: translateY(0);
    transition:
      opacity 1.6s cubic-bezier(0.215, 0.61, 0.355, 1),
      /* Ease-out-cubic with longer duration */ transform 1.8s
        cubic-bezier(0.165, 0.84, 0.44, 1),
      /* Ease-out-quart with longer duration */ box-shadow 0.3s ease-out,
      border-color 0.3s ease;
    will-change: transform, opacity; /* Optimize animation performance */
  }

  /* Apply the animation effect only when JavaScript is enabled */
  :global(html.js-enabled) .person-card:not(.in-view) {
    opacity: 0;
    transform: translateY(
      60px
    ); /* Increased distance for more pronounced effect */
  }

  /* Section heading animations - fade only */
  .section-heading {
    position: relative;
    margin-top: 2.5rem;
    margin-bottom: 1.5rem;
    font-size: 2.2rem;
    color: var(--heading-color); /* Uses UCLA Dark Blue from variables */
    font-weight: 600;
    transition: opacity 2s cubic-bezier(0.215, 0.61, 0.355, 1); /* Longer duration for smoother fade */
    opacity: 1;
  }

  :global(html.js-enabled) .section-heading:not(.heading-visible) {
    opacity: 0;
  }

  .person-card.clickable {
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .person-card.clickable:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12);
    border-color: #4493CF; /* UCLA Blue */
    background-color: rgba(68, 147, 207, 0.04); /* Very light UCLA blue background */
  }

  .person-image {
    width: 140px;
    height: 140px;
    object-fit: cover;
    flex-shrink: 0;
    border-radius: 50%;
    margin: 20px 20px 10px;
    border: 3px solid #fcd729; /* UCLA Yellow */
    box-shadow: 0 0 0 3px rgba(252, 215, 41, 0.2); /* UCLA Yellow glow */
    transition:
      transform 0.3s ease,
      box-shadow 0.3s ease;
    background-color: #f0f0f0; /* Light background for images with transparency */
  }

  .person-card:hover .person-image {
    transform: scale(1.05);
    box-shadow: 0 0 0 5px rgba(252, 215, 41, 0.3); /* UCLA Yellow glow */
  }

  .person-content {
    padding: 0 20px 20px;
    flex-grow: 1;
    width: 100%;
    text-align: center;
  }

  .person-card h3 {
    margin: 0 0 8px;
    font-size: 1.5rem;
    color: var(--heading-color);
    font-weight: 600;
    letter-spacing: -0.02em;
  }

  /* Person title styles */
  .person-title {
    color: #4493cf; /* UCLA Light Blue */
    font-style: italic;
    margin: 0 0 14px;
    font-size: 0.95rem;
    line-height: 1.5;
    font-weight: 500;
    position: relative;
    display: inline-block;
    max-width: 100%;
    margin-top: 0;
  }

  @media (max-width: 992px) {
    .people-grid {
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
    }
  }

  @media (max-width: 768px) {
    .person-image {
      width: 120px;
      height: 120px;
      margin: 16px 16px 10px;
    }

    .person-content {
      padding: 0 16px 16px;
    }

    .person-card h3 {
      font-size: 1.3rem;
    }

    .person-title {
      font-size: 1rem;
    }
  }

  @media (max-width: 580px) {
    .people-grid {
      grid-template-columns: 1fr;
    }

    .person-card {
      padding-bottom: 20px;
    }

    .person-image {
      width: 140px;
      height: 140px;
      margin: 20px 0 10px 0;
    }

    .person-content {
      padding: 0 20px 20px;
    }

    .person-title::after {
      left: 50%;
      transform: translateX(-50%);
    }

    /* External link icon removed */
  }

  @media (max-width: 480px) {
    .people-grid {
      gap: 16px;
    }

    .person-image {
      width: 140px;
      height: 140px;
    }

    .person-card h3 {
      font-size: 1.2rem;
    }
  }
  
  /* Modal Styles */
  .modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6);
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(4px);
  }
  
  .modal-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 101;
    padding: 20px;
  }
  
  .modal-content {
    background-color: var(--card-bg);
    border-radius: 18px;
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.18);
    max-width: 800px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
    border: 1px solid rgba(68, 147, 207, 0.2);
  }
  
  .modal-close {
    position: absolute;
    top: 15px;
    right: 15px;
    background: none;
    border: none;
    color: var(--text-color);
    opacity: 0.7;
    cursor: pointer;
    padding: 8px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
    z-index: 5;
    background-color: rgba(255, 255, 255, 0.8);
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
  }
  
  .modal-close:hover {
    opacity: 1;
    transform: scale(1.1);
    background-color: white;
  }
  
  .modal-person-info {
    display: flex;
    flex-direction: column;
    padding: 30px;
  }
  
  .modal-person-image-container {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
  }
  
  .modal-person-image {
    width: 180px;
    height: 180px;
    object-fit: cover;
    border-radius: 50%;
    border: 4px solid #fcd729;
    box-shadow: 0 0 0 4px rgba(252, 215, 41, 0.2);
  }
  
  .modal-person-details {
    text-align: center;
  }
  
  .modal-person-name {
    font-size: 2rem;
    margin: 0 0 10px;
    color: var(--heading-color);
    font-weight: 600;
  }
  
  .modal-person-title {
    color: #4493cf;
    font-size: 1.2rem;
    margin: 0 0 20px;
    font-style: italic;
    font-weight: 500;
  }
  
  .modal-person-bio {
    line-height: 1.6;
    color: var(--text-color);
    margin-bottom: 25px;
    text-align: left;
  }
  
  .modal-person-links {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 20px;
  }

  .modal-person-link {
    display: inline-flex;
    align-items: center;
    font-weight: 500;
    text-decoration: none;
    padding: 8px 16px;
    border-radius: 30px;
    transition: all 0.2s ease;
    gap: 8px;
  }

  .website-link, .linkedin-link {
    color: #4493cf; /* UCLA Blue */
    border: 2px solid #4493cf;
  }
  
  .website-link:hover, .linkedin-link:hover {
    background-color: #4493cf;
    color: white;
  }
  
  .link-icon {
    transition: transform 0.2s ease;
  }
  
  .modal-person-link:hover .link-icon {
    transform: translateX(2px);
  }
  
  @media (min-width: 768px) {
    .modal-person-info {
      flex-direction: row;
      align-items: center; /* Center items vertically */
    }
    
    .modal-person-image-container {
      margin-right: 30px;
      margin-bottom: 0;
      display: flex;
      align-items: center; /* Center image vertically */
    }
    
    .modal-person-details {
      text-align: left;
      flex: 1;
    }
  }
  
  @media (max-width: 480px) {
    .modal-content {
      padding: 20px;
    }
    
    .modal-person-image {
      width: 140px;
      height: 140px;
    }
    
    .modal-person-name {
      font-size: 1.6rem;
    }
  }
</style>