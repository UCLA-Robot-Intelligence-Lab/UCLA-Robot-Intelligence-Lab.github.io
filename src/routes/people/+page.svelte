<script lang="ts">
  import { onMount } from "svelte";

  // Add JS class to html element for animation support
  onMount(() => {
    document.documentElement.classList.add("js-enabled");
  });

  // Define person interface
  interface Person {
    name: string;
    title: string;
    image: string;
    bio: string;
    website?: string;
  }

  // Define people data structure
  interface PeopleData {
    faculty: Person[];
    collaborators: Person[];
    grad_students: Person[];
    undergrad_students: Person[];
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
  // People data
  const people: PeopleData = {
    faculty: [
      {
        name: "Yuchen Cui",
        title: "Lab Director, Assistant Professor",
        image: "/about-people/yuchen-cui.jpg",
        bio: "Yuchen is an Assistant Professor in the Computer Science Department. Yuchen's research lies at the intersection of machine learning, robotics, and human-robot interaction. Her work focuses on developing algorithms, frameworks, and systems that facilitate efficient robot learning from human interactions.",
        website: "https://yuchencui.cc/",
      },
    ],
    grad_students: [
      {
        name: "Xu Kristen Yan",
        title: "PhD student in ECE",
        image: "/about-people/xu.jpg",
        bio: "Xu is a PhD student in Electrical and Computer Engineering department. Her current research interests lie in leveraging physiological signals for seamless human-robot interactions. Outside of academics, she likes tennis, skating, and cooking.",
        website: "https://www.linkedin.com/in/xukristenyan",
      },
      {
        name: "Metin Alp Dogan",
        title: "Master’s student in ECE",
        image: "/about-people/alp.jpg",
        bio: "Alp is a Master’s student in ECE, specializing in artificial intelligence, particularly inverse reinforcement learning techniques. He has research experience in control systems, optimization, and intelligent systems, with a focus on surgical robotics, and is a recipient of the Fulbright Scholarship. Alp enjoys snowboarding, hiking, and working out.",
        website: "https://www.linkedin.com/in/metinalpdogan/",
      },
      {
        name: "Soham Kulkarni",
        title: "Master’s student in CS",
        image: "/about-people/soham.jpg",
        bio: "Soham is a second-year Master's student in Computer Science with a background and broad interests in robot learning and perception. His current research focuses on developing efficient data quality metrics for imitation learning. Beyond research, he enjoys wildlife photography, swimming, martial arts, and hiking to recharge.",
        website: "https://stochasticritic.github.io/",
      },
      {
        name: "Yuanhong Zeng",
        title: "Master’s student in ECE",
        image: "/about-people/yuanhong.jpeg",
        bio: "Yuanhong a first-year master’s student in the ECE department with a passion for optimization, computer vision, and robot learning. His current research involves developing an embodiment-agnostic manipulation policy using 3D flow generation. Outside of my academic pursuits, he is also a professionally trained chef and he enjoys exploring new food.",
        website: "https://www.linkedin.com/in/yuanhong-zeng/",
      },
    ],
    undergrad_students: [
      {
        name: "Tracey Tay",
        title: "Undergraduate Student in EE",
        image: "/about-people/tracey-tay.jpg",
        bio: "Tracey is an exchange student from Imperial College London. She is passionate about the intersection of AI and robotics, with a particular focus on advancing intelligent systems. Her experience includes exploring innovative applications of natural language processing (NLP) and retrieval-augmented generation (RAG). Aside from academics, she enjoys being outdoors, doing a mixture of sports, music, cooking and getting to know people :)",
        website: "http://www.linkedin.com/in/traceytayyeehsin",
      },
      {
        name: "Raayan Dhar",
        title: "Undergraduate Student in CS",
        image: "/about-people/raayan-dhar.jpg",
        bio: "Raayan is a sophomore in CS. He is interested in machine learning and deep learning broadly. He is especially interested in robotics, generative models, vision, and reinforcement learning. He is currently working on improving diffusion policies.",
        website: "https://raayandhar.github.io/",
      },
      {
        name: "Edward Sun",
        title: "Undergraduate Student in CS",
        image: "/about-people/Edward Sun.jpg",
        bio: "Edward is interested in generative models for robotics. Specifically, he is interested in developing robotic agents that can interact with humans better using natural language. In his free time, he likes to do pencil sketches, listen to music, and snowboard",
        website: "https://edwardosunny.github.io/",
      },
      {
        name: "William Jiang",
        title: "Undergraduate Student in CSE",
        image: "/about-people/william-jiang.jpg",
        bio: "William is an undergraduate student pursuing a degree in Computer Science and Engineering at UCLA. His work centers on robot policy learning using gaze data from Meta's Aria glasses and innovative applications in computer vision. In addition to his academic pursuits, William designed and developed this website. He is also a member of UCLA's Division II hockey team.",
        website: "https://willjianger9.github.io/",
      },
      {
        name: "Jonathan Ouyang",
        title: "Undergraduate Student in CS",
        image: "/about-people/Jonathan.jpg",
        bio: "Jonathan is an undergraduate student researching Computer Vision and its applications in Robot Policy Learning and Athletic Training. He previously worked with SJSU's AI/Deep Learning lab to utilize computer vision for swimmers in collaboration with the SJSU D1 swim team. He also won a $200k car from Google. In his free time, Jonathan likes to watch anime with Daniel and annoy William",
        website: "https://www.linkedin.com/in/jon-ouyang/",
      },
      {
        name: "Daniel Wu",
        title: "Undergraduate Student in CSE",
        image: "/about-people/daniel-wu.jpg",
        bio: "Daniel is an undergraduate studying CSE at UCLA and researching robot policy learning using computer vision. He is also on the UCLA Badminton Team. In his free time, he enjoys singing karaoke and watching anime with Jonathan and William.",
        website: "https://www.linkedin.com/in/danielwu06/",
      },
      {
        name: "Aadit Gupta",
        title: "Undergraduate Student in CE",
        image: "/about-people/aadit.jpg",
        bio: "Aadit is an undergraduate studying Computer Engineering and is interested in robotics, the applications of natural language processing and computer vision. Aside from academics, he enjoys playing basketball, pickleball, and surfing.",
        website: "https://www.linkedin.com/in/aadit-gupta/",
      },
      {
        name: "Siddaarth Prasanna",
        title: "Undergraduate Student in CS",
        image: "/about-people/siddaarth.jpg",
        bio: "Siddaarth is a current sophomore studying CS. He's interested in robot learning algorithms as well as deep learning in general. Outside of class, Siddaarth likes to run or sing!",
        website: "https://siddaarth.github.io/",
      },
      {
        name: "Yike Shi",
        title: "Undergraduate Student in CE",
        image: "/about-people/yike.jpg",
        bio: "Yike is a sophomore at UCLA majoring in Computer Engineering. He is deeply fascinated by both classical control and AI in robotics, with a focus on robotics learning, algorithms, and vision. His research interests also include exploring privacy and security challenges in AI models. Coming from Nanjing, China, Yike is skilled at cooking authentic Chinese cuisine and enjoys playing soccer and badminton.",
        website: "https://www.linkedin.com/in/yike-shi-996304264/",
      },
      {
        name: "Narek Germirlian",
        title: "Undergraduate Student in CS",
        image: "/about-people/Narek.png",
        bio: "Narek is an undergraduate student studying Computer Science at UCLA. His current research is focused on applications of computer vision, with additional interests in reinforcement learning and retrieval-augmented generation (RAG) models. Outside of research, Narek enjoys climbing, playing the piano, and spending time with family and friends.",
        website: "https://www.linkedin.com/in/narekgermirlian/",
      },
    ],
    collaborators: [
      {
        name: "Chenggong (Alex) Zhang",
        title: "PhD student in ECE",
        image: "/about-people/alex.jpg",
        bio: "Alex is a first year PhD student in ECE department from Yangtze River area, working on deep generative model and reinforcement learning. Currently, he is collaborating with Professor Cui on a project with policy learning for manipulation. Out of academia, he enjoys sprinting and listening to Spotify.",
        website: "https://www.linkedin.com/in/chenggong-zhang-1a3aa6252/",
      },
    ],
  };

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
      ...people.collaborators.map((person) => ({
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
    <h1 class="people-main-title">People</h1>

    <h2 class="section-heading">Faculty</h2>
    <div class="people-grid">
      {#each people.faculty as person}
        <a
          href={person.website || "#"}
          target="_blank"
          rel="noopener noreferrer"
          class="person-card {person.website ? 'has-link' : ''}"
        >
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <h3>{person.name}</h3>
            <p class="person-title">{person.title}</p>
            <p class="person-bio">{person.bio}</p>
          </div>
        </a>
      {/each}
    </div>

    <h2 class="section-heading">Graduate Students</h2>
    <div class="people-grid">
      {#each people.grad_students as person}
        <a
          href={person.website || "#"}
          target="_blank"
          rel="noopener noreferrer"
          class="person-card {person.website ? 'has-link' : ''}"
        >
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <h3>{person.name}</h3>
            <p class="person-title">{person.title}</p>
            <p class="person-bio">{person.bio}</p>
          </div>
        </a>
      {/each}
    </div>

    <h2 class="section-heading">Undergraduate Students</h2>
    <div class="people-grid">
      {#each people.undergrad_students as person}
        <a
          href={person.website || "#"}
          target="_blank"
          rel="noopener noreferrer"
          class="person-card {person.website ? 'has-link' : ''}"
        >
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <h3>{person.name}</h3>
            <p class="person-title">{person.title}</p>
            <p class="person-bio">{person.bio}</p>
          </div>
        </a>
      {/each}
    </div>

    <h2 class="section-heading">Collaborators</h2>
    <div class="people-grid">
      {#each people.collaborators as person}
        <a
          href={person.website || "#"}
          target="_blank"
          rel="noopener noreferrer"
          class="person-card {person.website ? 'has-link' : ''}"
        >
          <img
            src={person.image || "/placeholder.svg"}
            alt={person.name}
            class="person-image"
          />
          <div class="person-content">
            <h3>{person.name}</h3>
            <p class="person-title">{person.title}</p>
            <p class="person-bio">{person.bio}</p>
          </div>
        </a>
      {/each}
    </div>
  </div>
</section>

<style>
  /* People section */
  .people-main-title {
    text-align: center;
    margin-bottom: -0.5rem;
    margin-top: 0;
    font-size: 3rem;
    color: var(--heading-color);
    font-weight: 700;
    letter-spacing: -0.03em;
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
    display: flex;
    flex-direction: column;
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
    text-decoration: none;
    color: var(--text-color);
    cursor: pointer;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 0;
    width: 100%;
    border: 1px solid rgba(68, 147, 207, 0.1); /* UCLA Light Blue with low opacity */
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

  .person-card.has-link:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.12);
    background-color: var(--card-hover-bg);
    border-color: rgba(
      68,
      147,
      207,
      0.3
    ); /* UCLA Light Blue with higher opacity on hover */
  }

  .person-card.has-link::after {
    content: "";
    position: absolute;
    bottom: 16px;
    right: 16px;
    width: 24px;
    height: 24px;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%234493CF'%3E%3Cpath d='M5 3c-1.093 0-2 .907-2 2v14c0 1.093.907 2 2 2h14c1.093 0 2-.907 2-2v-7h-2v7H5V5h7V3H5zm9 0v2h3.586l-9.293 9.293 1.414 1.414L19 6.414V10h2V3h-7z'/%3E%3C/svg%3E");
    background-size: contain;
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
  }

  .person-card.has-link:hover::after {
    opacity: 0.8;
  }

  .person-image {
    width: 160px;
    height: 160px;
    object-fit: cover;
    flex-shrink: 0;
    border-radius: 50%;
    margin: 20px;
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
    padding: 25px 30px;
    flex-grow: 1;
    max-width: calc(100% - 200px); /* Adjusted for new image size and margin */
  }

  .person-card h3 {
    margin: 0 0 8px;
    font-size: 1.5rem;
    color: var(--heading-color);
    font-weight: 600;
    letter-spacing: -0.02em;
  }

  .person-title {
    color: #4493cf; /* UCLA Light Blue */
    font-style: italic;
    margin: 0 0 14px;
    font-size: 1.05rem;
    font-weight: 500;
    position: relative;
    display: inline-block;
  }

  /* Removed underline for person-title */

  .person-bio {
    margin: 0;
    font-size: 1rem;
    line-height: 1.6;
    color: var(--text-color);
  }

  @media (max-width: 768px) {
    .people-grid {
      gap: 20px;
    }

    .person-image {
      width: 120px;
      height: 120px;
      margin: 16px;
    }

    .person-content {
      padding: 16px 20px;
      max-width: calc(
        100% - 152px
      ); /* Adjusted for new image size and margin */
    }

    .person-card h3 {
      font-size: 1.3rem;
    }

    .person-title {
      font-size: 1rem;
    }
  }

  @media (max-width: 580px) {
    .person-card {
      flex-direction: column;
      align-items: center;
      text-align: center;
      padding-bottom: 20px;
    }

    .person-image {
      width: 160px;
      height: 160px;
      margin: 30px 0 10px 0;
    }

    .person-content {
      padding: 10px 25px 25px;
      max-width: 100%;
    }

    .person-title::after {
      left: 50%;
      transform: translateX(-50%);
    }

    .person-card.has-link::after {
      bottom: 15px;
      right: 15px;
    }
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
</style>
