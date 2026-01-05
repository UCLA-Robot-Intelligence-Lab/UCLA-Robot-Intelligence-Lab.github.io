<script>
  // Any interactivity can go here
</script>

<div class="syllabus-container">
  <h1>COM SCI 188: Introduction to Robotics</h1>
  <p><strong>Units:</strong> 4</p>
  <p><strong>Level:</strong> Upper Undergraduate</p>
  <p><strong>Quarter:</strong> Winter 2026</p>

  <h2>Schedule</h2>
  <ul>
    <li><strong>Class:</strong> TR 10-11:50am @ Boelter 2760</li>
    <li><strong>Discussion Sections (Required):</strong></li>
    <ul>
      <li>1A: F 2-3:50pm @ Haines Hall A2</li>
      <li>1B: F 12-1:50pm @ Haines Hall 118</li>
    </ul>
    <li><strong>Piazza:</strong> <a href="https://piazza.com/ucla/winter2026/cs188" target="_blank">Course Piazza</a></li>
  </ul>

  <h2>Recommended Background</h2>
  <ul>
    <li><strong>Math:</strong> Calculus (MATH 32A), Linear Algebra (MATH 33A), Probability (MATH 70, MATH 170x)</li>
    <li><strong>Physics:</strong> Mechanics (Physics 1A)</li>
    <li><strong>Coding:</strong> CS 35L & Proficiency in Python</li>
  </ul>

  <h2>Course Description</h2>
  <p>
    This course provides an overview of fundamental principles in robotics, including kinematics, dynamics, perception, control, and planning. Topics also explore the integration of hardware and software in robotic systems, along with applications in real-world scenarios such as robotic manipulation. Instruction includes lectures, hands-on projects, and discussions. Designed for undergraduate students interested in robotics and its interdisciplinary connections to computer science, engineering, and artificial intelligence.
  </p>
  <p><em>Letter grading.</em></p>

  <h2>Instructor</h2>
  <ul>
    <li><strong>Name:</strong> Yuchen Cui</li>
    <li><strong>Office:</strong> EVI 396B</li>
    <li><strong>Contact:</strong> <a href="mailto:yuchencui@cs.ucla.edu">yuchencui@cs.ucla.edu</a></li>
    <li><strong>Office Hours:</strong> Wed 3-4pm</li>
  </ul>

  <h2>Course Objectives</h2>
  <ul class="course-objectives clean-style">
    <li>Develop a foundational understanding of <em>kinematics, dynamics, and control</em> for modeling and managing robotic motion.</li>
    <li>Become familiar with <em>sensors and perception algorithms</em> to interpret environmental data for robotic decision-making.</li>
    <li>Understand principles of <em>state estimation</em>, as well as <em>task and motion planning</em>, to enable reliable and efficient robot behaviors.</li>
    <li>Explore basic ideas of <em>AI in robotics</em>, including imitation learning and human–robot interaction, for advanced autonomous capabilities.</li>
    <li>Gain <em>hands-on experience</em> in simulation tools to design, test, and refine robotic systems in a virtual environment.</li>
    <li>Reflect on the <em>ethical implications</em> of robotics, fostering responsible development and deployment of robotic technologies.</li>
  </ul>

  <h2>Reference Textbooks</h2>
  <ul>
    <li>
      <strong>Modern Robotics: Mechanics, Planning, and Control</strong> by Lynch & Park —
      <a href="https://hades.mech.northwestern.edu/images/7/7f/MR.pdf" target="_blank">PDF</a>
    </li>
    <li>
      <strong>Probabilistic Robotics</strong> by Thrun, Burgard, & Fox —
      <a href="https://docs.ufpr.br/~danielsantos/ProbabilisticRobotics.pdf" target="_blank">PDF</a>
    </li>
  </ul>

  <h2>Grading Breakdown</h2>
  <ul>
    <li>Problem Sets: 24% (4 × 6%)</li>
    <li>Programming Assignments: 24% (3 × 8%)</li>
    <li>Midterm Exam: 29%</li>
    <li>Final Project: 15% (demo 5% + report 10%)</li>
    <li>Participation & In-Class Quizzes: 8%</li>
    <li><strong>Late Policy:</strong> -10% × Max Score × Days Late</li>
  </ul>

  <h2>Course Staff</h2>
  <h3>Teaching Assistants</h3>
  <ul>
    <li><strong>Holden Grissett</strong></li>
    <ul>
      <li>Email: <a href="mailto:holdengs@g.ucla.edu">holdengs@g.ucla.edu</a></li>
      <li>Discussion 1A: F 2-3:50pm @ Haines Hall A2</li>
      <li>Office Hour: 2nd half of discussion section</li>
    </ul>
    <li><strong>Ashima Suvarna</strong></li>
    <ul>
      <li>Email: <a href="mailto:asuvarna31@ucla.edu">asuvarna31@ucla.edu</a></li>
      <li>Discussion 1B: F 12-1:50pm @ Haines Hall 118</li>
      <li>Office Hour: 2nd half of discussion section</li>
    </ul>
  </ul>

  <h3>Learning Assistants</h3>
  <ul>
    <li><strong>Raayan Dhar</strong> — <a href="mailto:raayandhar@ucla.edu">raayandhar@ucla.edu</a></li>
    <li><strong>Yike Shi</strong> — <a href="mailto:yikeshi9248@g.ucla.edu">yikeshi9248@g.ucla.edu</a></li>
    <li><strong>Alexis Lee</strong> — <a href="mailto:nocturne20@ucla.edu">nocturne20@ucla.edu</a></li>
  </ul>

  <p><em>Best to ask questions on Piazza!</em></p>

  <h2>Course Schedule (subject to change)</h2>

  <table class="schedule-table">
    <thead>
      <tr>
        <th>Week</th>
        <th>Date</th>
        <th>Topics</th>
        <th>Assignments</th>
        <th>Due</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>1/6<br />1/8<br />1/9</td>
        <td>Introduction, Logistics, and Overview<br />Configuration Space, Actuators, and Sensors<br />Robosuite Tutorial</td>
        <td>Problem Set 1</td>
        <td>1/16</td>
      </tr>
      <tr>
        <td>2</td>
        <td>1/13<br />1/15<br />1/16</td>
        <td>Rigid Body Motions &amp; Kinematics<br />Robot Dynamics and PID Control<br />CA 1 kickstart</td>
        <td>Coding Assignment 1</td>
        <td>1/23</td>
      </tr>
      <tr>
        <td>3</td>
        <td>1/20<br />1/22<br />1/23</td>
        <td>Cameras, Imaging Models, and Calibration<br />Computer Vision for Robotics<br />Practice Problems</td>
        <td>Problem Set 2</td>
        <td>1/30</td>
      </tr>
      <tr>
        <td>4</td>
        <td>1/27<br />1/29<br />1/30</td>
        <td>Probabilistic State Estimation<br />Simultaneous Localization and Mapping<br />CA 2 kickstart</td>
        <td>Coding Assignment 2</td>
        <td>2/6</td>
      </tr>
      <tr>
        <td>5</td>
        <td>2/3<br />2/5<br />2/6</td>
        <td>Configuration-Space Planning &amp; Sampling-Based Planning (PRM, RRT)<br />Trajectory Generation Basics<br />Practice Problems</td>
        <td>Problem Set 3</td>
        <td>2/13</td>
      </tr>
      <tr>
        <td>6</td>
        <td>2/10<br />2/12<br />2/13</td>
        <td>Markov Decision Processes (MDPs) &amp; Reinforcement Learning<br />Imitation Learning<br />CA 3 kickstart</td>
        <td>Coding Assignment 3</td>
        <td>2/20</td>
      </tr>
      <tr>
        <td>7</td>
        <td>2/17<br />2/19<br />2/20</td>
        <td>Midterm Review<br /><strong>Midterm Exam</strong><br />Office Hours</td>
        <td>Final Project Proposal</td>
        <td>2/27</td>
      </tr>
      <tr>
        <td>8</td>
        <td>2/24<br />2/26<br />2/27</td>
        <td>Human-Robot Interaction I<br />Human-Robot Interaction II<br />Final Project Kickoff &amp; Proposal Workshop</td>
        <td>Problem Set 4</td>
        <td>3/6</td>
      </tr>
      <tr>
        <td>9</td>
        <td>3/3<br />3/5<br />3/6</td>
        <td>Foundation Models for Robotics<br />Ethical Considerations<br />Project Workshop</td>
        <td>—</td>
        <td>—</td>
      </tr>
      <tr>
        <td>10</td>
        <td>3/10<br />3/12<br />3/13</td>
        <td>Frontier Research Topics<br />Final Project Brief<br />Office Hours</td>
        <td>Final Project Report<br />Report DUE (firm)</td>
        <td>3/13</td>
      </tr>
    </tbody>
  </table>

  <h2>University Policies</h2>
  <ul>
    <li><strong>GenAI Guidance</strong> — Follow UCLA's guidance on generative AI tools in academic settings. <a href="https://docs.google.com/document/d/1V9OpwizUiHgLVMeEx-7g3AV1QrTAkBo0D-dsFv0DlwM/edit?tab=t.0#heading=h.c6al1vj9d3g">UCLA GenAI Guidance</a>.</li>
    <li><strong>Academic Integrity</strong> — All work must be your own. Violations will be reported per university policy. <a href="https://docs.google.com/document/d/1V9OpwizUiHgLVMeEx-7g3AV1QrTAkBo0D-dsFv0DlwM/edit?tab=t.0#heading=h.c6al1vj9d3gd">UCLA Academic Integrity Statement</a>.</li>
    <li><strong>Title IX</strong> — For confidential support, contact <a href="mailto:care@careprogram.ucla.edu">CARE</a> or <a href="mailto:titleix@equity.ucla.edu">Title IX Office</a>.</li>
    <li><strong>Engineering EDI</strong> — Reach out to departmental EDI officers for questions on inclusivity and support. See <a href="https://samueli.ucla.edu/equity-diversity-and-inclusion/">here</a> for more information.</li>
  </ul>
</div>

<style>
  .syllabus-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    font-size: 1.125rem;
    line-height: 1.75;
  }

  h1, h2 {
    text-align: center;
    margin-top: 2rem;
  }

  ul.course-objectives {
    padding-left: 1.5rem;
    margin-top: 1rem;
    margin-bottom: 2rem;
    list-style-type: disc;
  }

  ul.course-objectives li {
    margin-bottom: 1rem;
    line-height: 1.8;
  }

  ul.course-objectives em {
    font-style: italic;
  }

  table.schedule-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1.5rem;
    font-size: 1rem;
  }

  table.schedule-table th,
  table.schedule-table td {
    border: 1px solid #ccc;
    padding: 0.75rem;
    vertical-align: top;
    text-align: left;
  }

  a {
    color: #1a56db;
    text-decoration: underline;
  }

  ul {
    padding-left: 1.5rem;
    margin-bottom: 1rem;
  }

  ul ul {
    padding-left: 1rem;
    margin-top: 0.25rem;
  }

  em {
    font-style: italic;
  }
</style>