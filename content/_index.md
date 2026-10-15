---
# Hand-edited page. The items of the focus-areas block are refreshed by scripts/generate_content.py.
title: ''
summary: ''
date: 2026-10-15
type: landing
sections:
- block: resume-biography-3
  content:
    username: me
    text: ''
    headings:
      about: Biography
      education: Education
      interests: Research interests
  design:
    background:
      gradient_mesh:
        enable: true
    name:
      size: md
    avatar:
      size: medium
      shape: circle
- block: focus-areas
  id: research
  content:
    title: Research
    text: Agentic AI safety and governance, reinforcement learning for autonomous systems, and applied AI for language, health and the geosciences.
    items:
    - name: Agentic AI Safety & Governance
      description: How consent, oversight and accountability hold up when AI systems act on people's behalf and interact with each other.
      icon: hero/shield-check
      url: /research/agentic-ai-safety/
      topics:
      - Consent
      - Multi-agent systems
      - Human oversight
      - EU AI Act
      metrics:
      - icon: hero/document-text
        value: '6'
        label: papers
      cta:
        text: Read more
        url: /research/agentic-ai-safety/
    - name: Reinforcement Learning & Autonomous Systems
      description: Decision-making under uncertainty and partial observability for autonomous vehicles, robots and control.
      icon: hero/cpu-chip
      url: /research/rl-autonomy/
      topics:
      - Deep RL
      - POMDPs
      - Autonomous driving
      - Robot navigation
      metrics:
      - icon: hero/document-text
        value: '12'
        label: papers
      cta:
        text: Read more
        url: /research/rl-autonomy/
    - name: AI for Geoscience & Energy
      description: 'Machine learning and control for geothermal systems: reservoir temperature, contamination and scaling.'
      icon: hero/globe-europe-africa
      url: /research/geoscience-energy/
      topics:
      - Geothermal systems
      - Reservoir temperature
      - GANs
      - Scaling control
      metrics:
      - icon: hero/document-text
        value: '15'
        label: papers
      cta:
        text: Read more
        url: /research/geoscience-energy/
    - name: Language Technologies & LLMs
      description: Turkish language models, embedding benchmarks and multimodal language analysis.
      icon: hero/language
      url: /research/language-tech/
      topics:
      - Turkish LLMs
      - Text embeddings
      - Benchmarks
      metrics:
      - icon: hero/document-text
        value: '3'
        label: papers
      cta:
        text: Read more
        url: /research/language-tech/
    - name: AI for Health
      description: Privacy-preserving and trustworthy AI for clinical prediction, medical imaging and digital twins.
      icon: hero/heart
      url: /research/health-ai/
      topics:
      - Federated learning
      - Digital twins
      - Medical imaging
      metrics:
      - icon: hero/document-text
        value: '16'
        label: papers
      cta:
        text: Read more
        url: /research/health-ai/
    - name: Computer Vision & Applied AI
      description: Applied machine learning with industry and public partners, from livestock tracking to smart appliances.
      icon: hero/eye
      url: /research/vision-applied/
      topics:
      - Object tracking
      - Soft sensors
      - Anomaly detection
      metrics:
      - icon: hero/document-text
        value: '8'
        label: papers
      cta:
        text: Read more
        url: /research/vision-applied/
    - name: Modeling, Simulation & Control
      description: High-fidelity simulation, computer generated forces and control (2003–2015).
      icon: hero/cube-transparent
      url: /research/modeling-simulation/
      topics:
      - Simulation
      - Computer generated forces
      - Underwater vehicles
      metrics:
      - icon: hero/document-text
        value: '25'
        label: papers
      cta:
        text: Read more
        url: /research/modeling-simulation/
  design:
    layout: cards
- block: collection
  id: papers
  content:
    title: Selected Publications
    text: ''
    count: 8
    filters:
      folders:
      - publications
      featured_only: true
    archive:
      enable: true
      text: All publications
      link: publications/
  design:
    view: citation
- block: collection
  id: news
  content:
    title: News
    count: 5
    filters:
      folders:
      - blog
    archive:
      enable: true
      text: All news
      link: blog/
  design:
    view: date-title-summary
- block: collection
  id: talks
  content:
    title: Recent Talks
    count: 5
    filters:
      folders:
      - events
    archive:
      enable: true
      text: All talks and media
      link: events/
  design:
    view: date-title-summary
---
