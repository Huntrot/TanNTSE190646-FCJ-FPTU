---
title: "Week 11 Worklog"
weight: 2
chapter: false
pre: " <b> 1.11. </b> "
---

### Week 11 Objectives:

* Complete the backend project.

### Tasks to Implement This Week:
| Day | Task | Start Date | Completion Date | Resources |
| --- | ----- | ----------- | ---------------- | ---------- |
| 2 | - Participate in the **AWS Cloud Mastery Series #2** event. | 17/11/2025 | 17/11/2025 | <> |
| 3 | - Update backend code: <br>&emsp; + Fully migrate to Serverless using aws-serverless-java-container-springboot2 and DynamoDB Enhanced Client. | 18/11/2025 | 18/11/2025 | <> |
| 4 | - Update backend code: <br>&emsp; + Use the Adapter Layer approach to convert the MySQL database to DynamoDB. | 19/11/2025 | 19/11/2025 | <> |
| 5-6 | - Update backend code: <br>&emsp; + Remove the Adapter Layer due to duplicated backend data. <br>&emsp; + Use a cloud-native approach to fully migrate to DynamoDB. | 20/11/2025 | 23/11/2025 | <> |

### Week 11 Achievements:
- Completed participation in **Cloud Mastery Series #2**, gaining solid understanding of key topics: DevOps Mindset, CI/CD Pipeline, Monitoring & Observability with **CloudWatch** and **AWS X-Ray**.  
- Acquired clear insight into real-world pipeline workflows from the speaker’s presentation and applied this knowledge to the backend project.  
- Successfully deployed the backend on **AWS Lambda** using `aws-serverless-java-container-springboot2`.  
- Fully migrated the database from **MySQL → DynamoDB**, including models, repositories, and services.  
- Removed the Adapter Layer to avoid data duplication and adopted a **cloud-native** approach, reducing complexity and boosting performance.  
- Fixed several issues related to DynamoDB Enhanced Client, NumberFormatException, and refactored all models to match the KeySchema.  
- The backend is now stable on the serverless architecture, ready for cost optimization and DynamoDB tuning.
