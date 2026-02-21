<script>
  import { onMount } from 'svelte';
  
  // Set up intersection observer for animation on page load
  onMount(() => {
    // Add js-enabled class to html element
    if (typeof document !== 'undefined') {
      document.documentElement.classList.add('js-enabled');
      document.documentElement.classList.remove('no-js');
    }
    
    // Create observer to detect when publications come into view
    const options = {
      root: null,
      rootMargin: '0px',
      threshold: 0.15 // Element is 15% visible before animating
    };
    
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Add a subtle delay to create a staggered effect
          const delay = Math.random() * 250; // Random delay between 0-250ms
          setTimeout(() => {
            entry.target.classList.add('in-view');
          }, delay);
          
          // Once animated, no need to observe anymore
          observer.unobserve(entry.target);
        }
      });
    }, options);
    
    // Observe all publication cards
    const publications = document.querySelectorAll('.publication-card');
    publications.forEach(pub => {
      observer.observe(pub);
    });
    
    // Observe the main title with a higher threshold
    const headingOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.5 // Higher threshold for heading
    };
    
    const headingObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('heading-visible');
          headingObserver.unobserve(entry.target);
        }
      });
    }, headingOptions);
    
    const heading = document.querySelector('.publications-title');
    if (heading) {
      headingObserver.observe(heading);
    }
  });
  
  // Publications
  const publications = [
    {
  title: "DiSCo: Diffusion Sequence Copilots for Shared Autonomy",
  authors:
    "Brandon McMahan, Andy Wang, Xu Yan, Michael Zhou, Yuyang Yuan, Johannes Y. Lee, Ali Shreif, Matthew Li, Zhenghao Peng, Bolei Zhou, Yuchen Cui, Jonathan C. Kao",
  venue:
    "ACM/IEEE International Conference on Human-Robot Interaction (HRI), 2026",
  links: [],
},
    {
  title:
    "Intent at a Glance: Gaze-Guided Robotic Manipulation via Foundation Models",
  authors:
    "Tracey Yee Hsin Tay, Xu Yan, Jonathan Ouyang, Daniel Wu, William Jiang, Jonathan Kao, Yuchen Cui",
  venue:
    "RSS 2025 Workshop on Robot Planning in the Era of Foundation Models, June 2025",
  links: [
    {
      text: "paper",
      url: "https://arxiv.org/abs/2601.05336",
      icon: "fa-file",
    },
    {
      text: "website",
      url: "https://gamma0.vercel.app/",
      icon: "fa-globe",
    },
  ],
},
{
  title: "TRACE: Textual Reasoning for Affordance Coordinate Extraction",
  authors: "Sangyun Park, Jin Kim, Yuchen Cui, Matthew S Brown",
  venue:
    "ICCV 2025 Knowledge-Intensive Multimodal Reasoning Workshop, Nov 2025",
  links: [
    {
      text: "paper",
      url: "https://arxiv.org/abs/2511.01999",
      icon: "fa-file",
    },
  ],
},
{
  title:
    "Casper: Inferring Diverse Intents for Assistive Teleoperation with Vision Language Models",
  authors:
    "Huihan Liu, Rutav Shah, Shuijing Liu, Jack Pittenger, Mingyo Seo, Yuchen Cui, Yonatan Bisk, Roberto Martín-Martín, Yuke Zhu",
  venue: "Conference on Robot Learning (CoRL), September 2025",
  links: [
    {
      text: "paper",
      url: "https://arxiv.org/abs/2506.14727",
      icon: "fa-file",
    },
  ],
},
{
  title:
    "GraphPad: Inference-Time 3D Scene Graph Updates for Embodied Question Answering",
  authors:
    "Muhammad Qasim Ali, Saeejith Nair, Alexander Wong, Yuchen Cui, Yuhao Chen",
  venue:
    "CVPR Workshop on 3D-LLM/VLA: Bridging Language, Vision and Action in 3D Environments, June 2025",
  links: [
    {
      text: "paper",
      url: "https://arxiv.org/abs/2506.01174",
      icon: "fa-file",
    },
  ],
},
{
  title:
    "SAMJAM: Zero-Shot Video Scene Graph Generation for Egocentric Kitchen Videos",
  authors:
    "Joshua Li, Fernando Jose Pena Cantu, Emily Yu, Alexander Wong, Yuchen Cui, Yuhao Chen",
  venue: "Computer Vision and Pattern Recognition Conference (CVPR) MetaFood Workshop, June 2025",
  links: [],
},

    {
      title:
        "Shared Autonomy for Proximal Teaching",
      authors: "Megha Srivastava, Reihaneh Iranmanesh, Yuchen Cui, Deepak Gopinath, Emily Sarah Sumner, Andrew Silva, Laporsha Dees, Guy Rosman, Dorsa Sadigh",
      venue:
        "ACM/IEEE International Conference on Human-Robot Interaction (HRI), Mar 2025",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2502.19899",
          icon: "fa-file",
        },
      ],
    },
    {
      title: 
        "How to Train Your Robots? The Impact of Demonstration Modality on Imitation Learning",
      authors: "Haozhuo Li, Yuchen Cui, Dorsa Sadigh",
      venue:
        "Proceedings of the International Conference on Robotics and Automation (ICRA), May 2025",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2503.07017",
          icon: "fa-file",
        },
      ],
    },
    {
      title:
        "FlowRetrieval: Flow-Guided Data Retrieval for Few-Shot Imitation Learning",
      authors: "Li-Heng Lin, Yuchen Cui, Amber Xie, Tianyu Hua, Dorsa Sadigh",
      venue:
        "Conference on Robot Learning (CoRL), November 2024",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2408.16944",
          icon: "fa-file",
        },
        {
          text: "website",
          url: "https://flow-retrieval.github.io/",
          icon: "fa-link",
        },
      ],
    },
    {
      title:
        "Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections",
      authors:
        "Lihan Zha, Yuchen Cui, Li-Heng Lin, Minae Kwon, Montserrat Gonzalez Arenas, Andy Zeng, Fei Xia, Dorsa Sadigh",
      venue:
        "International Conference on Robotics and Automation (ICRA), May 2024",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2311.10678",
          icon: "fa-file",
        },
        {
          text: "website",
          url: "https://sites.google.com/stanford.edu/droc",
          icon: "fa-link",
        },
      ],
    },
    {
      title: "Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
      authors: "Open X-Embodiment Collaboration",
      venue:
        "International Conference on Robotics and Automation (ICRA), May 2024",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2310.08864",
          icon: "fa-file",
        },
        {
          text: "website",
          url: "https://robotics-transformer-x.github.io",
          icon: "fa-link",
        },
      ],
    },
    {
      title: "Data Quality in Imitation Learning",
      authors: "Suneel Belkhale, Yuchen Cui, Dorsa Sadigh",
      venue:
        "Conference on Neural Information Processing Systems (NeurIPS), December 2023",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2306.02437",
          icon: "fa-file",
        },
      ],
    },
    {
      title: "HYDRA: Hybrid Robot Actions for Imitation Learning",
      authors: "Suneel Belkhale, Yuchen Cui, Dorsa Sadigh",
      venue:
        "Conference on Robot Learning (CoRL), November 2023",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2306.17237",
          icon: "fa-file",
        },
        {
          text: "website",
          url: "https://sites.google.com/view/hydra-il-2023",
          icon: "fa-link",
        },
      ],
    },
    {
      title: "Gesture-Informed Robot Assistance via Foundation Model",
      authors: "Li-Heng Lin, Yuchen Cui, Yilun Hao, Fei Xia, Dorsa Sadigh",
      venue:
        "Conference on Robot Learning (CoRL), November 2023",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2309.02721",
          icon: "fa-file",
        },
        {
          text: "website",
          url: "https://sites.google.com/view/giraf23",
          icon: "fa-link",
        },
      ],
    },
    {
      title:
        "Masked Imitation Learning: Discovering Environment-Invariant Modalities in Multimodal Demonstrations",
      authors:
        "Yilun Hao*, Ruinan Wang*, Zhangjie Cao, Zihan Wang, Yuchen Cui, Dorsa Sadigh",
      venue:
        "IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), October 2023",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2209.07682",
          icon: "fa-file",
        },
        {
          text: "website",
          url: "https://sites.google.com/view/mask-imitation-learning",
          icon: "fa-link",
        },
      ],
    },
    {
      title:
        '"No, to the Right" – Online Language Corrections for Robotic Manipulation via Shared Autonomy',
      authors:
        "Yuchen Cui*, Siddharth Karamcheti*, Raj Palleti, Nidhya Shivakumar, Percy Liang, Dorsa Sadigh",
      venue:
        "Proceedings of the 2023 ACM/IEEE International Conference on Human-Robot Interaction (HRI), March 2023",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2301.02555",
          icon: "fa-file",
        },
        {
          text: "website",
          url: "https://sites.google.com/view/hri-lilac",
          icon: "fa-link",
        },
      ],
    },
    {
      title:
        "Can Foundation Models Perform Zero-Shot Task Specification For Robot Manipulation?",
      authors:
        "Yuchen Cui, Scott Niekum, Abhinav Gupta, Vikash Kumar, Arvind Rajeswaran",
      venue: "Learning for Dynamics & Control Conference (L4DC), June 2022",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2204.11134",
          icon: "fa-file",
        },
        {
          text: "website",
          url: "https://sites.google.com/view/zestproject",
          icon: "fa-link",
        },
      ],
    },
    {
      title:
        "Understanding the Relationship between Interactions and Outcomes in Human-in-the-Loop Machine Learning",
      authors:
        "Yuchen Cui, Pallavi Koppol, Henny Admoni, Scott Niekum, Reid Simmons, Aaron Steinfeld, Tesca Fitzgerald",
      venue:
        "Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI), August 2021",
      links: [
        {
          text: "paper",
          url: "https://www.ijcai.org/proceedings/2021/0599.pdf",
          icon: "fa-file",
        },
      ],
    },
    {
      title:
        "The EMPATHIC Framework for Task Learning from Implicit Human Feedback",
      authors:
        "Yuchen Cui, Qiping Zhang, Alessandro Allievi, Peter Stone, Scott Niekum, and W. Bradley Knox",
      venue:
        "Conference on Robot Learning (CoRL), November 2020",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/2009.13649",
          icon: "fa-file",
        },
        {
          text: "website",
          url: "https://sites.google.com/utexas.edu/empathic",
          icon: "fa-link",
        },
      ],
    },
    {
      title: "Uncertainty-Aware Data Aggregation for Deep Imitation Learning",
      authors: "Yuchen Cui, David Isele, Scott Niekum, Kikuo Fujimura",
      venue:
        "International Conference on Robotics and Automation (ICRA), May 2019",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/1905.02780",
          icon: "fa-file",
        },
      ],
    },
    {
      title: "Risk-Aware Active Inverse Reinforcement Learning",
      authors: "Daniel S. Brown*, Yuchen Cui*, Scott Niekum",
      venue:
        "Conference on Robot Learning (CoRL), November 2020",
      links: [
        {
          text: "paper",
          url: "https://arxiv.org/abs/1901.02161",
          icon: "fa-file",
        },
      ],
    },
    {
      title: "Active Reward Learning from Critiques",
      authors: "Yuchen Cui, Scott Niekum",
      venue:
        "International Conference on Robotics and Automation (ICRA), May 2018",
      links: [
        {
          text: "paper",
          url: "https://ieeexplore.ieee.org/document/8460854",
          icon: "fa-file",
        },
      ],
    },
  ];
