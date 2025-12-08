---
title: "Blog 1"
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

### **Ingesting and Enriching Security Findings Delivered via Amazon EventBridge with Dynatrace**

Author: Shashiraj Jeripotula  

Publication date: 06/05/2025  

Categories: [Amazon Elastic Container Registry](https://aws.amazon.com/blogs/apn/category/compute/amazon-elastic-container-registry/), [Amazon EventBridge](https://aws.amazon.com/blogs/apn/category/application-integration/amazon-eventbridge/), [APN Launches](https://aws.amazon.com/blogs/apn/category/apn-launches/), [AWS Security Hub](https://aws.amazon.com/blogs/apn/category/security-identity-compliance/aws-security-hub/), [Partner solutions](https://aws.amazon.com/blogs/apn/category/post-types/partner-solutions/), [Technical How-to](https://aws.amazon.com/blogs/apn/category/post-types/technical-how-to/), [Thought Leadership](https://aws.amazon.com/blogs/apn/category/post-types/thought-leadership/)

Co-authors:  
Valeriy Leykin – Senior Product Manager, Dynatrace  
Erick Leon – Senior Manager, Global Tech Alliances, Dynatrace  
Shashiraj Jeripotula – Principal Partner Solutions Architect, AWS

In complex cloud environments, security findings are often siloed between tools used at build-time and runtime, and spread across multiple environments. As a result, achieving a holistic view of the organization’s security posture and potential risks becomes increasingly challenging. However, according to Gartner research ([Gartner research](https://www.gartner.com/doc/reprints?id=1-2J3U8GY7&ct=241017&st=sb)), fewer than 15% of large enterprise customers have deployed at least one security platform solution.

These challenges lead to several visible consequences:

* **Data access:** Security teams and engineers must navigate multiple products to gather relevant security data.
* **Prioritization:** Development and operations teams end up prioritizing findings differently due to fragmented DevSecOps tools.
* **Security coverage:** Security architects lack clear visibility into gaps in tool coverage across environments.
* **Manual effort:** Notifying stakeholders about critical security findings often requires numerous manual steps and coordination.
* **Remediation:** Owner teams tend to take longer to address critical issues because of alert fatigue, increasing Mean Time to Remediation (MTTR).

Additionally, the sheer number of security findings can overwhelm DevSecOps teams, causing them to overlook truly impactful issues that affect running production services. One common example is a high-severity vulnerability detected in a build-time artifact, such as a container image that has not yet been deployed and therefore does not pose a runtime risk. These findings should not distract DevSecOps teams. Instead, they should focus on vulnerabilities within production applications that are exposed to the internet and represent real risk.

### **How a Unified Observability and Security Platform Can Help**

To address these challenges, the unified observability and security platform [Dynatrace](https://www.dynatrace.com/) integrates with [Amazon EventBridge](https://aws.amazon.com/eventbridge/) to break down silos between DevSecOps teams, consolidate security findings across the Software Development Lifecycle (SDLC), and enrich them with runtime context. With [Dynatrace’s OpenPipeline](https://www.dynatrace.com/platform/openpipeline/), the platform enables teams to ingest, visualize, prioritize, and automate security findings. This reduces alert noise and helps focus on issues that matter most for critical production environments.

Dynatrace combines deep and broad observability with continuous application security and advanced AIOps, providing intelligent answers and automation from data at enterprise scale. This empowers organizations to modernize and automate cloud operations, deploy software faster and more securely, and deliver flawless digital experiences.

### **Ingesting Amazon EventBridge Data into the Dynatrace Platform**

Dynatrace collaborates with AWS ([Dynatrace partners with AWS](https://partners.amazonaws.com/partners/001E000000texmiIAA/Dynatrace)) and serves as a destination for [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destination-partners.html#api-destination-dynatrace). Depending on the use case, findings and logs may be forwarded to dedicated OpenPipeline endpoints and ingested into the [Dynatrace Grail data lake](https://www.dynatrace.com/platform/grail/).

![image1](/images/3-BlogsTranslated/blog1/1.png)  
*Figure 1 – Ingesting data from Amazon EventBridge*

Dynatrace supports security findings forwarded through Amazon EventBridge in the following scenarios:

* Forwarding from third-party tools as raw events or using a supported generic standard data format such as [Open Cybersecurity Schema Framework](https://schema.ocsf.io/) (OCSF) or [Amazon Security Findings Format](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) (ASFF).
* Forwarding from [AWS Security Hub](https://aws.amazon.com/security-hub/), including vulnerability, detection, and compliance events.
* Forwarding container security findings from [Amazon ECR](https://aws.amazon.com/ecr/) (including basic and enhanced scanning).
* Forwarding detection findings from [Amazon GuardDuty](https://aws.amazon.com/guardduty/).

As part of each integration setup, Dynatrace provides [CloudFormation templates](https://github.com/dynatrace-oss/cloud-snippets/tree/main/aws) and detailed configuration guidance.

EventBridge rules listen for events and trigger corresponding AWS Lambda functions for pre-processing and ingestion into Dynatrace through OpenPipeline.

Dynatrace maps ingested events to Semantic Dictionary conventions for supported products and formats ([supported products and data formats](https://dt-url.net/1d63p0v)). Users can consume events in a unified manner for dashboards, notebooks, and automation workflows.

During event consumption, users can enrich events with runtime context from Dynatrace. This improves understanding of how events affect monitored environments and supports intelligent prioritization.

![image2](/images/3-BlogsTranslated/blog1/2.png)  
*Figure 2 – Dynatrace Runtime Contextualization Dashboard*

### **Summary**

By integrating Amazon EventBridge with the Dynatrace platform, DevSecOps teams gain access to both security findings and runtime context in a single platform. This enables more effective prioritization of findings originating from different environments and tools.

Additional native Dynatrace capabilities — such as [Workflows](https://docs.dynatrace.com/docs/shortlink/workflows), [Dashboards](https://docs.dynatrace.com/docs/shortlink/dashboards), and [Security Investigator](https://docs.dynatrace.com/docs/shortlink/security-investigator) — help users visualize, analyze, and automate handling of security findings. This drives operationalization and reduces alert fatigue.

To learn more about individual AWS integrations and corresponding use cases, refer to Dynatrace documentation:

* [Ingesting vulnerability findings and scan events from Amazon ECR](https://dt-url.net/tz03pa8)
* [Ingesting security findings from AWS Security Hub](https://dt-url.net/bl23u9i)
* [Ingesting security findings from Amazon GuardDuty](https://dt-url.net/jv03zhm)

For updates on new Dynatrace product releases and capabilities, explore the following blogs:

* [Enrich AWS ECR vulnerability findings with runtime context](https://dt-url.net/9763wjo)
* [Ingesting and enriching security findings delivered via Amazon EventBridge with Dynatrace](https://dt-url.net/xn03wga)
* [Ingesting and enriching findings from AWS Security Hub with Dynatrace](https://dt-url.net/t703wux)

![image3](/images/3-BlogsTranslated/blog1/3.png)

### **Dynatrace – AWS Partner Spotlight**

Dynatrace is an AWS Advanced Technology Partner and AWS Competency Partner, providing software intelligence solutions that simplify cloud complexity and accelerate digital transformation. With advanced observability, AI, and full automation, our all-in-one platform delivers answers — not just data — about application performance, underlying infrastructure, and every user’s experience.

[Contact Dynatrace](https://partnercentral.awspartner.com/PartnerConnect?id=001E000000texmiIAA&source=Blog&campaign=) | [Partner Overview](https://partners.amazonaws.com/partners/001E000000texmiIAA/Dynatrace) | [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=1422b3b0-b081-4af9-9d2b-34e6eb924f05)

TAGS: [APN Programs](https://aws.amazon.com/blogs/apn/tag/apn-programs/), [AWS Competency Partners](https://aws.amazon.com/blogs/apn/tag/aws-competency-program/), [AWS Marketplace](https://aws.amazon.com/blogs/apn/tag/aws-marketplace/)
