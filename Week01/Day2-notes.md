# 📅 Week 1 - Day 2: Amazon EC2 & Compute Services

**Date:** November 7, 2025
**Time:** 21:00 HRS (9:00 PM EAT)
**Duration:** 1 Hour 30 minutes
**Status:** ✅ Completed

---

## 📚 What I Learned Today

### 🖥️ Compute in the Cloud

#### Core Concepts
- **Vertical Scaling:** Ability to resize compute resources up or down
- **Networking Control:** Full control over network configuration and access
- **Compute as a Service (CaaS):** Pay only for compute time used
- **Multi-tenancy:** Multiple customers share same physical hardware securely

---

### 💻 Amazon EC2 Instance Types

Understanding the right instance type is crucial for performance and cost optimization.

| Instance Type | Best For | Key Characteristics | Example Use Cases |
|--------------|----------|---------------------|-------------------|
| **General Purpose** | Balanced workloads | Equal compute, memory, networking | Web servers, code repositories, dev/test environments |
| **Compute Optimized** | CPU-intensive tasks | High-performance processors | Gaming servers, HPC, batch processing, ML inference |
| **Memory Optimized** | Memory-intensive tasks | Fast memory performance | In-memory databases, real-time big data analytics |
| **Accelerated Computing** | GPU-required workloads | Hardware accelerators | Graphics rendering, ML training, pattern matching |
| **Storage Optimized** | I/O-intensive tasks | High sequential read/write | Data warehouses, distributed file systems, log processing |

**💡 Pro Tip:** Start with General Purpose (t2/t3 instances) and monitor performance. Scale to specialized instance types as needs become clear.

---

### 🛠️ Provisioning AWS Resources

AWS provides three primary methods to interact with and provision resources:

#### 1. AWS Management Console
- **Type:** Browser-based visual interface
- **Best For:** Beginners, testing, manual configuration
- **Use Cases:**
  - Setting up test environments
  - Viewing AWS bills and cost explorer
  - Managing monitoring dashboards
  - Performing administrative tasks
- **Pros:** Intuitive, visual, no coding required
- **Cons:** Manual, time-consuming for repetitive tasks

#### 2. AWS CLI (Command Line Interface)
- **Type:** Terminal-based API access
- **Best For:** Automation, scripting, DevOps workflows
- **Features:**
  - Make API calls from local terminal
  - Use AWS CloudShell for browser-based CLI
  - Create automation scripts
  - Integrate with CI/CD pipelines
- **Pros:** Fast, scriptable, version-controllable
- **Cons:** Steeper learning curve

#### 3. AWS SDK (Software Development Kit)
- **Type:** Programming language libraries
- **Best For:** Developers building applications
- **Supported Languages:** Python (Boto3), JavaScript, Java, .NET, Go, Ruby, PHP
- **Use Cases:**
  - Embed AWS services in applications
  - Build custom cloud management tools
  - Create automated workflows
- **Pros:** Full programmatic control, native language integration
- **Cons:** Requires programming knowledge

---

### 🔒 Shared Responsibility Model for EC2

```
┌─────────────────────────────────────────┐
│      CUSTOMER (Security IN Cloud)       │
│  - Guest OS (patches, updates)          │
│  - Application security                 │
│  - Identity & Access Management         │
│  - Security groups & firewall config    │
│  - Data encryption                      │
├─────────────────────────────────────────┤
│      AWS (Security OF Cloud)            │
│  - Physical infrastructure              │
│  - Network infrastructure               │
│  - Hypervisor                          │
│  - Host OS                              │
│  - Physical security of data centers    │
└─────────────────────────────────────────┘
```

**Key Insight:** AWS secures the infrastructure, but YOU are responsible for securing what you put on it.

---

### 💿 Amazon Machine Images (AMI)

**Definition:** Template containing OS, storage configuration, architecture type, and pre-installed software for EC2 instances.

#### AMI Components:
- **Operating System:** Windows, Linux (Ubuntu, Amazon Linux, etc.)
- **Storage Mapping:** EBS volumes and instance store
- **Architecture:** x86 or ARM-based processors
- **Permissions:** Public, private, or AWS Marketplace
- **Software Stack:** Pre-configured applications and services

#### AMI Benefits:
1. **Consistency:** Deploy identical environments every time
2. **Repeatability:** Launch multiple instances with same configuration
3. **Version Control:** Maintain different versions of server configurations
4. **Deployment Automation:** Integrate with Infrastructure as Code (IaC)
5. **Disaster Recovery:** Quick restoration from known-good states

#### AMI Sources:
- **AWS-provided:** Pre-configured, optimized, regularly updated
- **AWS Marketplace:** Third-party vendors with specialized configurations
- **Custom AMIs:** Create your own from configured instances
- **Community AMIs:** Shared by other AWS users

---

### 💰 Amazon EC2 Pricing Models