</script>

<section class="publications-section">
  <div class="container publications-container">
    <h1 class="publications-title">Publications</h1>

    <div class="publications-list">
      {#each publications as pub, i}
        <div class="publication-item">
          <h3 class="publication-title">{pub.title}</h3>
          <p class="publication-authors">{pub.authors}</p>
          <p class="publication-venue">{pub.venue}</p>
          <div class="publication-links">
            {#each pub.links as link}
              <a
                href={link.url}
                target="_blank"
                rel="noopener noreferrer"
                class="link-button"
                aria-label={link.text}
              >
                <i class="fa {link.icon}"></i>
              </a>
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>

<style>
  /* Publications section styles */
  .publications-section {
    padding: 30px 0 80px;
    background-color: white;
  }

  .publications-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .publications-title {
    font-size: 2.5rem;
    font-weight: 600;
    color: #1a1a1a;
    margin: 0 0 50px 0;
    letter-spacing: -0.02em;
  }

  .publications-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .publication-item {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .publication-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #1a1a1a;
    margin: 0 0 4px 0;
    line-height: 1.4;
  }

  .publication-authors {
    font-size: 0.95rem;
    margin: 0 0 2px 0;
    line-height: 1.5;
    color: #333333;
  }

  .publication-venue {
    font-size: 0.95rem;
    font-style: italic;
    margin: 0 0 8px 0;
    color: #555555;
    line-height: 1.5;
  }

  .publication-links {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 0;
  }

  .link-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 2px;
    border-radius: 50%;
    font-size: 0.65rem;
    text-decoration: none;
    transition: all 0.2s ease;
    background-color: #4493CF;
    color: white;
    border: none;
    width: 18px;
    height: 18px;
  }

  .link-button:hover {
    background-color: #2a7ab8;
  }


  /* Responsive adjustments */
  @media (max-width: 768px) {
    .publications-title {
      font-size: 2rem;
      margin-bottom: 40px;
    }

    .publications-list {
      gap: 18px;
    }

    .publication-title {
      font-size: 1.05rem;
    }

    .publication-authors,
    .publication-venue {
      font-size: 0.9rem;
    }
  }

  @media (max-width: 480px) {
    .publications-title {
      font-size: 1.75rem;
    }

    .link-button {
      padding: 2px;
      font-size: 0.6rem;
      width: 16px;
      height: 16px;
    }
  }
</style>
