<script lang="ts">
  import { onMount } from "svelte";
  import { fade } from "svelte/transition";

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
        website: "https://yuchencui.cc/",
      },
    ],
    grad_students: [
      {
        name: "Xu Kristen Yan",
        title: "PhD student in ECE",
        image: "/about-people/xu.jpg",
        website: "https://www.linkedin.com/in/xukristenyan",
      },
      {
        name: "Metin Alp Dogan",
        title: "Master’s student in ECE",
        image: "/about-people/alp.jpg",
        website: "https://www.linkedin.com/in/metinalpdogan/",
      },
      
      {
        name: "Yuanhong Zeng",
        title: "Master’s student in ECE",
        image: "/about-people/yuanhong.jpeg",
        website: "https://www.linkedin.com/in/yuanhong-zeng/",
      },
    ],
    undergrad_students: [
     
      {
        name: "Raayan Dhar",
        title: "Undergraduate Student in CS",
        image: "/about-people/raayan-dhar.jpg",
        website: "https://raayandhar.github.io/",
      },
      {
        name: "Edward Sun",
        title: "Undergraduate Student in CS",
        image: "/about-people/Edward Sun.jpg",
        website: "https://edwardosunny.github.io/",
      },
      {
        name: "William Jiang",
        title: "Undergraduate Student in CSE",
        image: "/about-people/william-jiang.jpg",
        website: "https://willjianger9.github.io/",
      },
      {
        name: "Jonathan Ouyang",
        title: "Undergraduate Student in CS",
        image: "/about-people/Jonathan.jpg",
        website: "https://www.linkedin.com/in/jon-ouyang/",
      },
      {
        name: "Daniel Wu",
        title: "Undergraduate Student in CSE",
        image: "/about-people/daniel-wu.jpg",
        website: "https://www.linkedin.com/in/danielwu06/",
      },
      {
        name: "Aadit Gupta",
        title: "Undergraduate Student in CE",
        image: "/about-people/aadit.jpg",
        website: "https://www.linkedin.com/in/aadit-gupta/",
      },
      {
        name: "Yike Shi",
        title: "Undergraduate Student in CE",
        image: "/about-people/yike.jpg",
        website: "https://www.linkedin.com/in/yike-shi-996304264/",
      },
    ],
    alumni: [
      {
        name: "Soham Kulkarni",
        title: "Master’s student in CS",
        image: "/about-people/soham.jpg",
        website: "https://stochasticritic.github.io/",
      },
       {
        name: "Tracey Tay",
        title: "Undergraduate Student in EE",
        image: "/about-people/tracey-tay.jpg",
        website: "http://www.linkedin.com/in/traceytayyeehsin",
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
    text-decoration: none;
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

  .person-title {
    color: #4493cf; /* UCLA Light Blue */
    font-style: italic;
    margin: 0 0 14px;
    font-size: 1.05rem;
    font-weight: 500;
    position: relative;
    display: inline-block;
    max-width: 100%;
  }

  /* Removed underline for person-title */

  .person-bio {
    margin: 0;
    font-size: 0.95rem;
    line-height: 1.5;
    color: var(--text-color);
    /* Removed truncation properties to show full bio text */
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
