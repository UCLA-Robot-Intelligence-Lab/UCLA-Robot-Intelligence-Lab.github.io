<script>
  // Publications
  const publications = [
    {
      title: "FlowRetrieval: Flow-Guided Data Retrieval for Few-Shot Imitation Learning",
      authors: "Li-Heng Lin, Yuchen Cui, Amber Xie, Tianyu Hua, Dorsa Sadigh",
      venue: "Proceedings of the 8th Conference on Robot Learning (CoRL), November 2024",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/2408.16944", icon: "fa-file" },
        { text: "website", url: "https://flow-retrieval.github.io/", icon: "fa-link" }
      ]
    },
    {
      title: "Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections",
      authors: "Lihan Zha, Yuchen Cui, Li-Heng Lin, Minae Kwon, Montserrat Gonzalez Arenas, Andy Zeng, Fei Xia, Dorsa Sadigh",
      venue: "International Conference on Robotics and Automation (ICRA), May 2024",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/2311.10678", icon: "fa-file" },
        { text: "website", url: "https://sites.google.com/stanford.edu/droc", icon: "fa-link" }
      ]
    },
    {
      title: "Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
      authors: "Open X-Embodiment Collaboration",
      venue: "International Conference on Robotics and Automation (ICRA), May 2024",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/2310.08864", icon: "fa-file" },
        { text: "website", url: "https://robotics-transformer-x.github.io", icon: "fa-link" }
      ]
    },
    {
      title: "Data Quality in Imitation Learning",
      authors: "Suneel Belkhale, Yuchen Cui, Dorsa Sadigh",
      venue: "Conference on Neural Information Processing Systems (NeurIPS), December 2023",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/2306.02437", icon: "fa-file" }
      ]
    },
    {
      title: "HYDRA: Hybrid Robot Actions for Imitation Learning",
      authors: "Suneel Belkhale, Yuchen Cui, Dorsa Sadigh",
      venue: "Proceedings of the 7th Conference on Robot Learning (CoRL), November 2023",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/2306.17237", icon: "fa-file" },
        { text: "website", url: "https://sites.google.com/view/hydra-il-2023", icon: "fa-link" }
      ]
    },
    {
      title: "Gesture-Informed Robot Assistance via Foundation Model",
      authors: "Li-Heng Lin, Yuchen Cui, Yilun Hao, Fei Xia, Dorsa Sadigh",
      venue: "Proceedings of the 7th Conference on Robot Learning (CoRL), November 2023",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/2309.02721", icon: "fa-file" },
        { text: "website", url: "https://sites.google.com/view/giraf23", icon: "fa-link" }
      ]
    },
    {
      title: "Masked Imitation Learning: Discovering Environment-Invariant Modalities in Multimodal Demonstrations",
      authors: "Yilun Hao*, Ruinan Wang*, Zhangjie Cao, Zihan Wang, Yuchen Cui, Dorsa Sadigh",
      venue: "Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), October 2023",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/2209.07682", icon: "fa-file" },
        { text: "website", url: "https://sites.google.com/view/mask-imitation-learning", icon: "fa-link" }
      ]
    },
    {
      title: "\"No, to the Right\" – Online Language Corrections for Robotic Manipulation via Shared Autonomy",
      authors: "Yuchen Cui*, Siddharth Karamcheti*, Raj Palleti, Nidhya Shivakumar, Percy Liang, Dorsa Sadigh",
      venue: "Proceedings of the 2023 ACM/IEEE International Conference on Human-Robot Interaction (HRI), March 2023",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/2301.02555", icon: "fa-file" },
        { text: "website", url: "https://sites.google.com/view/hri-lilac", icon: "fa-link" }
      ]
    },
    {
      title: "Can Foundation Models Perform Zero-Shot Task Specification For Robot Manipulation?",
      authors: "Yuchen Cui, Scott Niekum, Abhinav Gupta, Vikash Kumar, Arvind Rajeswaran",
      venue: "Learning for Dynamics & Control Conference (L4DC), June 2022",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/2204.11134", icon: "fa-file" },
        { text: "website", url: "https://sites.google.com/view/zestproject", icon: "fa-link" }
      ]
    },
    {
      title: "Understanding the Relationship between Interactions and Outcomes in Human-in-the-Loop Machine Learning",
      authors: "Yuchen Cui, Pallavi Koppol, Henny Admoni, Scott Niekum, Reid Simmons, Aaron Steinfeld, Tesca Fitzgerald",
      venue: "Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI), August 2021",
      links: [
        { text: "paper", url: "https://www.ijcai.org/proceedings/2021/0599.pdf", icon: "fa-file" }
      ]
    },
    {
      title: "The EMPATHIC Framework for Task Learning from Implicit Human Feedback",
      authors: "Yuchen Cui, Qiping Zhang, Alessandro Allievi, Peter Stone, Scott Niekum, and W. Bradley Knox",
      venue: "Proceedings of the 4th Conference on Robot Learning (CoRL), November 2020",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/2009.13649", icon: "fa-file" },
        { text: "website", url: "https://sites.google.com/utexas.edu/empathic", icon: "fa-link" }
      ]
    },
    {
      title: "Uncertainty-Aware Data Aggregation for Deep Imitation Learning",
      authors: "Yuchen Cui, David Isele, Scott Niekum, Kikuo Fujimura",
      venue: "International Conference on Robotics and Automation (ICRA), May 2019",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/1905.02780", icon: "fa-file" }
      ]
    },
    {
      title: "Risk-Aware Active Inverse Reinforcement Learning",
      authors: "Daniel S. Brown*, Yuchen Cui*, Scott Niekum",
      venue: "Proceedings of the 4th Conference on Robot Learning (CoRL), November 2020",
      links: [
        { text: "paper", url: "https://arxiv.org/abs/1901.02161", icon: "fa-file" }
      ]
    },
    {
      title: "Active Reward Learning from Critiques",
      authors: "Yuchen Cui, Scott Niekum",
      venue: "International Conference on Robotics and Automation (ICRA), May 2018",
      links: [
        { text: "paper", url: "https://ieeexplore.ieee.org/document/8460854", icon: "fa-file" }
      ]
    }
  ];
