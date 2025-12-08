---
title: "Event 7"
weight: 1
chapter: false
pre: " <b> 4.7. </b> "
---

## Report on AWS Cloud Club – Security & Data Protection Workshop

### Purpose of the Event
- Gain a clear understanding of **Incident Response** in AWS environments.  
- Learn core concepts of **Data Protection**, including encryption, key management, and access monitoring.  
- Practice securing data using **AWS KMS** and tracking activity with **AWS CloudTrail**.  
- Improve teamwork skills through GameDay-style collaborative activities.  

---

### Speakers
- **Le Vu Xuan An** - AWS Cloud Club Captain HCMUTE, First Cloud Al Journey
- **Tran Duc Anh** - AWS Cloud Club Captain SGU, First Cloud Al Journey
- **Tran Doan Cong Ly** - AWS Cloud Club Captain PTIT, First Cloud Al Journey
- **Danh Hoang Hieu Nghi** - AWS Cloud Club Captain HUFLIT, First Cloud Al Journey
- **Nguyen Tuan Thinh** - Cloud Engineer Trainee, First Cloud Al Journey
- **Nguyen Do Thanh Dat** - Cloud Engineer Trainee, First Cloud Al Journey
- **Kha Van** - Cloud Security Engineer, AWS Community Builders
- **Thịnh Lâm** – FCJ Cloud Engineer  
- **Việt Nguyễn** – FCJ Cloud Engineer  
- **Mendel Grabski (Long)** – ex Head of Security & DevOps, Cloud Security Solutions Architect  
- **Tinh Truong** – AWS Community Builder, Platform Engineer tại TymeX  

---

### Key Highlights

#### Incident Response on AWS
- Overview of the incident response lifecycle:  
  **Detect → Analyze → Contain → Eradicate → Recover → Lessons Learned**.  
- Emphasis on team coordination and clearly assigned responsibilities.  
- Practical examples to illustrate how to detect and isolate incidents quickly.

#### Data Protection – Encryption & Key Governance
- Explanation of **Encryption at Rest** and **Encryption in Transit**, and how AWS implements them.  
- Hands-on practice with **AWS Key Management Service (KMS)**:  
  - AWS-owned CMK  
  - AWS-managed CMK  
  - Customer-managed CMK  
- Learned how to configure **Customer Managed Keys** with lifecycle control, rotation, and access governance.

#### KMS for DynamoDB (the part I focused on the most)
- DynamoDB uses AES-256 encryption by default.  
- Comparison of different key types and why Customer Managed Keys are preferred in production.  
- Demonstrations showing that every “decrypt” call triggered by DynamoDB is logged—useful for security audits and anomaly detection.

#### CloudTrail – Logging & Incident Investigation
- CloudTrail records all **AWS API calls** within the account.  
- Practical scenarios showing how to use CloudTrail to:  
  - track KMS usage,  
  - audit IAM access patterns,  
  - investigate access to S3 or DynamoDB data.  

---

### Personal Experience & Lessons Learned
- This was **my first time participating in a GameDay-style event**, and I learned a great deal from the hands-on challenges.  
- The activities helped me understand how to **divide tasks based on difficulty** and support teammates effectively.  
- I gained deeper insight into encryption with KMS and analyzing logs with CloudTrail.  
- I realized the importance of teamwork in security—no single person can handle an entire incident alone.

---

### Outcomes
- Understand the full **Incident Response Framework** and how to apply it in real projects.  
- Confidently use **KMS with DynamoDB** and apply best practices for key management.  
- Able to read and analyze **CloudTrail logs** for incident investigation.  
- Improved teamwork, problem-solving, and rapid-response mindset.  
- Better prepared to implement data protection measures in real-world systems.  

---

### Event Photos
![Event7 Photo 1](/images/4-Events/Event7/1.jpg)  
![Event7 Photo 2](/images/4-Events/Event7/2.jng)  
![Event7 Photo 3](/images/4-Events/Event7/3.jpg)

> **Summary:** The Security & Data Protection Workshop provided a deep understanding of AWS security—especially KMS, CloudTrail, and incident response practices. It was also a valuable opportunity to practice teamwork through GameDay activities and apply security concepts to practical scenarios.
