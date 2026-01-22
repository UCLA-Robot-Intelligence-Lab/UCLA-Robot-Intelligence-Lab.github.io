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
        name: "Xu Yan",
        title: "PhD student in CS",
        image: "/about-people/xu.jpg",
        bio: "Xu is a PhD student in Computer Science, co-advised by Professor Yuchen Cui and Professor Jonathan Kao. Her research focuses on making human-robot collaboration feel as natural and effortless as working with a trusted teammate, particularly by leveraging physiological signals for seamless human-robot interaction. Outside of academics, she enjoys tennis, skating, and cooking.",
        website: "https://web.cs.ucla.edu/~xkyan3/",
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
    ],
    masters_students: [
      {
        name: "Metin Alp Dogan",
        title: "Master's student in ECE",
        image: "/about-people/alp.jpg",
        bio: "Alp is a Master's student in ECE, specializing in artificial intelligence, particularly inverse reinforcement learning techniques. He has research experience in control systems, optimization, and intelligent systems, with a focus on surgical robotics, and is a recipient of the Fulbright Scholarship. Alp enjoys snowboarding, hiking, and working out.",
        linkedin: "https://www.linkedin.com/in/metinalpdogan/",
      },
      {
        name: "Yuanhong Zeng",
        title: "Master's student in ECE",
        image: "/about-people/yuanhong.jpeg",
        bio: "Yuanhong a first-year master's student in the ECE department with a passion for optimization, computer vision, and robot learning. His current research involves developing an embodiment-agnostic manipulation policy using 3D flow generation. Outside of my academic pursuits, he is also a professionally trained chef and he enjoys exploring new food.",
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
        website: "https://yik3.github.io/Yike-Shi.github.io/",
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

  // Robots data
  const robots = [
    {
      name: "xArm",
      image: "/about-people/xarm.png"
    },
    {
      name: "Bimanual Robot",
      image: "/about-people/bimanual.png"
    },
    {
      name: "Humanoid Robot",
      image: "/about-people/humanoid.png"
    }
  ];

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
    masters_students: Person[];
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
    <h1 class="page-title">People</h1>
    <h2 class="section-heading">Faculty Members</h2>
    <div class="people-list">
      {#each people.faculty as person}
        <div class="person-item">
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <div class="person-header">
              <h3 class="person-name">{person.name}</h3>
              <div class="person-social-icons">
                {#if person.website}
                  <a href={person.website} target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="Website">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="12" r="10"></circle>
                      <line x1="2" y1="12" x2="22" y2="12"></line>
                      <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                    </svg>
                  </a>
                {/if}
                {#if person.linkedin}
                  <a href={person.linkedin} target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="LinkedIn">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                      <rect x="2" y="9" width="4" height="12"></rect>
                      <circle cx="4" cy="4" r="2"></circle>
                    </svg>
                  </a>
                {/if}
              </div>
            </div>
            <p class="person-bio">{person.bio || ''}</p>
          </div>
        </div>
      {/each}
    </div>

    <h2 class="section-heading">PhD Students</h2>
    <div class="people-list">
      {#each people.grad_students as person}
        <div class="person-item" id={person.name.toLowerCase().replace(/\s+/g, '-')}>
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <div class="person-header">
              <h3 class="person-name">{person.name}</h3>
              <div class="person-social-icons">
                {#if person.website}
                  <a href={person.website} target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="Website">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="12" r="10"></circle>
                      <line x1="2" y1="12" x2="22" y2="12"></line>
                      <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                    </svg>
                  </a>
                {/if}
                {#if person.linkedin}
                  <a href={person.linkedin} target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="LinkedIn">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                      <rect x="2" y="9" width="4" height="12"></rect>
                      <circle cx="4" cy="4" r="2"></circle>
                    </svg>
                  </a>
                {/if}
              </div>
            </div>
            <p class="person-bio">{person.bio || ''}</p>
          </div>
        </div>
      {/each}
    </div>

    <h2 class="section-heading">Masters Students</h2>
    <div class="people-list">
      {#each people.masters_students as person}
        <div class="person-item">
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <div class="person-header">
              <h3 class="person-name">{person.name}</h3>
              <div class="person-social-icons">
                {#if person.website}
                  <a href={person.website} target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="Website">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="12" r="10"></circle>
                      <line x1="2" y1="12" x2="22" y2="12"></line>
                      <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                    </svg>
                  </a>
                {/if}
                {#if person.linkedin}
                  <a href={person.linkedin} target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="LinkedIn">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                      <rect x="2" y="9" width="4" height="12"></rect>
                      <circle cx="4" cy="4" r="2"></circle>
                    </svg>
                  </a>
                {/if}
              </div>
            </div>
            <p class="person-bio">{person.bio || ''}</p>
          </div>
        </div>
      {/each}
    </div>

    <h2 class="section-heading">Undergraduate Students</h2>
    <div class="people-list">
      {#each people.undergrad_students as person}
        <div class="person-item">
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <div class="person-header">
              <h3 class="person-name">{person.name}</h3>
              <div class="person-social-icons">
                {#if person.website}
                  <a href={person.website} target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="Website">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="12" r="10"></circle>
                      <line x1="2" y1="12" x2="22" y2="12"></line>
                      <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                    </svg>
                  </a>
                {/if}
                {#if person.linkedin}
                  <a href={person.linkedin} target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="LinkedIn">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                      <rect x="2" y="9" width="4" height="12"></rect>
                      <circle cx="4" cy="4" r="2"></circle>
                    </svg>
                  </a>
                {/if}
              </div>
            </div>
            <p class="person-bio">{person.bio || ''}</p>
          </div>
        </div>
      {/each}
    </div>

    <h2 class="section-heading">Alumni</h2>
    <div class="people-list">
      {#each people.alumni as person}
        <div class="person-item">
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <div class="person-header">
              <h3 class="person-name">{person.name}</h3>
              <div class="person-social-icons">
                {#if person.website}
                  <a href={person.website} target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="Website">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="12" r="10"></circle>
                      <line x1="2" y1="12" x2="22" y2="12"></line>
                      <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                    </svg>
                  </a>
                {/if}
                {#if person.linkedin}
                  <a href={person.linkedin} target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="LinkedIn">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                      <rect x="2" y="9" width="4" height="12"></rect>
                      <circle cx="4" cy="4" r="2"></circle>
                    </svg>
                  </a>
                {/if}
              </div>
            </div>
            <p class="person-bio">{person.bio || ''}</p>
          </div>
        </div>
      {/each}
    </div>

    <h2 class="section-heading">Robots</h2>
    <div class="robots-grid">
      {#each robots as robot}
        <div class="robot-item">
          <img
            src={robot.image}
            alt={robot.name}
            class="robot-image"
          />
          <p class="robot-name">{robot.name}</p>
        </div>
      {/each}
    </div>
  </div>
</section>


<style>
  .content-section {
    padding: 30px 0 80px;
    background-color: white;
  }

  .people-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .page-title {
    font-size: 2.5rem;
    font-weight: 600;
    color: #1a1a1a;
    margin: 0 0 30px 0;
    letter-spacing: -0.02em;
  }

  .section-heading {
    font-size: 1.5rem;
    font-weight: 600;
    color: #1a1a1a;
    margin: 40px 0 20px 0;
  }

  .section-heading:first-of-type {
    margin-top: 0;
  }

  .people-list {
    display: flex;
    flex-direction: column;
    gap: 30px;
    margin-bottom: 40px;
  }

  .person-item {
    display: flex;
    gap: 20px;
    align-items: flex-start;
    scroll-margin-top: 100px;
  }

  .person-image {
    width: 120px;
    height: 120px;
    border-radius: 8px;
    object-fit: cover;
    flex-shrink: 0;
  }

  .person-content {
    flex: 1;
  }

  .person-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 4px;
  }

  .person-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: #4493CF;
    margin: 0;
  }

  .person-social-icons {
    display: flex;
    gap: 6px;
  }

  .social-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background-color: #4493CF;
    color: white;
    transition: background-color 0.2s ease;
  }

  .social-icon svg {
    width: 14px;
    height: 14px;
  }

  .social-icon:hover {
    background-color: #2a7ab8;
  }

  .person-bio {
    font-size: 0.95rem;
    line-height: 1.6;
    color: #333333;
    margin: 0;
  }

  .robots-grid {
    display: flex;
    gap: 30px;
    margin-bottom: 40px;
    flex-wrap: wrap;
  }

  .robot-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
  }

  .robot-image {
    width: 120px;
    height: 120px;
    border-radius: 8px;
    object-fit: cover;
  }

  .robot-name {
    font-size: 0.95rem;
    font-weight: 500;
    color: #1a1a1a;
    margin: 0;
    text-align: center;
  }

  @media (max-width: 768px) {
    .section-heading {
      font-size: 1.3rem;
      margin: 35px 0 18px 0;
    }

    .person-item {
      gap: 16px;
    }

    .person-image {
      width: 100px;
      height: 100px;
    }

    .person-name {
      font-size: 1.05rem;
    }

    .person-bio {
      font-size: 0.9rem;
    }
  }

  @media (max-width: 480px) {
    .person-item {
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    .person-header {
      justify-content: center;
    }
  }
</style>