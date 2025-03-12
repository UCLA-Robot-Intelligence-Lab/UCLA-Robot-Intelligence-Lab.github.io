<script lang="ts">
  // Define person interface
  interface Person {
    name: string;
    title: string;
    image: string;
    bio: string;
    website?: string;
  }
  // People data
  const people: { faculty: Person[]; grad_students: Person[]; undergrad_students: Person[] } = {
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
        name: "Metin Alp Dogan",
        title: "Master’s student",
        image: "/about-people/alp.jpg",
        bio: "Alp is a Master’s student in ECE, specializing in artificial intelligence, particularly inverse reinforcement learning techniques. He has research experience in control systems, optimization, and intelligent systems, with a focus on surgical robotics, and is a recipient of the Fulbright Scholarship. Alp enjoys snowboarding, hiking, and working out.",
        website: "https://www.linkedin.com/in/metinalpdogan/",
      },
      {
        name: "Soham Kulkarni",
        title: "Master’s student",
        image: "/generic_student.jpg",
        bio: "Soham is a Master’s student in ECE.",
        website: "/",
      },
    ],
    undergrad_students: [
      {
        name: "Tracey Tay",
        title: "Undergraduate Student",
        image: "/about-people/tracey-tay.jpg",
        bio: "Tracey is an exchange student from Imperial College London. She is passionate about the intersection of AI and robotics, with a particular focus on advancing intelligent systems. Her experience includes exploring innovative applications of natural language processing (NLP) and retrieval-augmented generation (RAG). Aside from academics, she enjoys being outdoors, doing a mixture of sports, music, cooking and getting to know people :)",
        website: "http://www.linkedin.com/in/traceytayyeehsin",
      },
      {
        name: "Raayan Dhar",
        title: "Sophomore, CS",
        image: "/about-people/raayan-dhar.jpg",
        bio: "Raayan is a sophomore in CS. He is interested in machine learning and deep learning broadly. He is especially interested in robotics, generative models, vision, and reinforcement learning. He is currently working on improving diffusion policies.",
        website: "https://raayandhar.github.io/",
      },
      {
        name: "Edward Sun",
        title: "Undergraduate Student",
        image: "/about-people/Edward Sun.jpg",
        bio: "Edward is interested in generative models for robotics. Specifically, he is interested in developing robotic agents that can interact with humans better using natural language. In his free time, he likes to do pencil sketches, listen to music, and snowboard",
        website: "https://edwardosunny.github.io/",
      },
      {
        name: "William Jiang",
        title: "Undergraduate Student, CSE",
        image: "/about-people/william-jiang.jpg",
        bio: "William is an undergraduate student pursuing a degree in Computer Science and Engineering at UCLA. His work centers on robot policy learning using gaze data from Meta's Aria glasses and innovative applications in computer vision. In addition to his academic pursuits, William designed and developed this website. He is also a member of UCLA's Division II hockey team.",
        website: "https://willjianger9.github.io/",
      },
      {
        name: "Jonathan Ouyang",
        title: "Undergraduate Student",
        image: "/about-people/jo-ouyang.jpg",
        bio: "Jonathan is an undergraduate student researching Computer Vision and its applications in Robot Policy Learning and Athletic Training. He previously worked with SJSU's AI/Deep Learning lab to utilize computer vision for swimmers in collaboration with the SJSU D1 swim team. He also won a $200k car from Google. In his free time, Jonathan likes to watch anime with Daniel and annoy William",
        website: "https://www.linkedin.com/in/jon-ouyang/",
      },
      {
        name: "Daniel Wu",
        title: "Undergraduate Student, CSE",
        image: "/about-people/daniel-wu.jpg",
        bio: "Daniel is an undergraduate studying CSE at UCLA and researching robot policy learning using computer vision. He is also on the UCLA Badminton Team. In his free time, he enjoys singing karaoke and watching anime with Jonathan and William.",
        website: "https://www.linkedin.com/in/danielwu06/",
      },
      {
        name: "Aadit Gupta",
        title: "Undergraduate Student, Computer Engineering",
        image: "/about-people/aadit.jpg",
        bio: "Aadit is an undergraduate studying Computer Engineering and is interested in robotics, the applications of natural language processing and computer vision. Aside from academics, he enjoys playing basketball, pickleball, and surfing.",
        website: "https://www.linkedin.com/in/aadit-gupta/",
      },
      {
        name: "Siddaarth Prasanna",
        title: "Sophomore, CS",
        image: "/about-people/siddaarth.jpg",
        bio: "Siddaarth is a current sophomore studying CS. He's interested in robot learning algorithms as well as deep learning in general. Outside of class, Siddaarth likes to run or sing!",
        website: "https://siddaarth.github.io/",
      },
      {
        name: "Yike Shi",
        title: "Sophomore, Computer Engineering",
        image: "/about-people/yike.jpg",
        bio: "Yike is a sophomore at UCLA majoring in Computer Engineering. He is deeply fascinated by both classical control and AI in robotics, with a focus on robotics learning, algorithms, and vision. His research interests also include exploring privacy and security challenges in AI models. Coming from Nanjing, China, Yike is skilled at cooking authentic Chinese cuisine and enjoys playing soccer and badminton.",
        website: "https://www.linkedin.com/in/yike-shi-996304264/",
      },
      {
        name: "Narek Germirlian",
        title: "Undergraduate Student, CS",
        image: "/about-people/Narek.png",
        bio: "Narek is an undergraduate student studying Computer Science at UCLA. His current research is focused on applications of computer vision, with additional interests in reinforcement learning and retrieval-augmented generation (RAG) models. Outside of research, Narek enjoys climbing, playing the piano, and spending time with family and friends.",
        website: "https://www.linkedin.com/in/narekgermirlian/",
      },
    ],
  };