</script>

<section class="publications-section">
  <div class="container">
    <h1 class="publications-title">Publications</h1>

    <div class="publications-list">
      {#each publications as pub, i}
        <div class="publications-container">
          <p>
            <b>{pub.title}</b> <br />
            {pub.authors} <br />
            <i>{pub.venue}</i> <br />
            {#each pub.links as link}
              <a href={link.url} target="_blank">
                <button class="btn">
                  <i class="fa {link.icon}"></i> {link.text}
                </button>
              </a>
            {/each}
          </p>
        </div>
      {/each}
    </div>
  </div>
</section>

<style>
  /* Publications section styles */
  .publications-section {
    padding: 2rem 0;
  }

  .publications-title {
    margin-bottom: 1rem;
    color: var(--text-color);
    text-align: center;
  }

  .publications-list {
    display: flex;
    flex-direction: column;
    gap: 25px;
    margin-top: 2rem;
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
  }

  .publications-container {
    background-color: var(--card-bg);
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
  }

  .publications-container:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
  }

  .publications-container p {
    margin: 0;
    line-height: 1.6;
  }

  .publications-container b {
    font-size: 1.1rem;
    color: var(--heading-color);
    display: inline-block;
    margin-bottom: 5px;
  }

  .publications-container i {
    color: var(--secondary-text);
    display: inline-block;
    margin-bottom: 10px;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    background-color: var(--btn-bg);
    color: var(--btn-text);
    border: none;
    padding: 6px 12px;
    margin-right: 8px;
    margin-top: 10px;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 0.9rem;
    text-decoration: none;
  }

  .btn:hover {
    background-color: var(--btn-hover-bg);
    transform: translateY(-2px);
  }

  .btn i {
    margin-right: 5px;
    font-size: 0.9rem;
    color: var(--btn-icon);
  }



  /* Responsive adjustments */
  @media (max-width: 768px) {
    .publications-container {
      padding: 15px;
    }

    .publications-container b {
      font-size: 1rem;
    }

    .btn {
      padding: 5px 10px;
      font-size: 0.8rem;
      margin-top: 8px;
    }
  }
</style>
