<script>
  // Publications
  const publications = [
    {
      title:
        "FlowRetrieval: Flow-Guided Data Retrieval for Few-Shot Imitation Learning",
      authors: "Li-Heng Lin, Yuchen Cui, Amber Xie, Tianyu Hua, Dorsa Sadigh",
      venue:
        "Proceedings of the 8th Conference on Robot Learning (CoRL), November 2024",
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
        "Proceedings of the 7th Conference on Robot Learning (CoRL), November 2023",
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
        "Proceedings of the 7th Conference on Robot Learning (CoRL), November 2023",
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
        "Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), October 2023",
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
        "Proceedings of the 4th Conference on Robot Learning (CoRL), November 2020",
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
        "Proceedings of the 4th Conference on Robot Learning (CoRL), November 2020",
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
        <div class="publication-card">
          <div class="publication-content">
            <h3 class="publication-title">{pub.title}</h3>
            <p class="publication-authors">{pub.authors}</p>
            <p class="publication-venue">{pub.venue}</p>
          </div>
          <div class="publication-links">
            {#each pub.links as link}
              <a
                href={link.url}
                target="_blank"
                rel="noopener noreferrer"
                class="link-button"
              >
                <span class="icon"><i class="fa {link.icon}"></i></span>
                <span class="label">{link.text}</span>
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
    padding: 4rem 0;
  }

  .publications-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 4rem; /* Increased horizontal padding */
  }

  .publications-title {
    margin-bottom: 2.5rem;
    color: var(--heading-color);
    text-align: center;
    font-size: 2.5rem;
    letter-spacing: -0.03em;
    font-weight: 700;
  }

  .publications-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin-top: 2rem;
    width: 100%;
  }

  .publication-card {
    background-color: var(--card-bg);
    border-radius: 14px;
    overflow: hidden;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    display: flex;
    flex-direction: column;
    border: 1px solid rgba(68, 147, 207, 0.1); /* UCLA Light Blue with opacity */
  }

  /* Create a subtle glass-like effect for the card - Vercel inspired */
  .publication-card::before {
    content: "";
    position: absolute;
    inset: 0;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border-radius: 14px;
    opacity: 0;
    transition: opacity 0.25s ease;
    z-index: -1;
  }

  .publication-card:hover {
    transform: translateY(-4px);
    box-shadow:
      0 5px 20px rgba(0, 0, 0, 0.07),
      0 0 0 1px rgba(49, 64, 98, 0.08); /* UCLA Dark Blue border */
    border-color: rgba(
      68,
      147,
      207,
      0.25
    ); /* UCLA Light Blue with higher opacity on hover */
  }

  .publication-card:hover::before {
    opacity: 0.5;
  }

  .publication-content {
    padding: 1.75rem 1.75rem 0.75rem;
    flex: 1;
  }

  .publication-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--heading-color);
    margin: 0 0 0.75rem 0;
    letter-spacing: -0.01em;
    line-height: 1.4;
  }

  .publication-authors {
    font-size: 0.95rem;
    margin: 0 0 0.5rem 0;
    line-height: 1.5;
    color: var(--text-color);
  }

  .publication-venue {
    font-size: 0.9rem;
    font-style: italic;
    margin: 0 0 1.25rem 0;
    color: var(--secondary-text-color);
    padding-bottom: 0.75rem;
    border-bottom: 1px solid rgba(68, 147, 207, 0.1); /* UCLA Light Blue with opacity */
  }

  .publication-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    padding: 0.5rem 1.75rem 1.75rem;
    margin-top: -1.5rem;
  }

  .link-button {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.6rem 1rem;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.2s ease;
    background-color: rgba(
      68,
      147,
      207,
      0.1
    ); /* UCLA Light Blue with opacity */
    color: var(--heading-color);
    border: 1px solid transparent;
  }

  /* Subtle glow on hover - shadcn inspired */
  .link-button:hover {
    background-color: rgba(
      68,
      147,
      207,
      0.15
    ); /* UCLA Light Blue with opacity */
    color: var(--ucla-light-blue);
    border-color: rgba(68, 147, 207, 0.3); /* UCLA Light Blue border */
    transform: translateY(-2px);
    box-shadow: 0 2px 8px rgba(68, 147, 207, 0.2); /* UCLA Light Blue glow */
  }

  .icon {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.85rem;
  }

  .label {
    line-height: 1;
  }

  /* Dark mode specific styles */
  :global(.dark-mode) .publication-card {
    border-color: rgba(68, 147, 207, 0.15);
    background-color: rgba(30, 30, 30, 0.7);
  }

  :global(.dark-mode) .publication-title {
    color: var(--ucla-light-blue);
  }

  :global(.dark-mode) .link-button {
    background-color: rgba(68, 147, 207, 0.15);
    color: var(--text-color);
  }

  :global(.dark-mode) .link-button:hover {
    background-color: rgba(252, 215, 41, 0.2);
    color: var(--ucla-yellow);
    border-color: rgba(252, 215, 41, 0.3);
    box-shadow: 0 2px 10px rgba(252, 215, 41, 0.15);
  }

  /* Responsive adjustments */
  @media (max-width: 768px) {
    .publications-title {
      font-size: 2.2rem;
      margin-bottom: 2rem;
    }

    .publication-content {
      padding: 1.5rem;
    }

    .publication-links {
      padding: 0 1.5rem 1.5rem;
    }

    .publication-title {
      font-size: 1.1rem;
    }
  }

  @media (max-width: 480px) {
    .publications-title {
      font-size: 1.8rem;
    }

    .publication-content {
      padding: 1.25rem;
    }

    .publication-links {
      padding: 0 1.25rem 1.25rem;
      gap: 0.5rem;
    }

    .link-button {
      padding: 0.5rem 0.8rem;
      font-size: 0.85rem;
    }
  }
</style>