</script>

<section class="content-section">
  <div class="container">
    <h1>People</h1>

    <h2>Faculty</h2>
    <div class="people-grid">
      {#each people.faculty as person}
        <a 
          href={person.website || '#'} 
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

    <h2>Graduate Students</h2>
    <div class="people-grid">
      {#each people.grad_students as person}
        <a 
          href={person.website || '#'} 
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

    <h2>Undergraduate Students</h2>
    <div class="people-grid">
      {#each people.undergrad_students as person}
        <a 
          href={person.website || '#'} 
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
  .people-grid {
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin-bottom: 50px;
    width: 100%;
  }

  .person-card {
    background-color: var(--card-bg);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
    transition:
      transform 0.3s ease-out,
      box-shadow 0.3s ease-out;
    text-decoration: none;
    color: var(--text-color);
    cursor: pointer;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 0;
    width: 100%;
    border: 1px solid var(--border-color);
  }

  .person-card.has-link:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
    background-color: var(--card-hover-bg);
  }
  
  .person-card.has-link::after {
    content: '';
    position: absolute;
    bottom: 12px;
    right: 12px;
    width: 20px;
    height: 20px;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23718096'%3E%3Cpath d='M5 3c-1.093 0-2 .907-2 2v14c0 1.093.907 2 2 2h14c1.093 0 2-.907 2-2v-7h-2v7H5V5h7V3H5zm9 0v2h3.586l-9.293 9.293 1.414 1.414L19 6.414V10h2V3h-7z'/%3E%3C/svg%3E");
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
  }

  .person-content {
    padding: 20px 30px;
    flex-grow: 1;
    max-width: calc(100% - 160px);
  }
  
  .person-card h3 {
    margin: 0 0 8px;
    font-size: 1.4rem;
    color: var(--heading-color);
  }

  .person-title {
    color: var(--secondary-text-color);
    font-style: italic;
    margin: 0 0 12px;
    font-size: 1rem;
  }

  .person-bio {
    margin: 0;
    font-size: 0.95rem;
    line-height: 1.5;
    color: var(--text-color);
  }



  @media (max-width: 768px) {
    .people-grid {
      gap: 16px;
    }
    
    .person-image {
      width: 140px;
      height: 140px;
    }
    
    .person-content {
      padding: 16px 20px;
      max-width: calc(100% - 140px);
    }
    
    .person-card h3 {
      font-size: 1.2rem;
    }
  }
  
  @media (max-width: 580px) {
    .person-card {
      flex-direction: column;
    }
    
    .person-image {
      width: 100%;
      height: 200px;
    }
    
    .person-content {
      padding: 20px;
      max-width: 100%;
    }
  }

  @media (max-width: 480px) {
    .people-grid {
      grid-template-columns: 1fr;
    }
  }
</style>
