# Week 1: Introduction to Cloud & AWS

**Phase 1: Foundation**
**Status:** 🔄 In Progress
**Study Hours:** 1.67 / 9 hours

---

## 📚 Learning Objectives

This week focuses on introduction to cloud computing fundamentals and AWS core services.

### Key Topics:
- Cloud Computing Fundamentals & Service Models
- AWS Global Infrastructure (Regions & Availability Zones)
- AWS Shared Responsibility Model
- AWS Core Services (EC2, S3, Lambda)

---

## 📅 Daily Breakdown

### Day 1 (Tuesday Evening - 1.67 hours) ✅ COMPLETED
**Topics:**
- Introduction to Cloud Computing
- Client-Server Model & Pay-As-You-Go Pricing
- AWS Global Infrastructure (Regions & Availability Zones)
- AWS Shared Responsibility Model
- Benefits of AWS Cloud

**Key Learnings:**
- ☁️ Cloud computing = On-demand IT resources over internet with pay-as-you-go pricing
- 🌍 AWS Regions contain minimum 3 physically separate Availability Zones
- 🛡️ High availability achieved by distributing resources across multiple AZs
- 🔒 Shared Responsibility: AWS secures infrastructure, customers secure data/applications
- 💰 Six key benefits: Pay-as-you-go, economies of scale, stop guessing capacity, speed/agility, no data center costs, global reach

**Resources:**
- [x] AWS Cloud Practitioner Essentials - Module 1
- [x] AWS Documentation on Cloud Computing
- [x] AWS Shared Responsibility Model Documentation
- [x] Regions and Availability Zones Overview

**Notes:** See `Day1-notes.md`

---

### Day 2 (Thursday Evening - 1.5 hours) ✅ COMPLETED
**Topics:**
- Amazon EC2 (Elastic Compute Cloud)
- EC2 Instance Types (General Purpose, Compute, Memory, Accelerated, Storage)
- How to Provision AWS Resources (Console, CLI, SDK)
- Amazon Machine Images (AMI)
- EC2 Pricing Models
- Introduction to Autoscaling and Load Balancing

**Key Learnings:**
- 🖥️ EC2 provides resizable compute capacity with vertical scaling and networking control
- 📦 5 EC2 instance types: General Purpose, Compute Optimized, Memory Optimized, Accelerated Computing, Storage Optimized
- 🛠️ Three ways to provision resources: AWS Console (beginners), CLI (automation), SDK (developers)
- 💿 AMIs enable consistent, repeatable environments for deployment automation
- 💰 EC2 offers flexible pricing models to optimize costs

**Resources:**
- [x] AWS Cloud Practitioner Essentials - Module 2
- [x] EC2 Instance Types documentation
- [x] Watched EC2 Launch Demo

**Notes:** See `Day2-notes.md`

---

### Day 3 (Saturday Morning - 3 hours)
**Topics:**
- Labs and hands-on practice
- Building small projects

**Labs:**
- [ ] Lab 1: [Lab name]
- [ ] Lab 2: [Lab name]

**Notes:** See `labs/` directory

---

### Day 4 (Sunday Afternoon - 3 hours)
**Topics:**
- Project work
- Review and documentation

**Activities:**
- [ ] Complete weekly project
- [ ] Document learnings
- [ ] Update GitHub
- [ ] Write blog post

---

## 🛠️ Hands-On Labs

### Lab 1: [Lab Name]
**Location:** `labs/lab1-[name].md`  
**Duration:** 45 minutes  
**Objective:** [What you'll build/learn]

### Lab 2: [Lab Name]
**Location:** `labs/lab2-[name].md`  
**Duration:** 45 minutes  
**Objective:** [What you'll build/learn]

---

## 📝 Notes & Resources

**Key Concepts Learned:**
- **Cloud Computing:** On-demand delivery of IT resources over the internet with pay-as-you-go pricing
- **AWS Regions:** Physical locations around the world containing groups of data centers (minimum 3 AZs each)
- **Availability Zones (AZs):** One or more isolated data centers with redundant power, networking, and connectivity
- **Shared Responsibility Model:** AWS secures the infrastructure (OF the cloud), customers secure their data/applications (IN the cloud)
- **Cloud Deployment Models:** Cloud-based, On-premise, and Hybrid approaches
- **High Availability:** Distribute resources across multiple AZs to prevent single points of failure

**Useful Commands:**
```bash
# Add commands learned this week to commands.sh
# (No CLI commands learned on Day 1 - theoretical foundation)
```

**Resources Used:**
- [AWS Cloud Practitioner Essentials](https://skillbuilder.aws/learn/94T2BEN85A/aws-cloud-practitioner-essentials/8D79F3AVR7)
- [What is Cloud Computing?](https://aws.amazon.com/what-is-cloud-computing/?nc1=f_cc)
- [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

---

## 💡 Challenges & Solutions

### Challenge 1: Understanding Regions vs Availability Zones
**Problem:** Initially confused about the practical difference between AWS Regions and Availability Zones. The concepts seemed similar.

**Solution:**
- Watched AWS Cloud Practitioner Essentials Module 1 video
- Explored AWS Console to see regions and AZs visually
- Drew diagrams to understand the hierarchy
- Researched example architectures

**Learning:**
- **Regions** are large geographic areas (e.g., US East, Europe, Asia Pacific)
- **Availability Zones** are isolated data centers within a region
- **Best Practice:** Deploy across multiple AZs for high availability
- **Mental Model:** Region (Country/Continent) → AZ (City/Data Center) → Data Center (Building)

---

## ✅ Week Completion Checklist

- [x] Completed study session 1/4 (1.67 hours)
- [x] Completed study session 2/4 (1.5 hours)
- [ ] Completed study session 3/4 (Saturday labs)
- [ ] Completed study session 4/4 (Sunday project)
- [ ] Finished all labs
- [x] Updated notes and documentation
- [x] Committed code to GitHub
- [ ] Wrote weekly blog post
- [x] Updated main README progress
- [ ] Engaged with community

---

## 📈 Progress

**Time Invested:** 3.17 / 9 hours (35.2%)
**Labs Completed:** 0 / 2
**Commits Made:** 3+ (Day 1 & 2 complete)  

**Next Week:** Week 2 - Core AWS Services

---

[← Week 0](../README.md) | [Main README](../README.md) | [Week 2 →](../Week02/README.md)