| Pricing Model | Commitment | Discount | Best For | Key Features |
|--------------|------------|----------|----------|--------------|
| **On-Demand** | None | Baseline | Unpredictable workloads, short-term | Pay per second/hour, no upfront cost |
| **Savings Plans** | 1-3 years | Up to 72% | Consistent usage patterns | Flexible across instance families |
| **Reserved Instances** | 1-3 years | Up to 75% | Steady-state workloads | Specific instance type reservation |
| **Spot Instances** | None | Up to 90% | Fault-tolerant workloads | Can be interrupted with 2-min warning |
| **Dedicated Hosts** | 1-3 years | Varies | Compliance requirements | Physical server for single customer |

#### Pricing Model Decision Tree:
```
Is workload predictable?
├─ YES → Reserved Instances or Savings Plans
└─ NO → Is workload interruptible?
    ├─ YES → Spot Instances
    └─ NO → On-Demand

Need licensing control or compliance?
└─ YES → Dedicated Hosts
```

---

## 🛠️ New Tools & Technologies

### Learned Today:
- 🖥️ **Amazon EC2** - Elastic Compute Cloud for resizable compute capacity
- 💿 **Amazon Machine Images (AMI)** - Templates for EC2 instance deployment
- 🖱️ **AWS Management Console** - Visual web interface for AWS services
- ⌨️ **AWS CLI** - Command-line tool for automation
- 📚 **AWS SDKs** - Libraries for programmatic AWS access (Boto3, etc.)
- 💰 **EC2 Pricing Models** - Five different cost optimization strategies

### Coming Up:
- ⚖️ Elastic Load Balancing (ELB)
- 📈 Auto Scaling
- 📬 Amazon SQS (Simple Queue Service)
- 🔔 Amazon SNS (Simple Notification Service)

---

## 💻 Hands-On Practice

### What I Worked On:
- Watched AWS Cloud Practitioner Essentials Module 2 videos
- Explored EC2 instance types and their use cases
- Reviewed EC2 launch demo and AMI selection process
- Studied EC2 pricing calculator and cost optimization strategies
- Compared provisioning methods (Console vs CLI vs SDK)

### Key Activities:
```
✅ Completed AWS Module 2: Compute in the Cloud
✅ Studied all 5 EC2 instance types with real-world examples
✅ Watched EC2 instance launch demo
✅ Reviewed AMI configuration and selection
✅ Analyzed EC2 pricing models and use cases
✅ Compared provisioning tools (Console, CLI, SDK)
✅ Documented notes and key concepts
```

### Planning Next Hands-On:
```bash
# Saturday lab session will include:
# 1. Launch first EC2 instance
# 2. Connect to instance via SSH
# 3. Configure security groups
# 4. Create custom AMI from configured instance
# 5. Test different instance types
```

---

## 💡 Key Takeaways

### Top 3 Insights:

1. **🎯 Match Instance Type to Workload**
   - Each EC2 instance type is optimized for specific workload patterns
   - Starting with General Purpose provides flexibility while learning
   - Understanding workload requirements prevents over-provisioning costs
   - Can easily change instance types as needs evolve

2. **⚙️ Choose the Right Provisioning Method**
   - AWS provides multiple ways (Console, CLI, SDK) to interact with and automate cloud resource management
   - Console for learning, CLI for automation, SDK for application integration
   - DevOps professionals leverage CLI/SDK for Infrastructure as Code

3. **💰 Pricing Flexibility Enables Cost Optimization**
   - Different EC2 pricing models help match business needs to budget and workload patterns
   - Combine multiple models for different workload types (70-90% savings possible)
   - Understanding pricing models is crucial for AWS Cloud Practitioner exam

### Important Concepts to Remember:
- **AMIs** are templates, not running instances (like blueprints)
- **Instance families** have specific letter codes (T, M, C, R, P, etc.)
- **Shared responsibility** means YOU secure the OS and applications
- **Pricing decisions** should balance cost, performance, and availability
- **Automation** through CLI/SDK is essential for production workflows

---

## 🚧 Challenges Faced

### Challenge #1: Understanding EC2 Pricing Models

**Problem:**
Initially overwhelmed by five different pricing models. Unclear when to use each option and how to combine them for optimal cost savings.

**Solution:**
- Created comparison table with key features of each model
- Reviewed AWS pricing calculator and documentation examples
- Researched real-world use case examples for each pricing type
- Mapped pricing models to specific workload characteristics

**Learning:**
On-demand suits unpredictable workloads; Reserved/Savings plans fit steady-state usage; Spot Instances provide massive savings (up to 90%) for fault-tolerant workloads; Dedicated Hosts for compliance and licensing requirements.

**Mental Model:**
```
Predictable workload? → Reserved/Savings Plans (save 50-75%)
Can handle interruptions? → Spot Instances (save up to 90%)
Need flexibility? → On-Demand (baseline pricing)
Licensing/Compliance? → Dedicated Hosts (full control)
```

---

### Challenge #2: Distinguishing Between Instance Types

**Problem:**
Five instance type families seemed similar at first. Difficult to remember which type suits which workload.

**Solution:**
- Created mnemonic device: **GCMAS** (General, Compute, Memory, Accelerated, Storage)
- Associated each type with clear real-world analogy
- Reviewed AWS documentation examples for each category

**Learning:**
Think of instance types like different vehicle types:
- **General Purpose** = Family car (everyday use, balanced)
- **Compute Optimized** = Sports car (speed/performance)
- **Memory Optimized** = Truck (carry heavy loads in memory)
- **Accelerated Computing** = Race car (specialized high-performance)
- **Storage Optimized** = Delivery van (lots of storage access)

---

## 📖 Resources Used

### Official AWS Resources:
1. **[AWS Cloud Practitioner Essentials - Module 2](https://skillbuilder.aws/learn/94T2BEN85A/aws-cloud-practitioner-essentials/8D79F3AVR7)**
   - Compute in the Cloud (comprehensive module)
   - EC2 instance types and pricing models


### Additional Learning:
- **AWS Documentation:** Amazon EC2 Overview
- **FreeCodeCamp YouTube:** AWS EC2 Basics for Beginners

### Time Spent on Each Resource:
- Video course: 45 minutes
- Documentation reading: 30 minutes
- Pricing calculator exploration: 15 minutes

---

## 🎯 Tomorrow's Plan (Day 3 - Saturday Lab Session)

### Primary Goals:
1. **Launch First EC2 Instance**
   - Choose appropriate AMI (Amazon Linux 2)
   - Select instance type (t2.micro for free tier)
   - Configure security group (SSH access)

2. **Study Auto Scaling & Load Balancing**
   - Learn Elastic Load Balancing concepts
   - Understand Auto Scaling groups
   - Study traffic distribution patterns

3. **Explore Messaging Services**
   - Amazon SQS (Simple Queue Service)
   - Amazon SNS (Simple Notification Service)
   - Message queuing patterns

### Preparation:
- [ ] Ensure AWS Free Tier account is active
- [ ] Generate SSH key pair for EC2 access
- [ ] Bookmark EC2 launch guide
- [ ] Review security group best practices

---

## 📊 Session Metrics

**Productivity Indicators:**
- **Focus Level:** High - stayed on track with module content
- **Comprehension:** Strong - pricing models became clear after practice
- **Note Quality:** Detailed with tables and diagrams
- **Questions Remaining:** 2-3 about scaling strategies (will explore Saturday)

**Emotional State:**
- **Mood:** 😊 Focused and productive
- **Energy Level:** 8/10 - maintained good concentration
- **Confidence:** 7/10 - comfortable with concepts, ready for hands-on

**What Went Well:**
- ✅ Tables and comparisons made concepts crystal clear
- ✅ Pricing calculator hands-on helped solidify understanding
- ✅ Real-world examples connected theory to practice
- ✅ Organized notes will be great study reference

**What Could Be Better:**
- 🔄 Would benefit from actual hands-on EC2 launch (coming Saturday!)
- 🔄 Could explore more pricing calculator scenarios
- 🔄 Should take screenshots during demos

---

## 🎮 Gamification Stats

**XP Earned:** 50 XP (Study Session)
**Current Total:** 100 XP
**Progress:** Day 2/336 complete
**Streak:** 2 study sessions ✅

**To Log This Session:**
```bash
cd Scripts/gamification
./xp q
```

---

## 📝 Personal Notes

### Reflections:
Day 2 built perfectly on Day 1's foundation. Understanding cloud basics made EC2 concepts much easier to grasp. The variety of instance types shows AWS's flexibility in handling different workload requirements. Most exciting realization: with the right pricing strategy, you can save 70-90% on compute costs!

### Connections to Prior Knowledge:
- EC2 instance types remind me of choosing server specifications in traditional environments
- Pricing models similar to mobile phone plans (pay-as-you-go vs contract)
- AMIs are like VM templates or Docker images
- Security groups relate to traditional firewall concepts

### Questions for Further Research:
1. How exactly does AWS determine when to reclaim Spot Instances?
2. What's the practical difference between Savings Plans and Reserved Instances?
3. How do you automate AMI creation and updates in production?
4. What's the best practice for combining multiple pricing models?

### Ah-Ha Moments:
💡 **Instance types aren't just about size** - they're about optimizing for specific workload patterns (CPU, memory, I/O, GPU)

💡 **AMIs enable true Infrastructure as Code** - can version control entire server configurations

💡 **AWS pricing flexibility = competitive advantage** - businesses can scale efficiently without massive upfront investment

---

**Session Status:** ✅ **COMPLETED**
**Next Session:** November 9, 2025 (Day 3 - Saturday Lab Session)
**Journey Progress:** 2/4 Week 1 sessions complete → 50% of Week 1!

---

*"The best way to learn is by doing. Tomorrow, we build!"*

**#DevOpsJourney #AWS #EC2 #Day2Complete #CloudComputing**
