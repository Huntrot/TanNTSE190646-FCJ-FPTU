---
title: "Blog 2"
weight: 1
chapter: false
pre: " <b> 3.2. </b> "
---

### **Leveraging Generative AI to Accelerate Genomics Data Standardization in Public Health**

**Authors:** Noor Dhaliwal, Dr. Kelsey Florek, and Logan Fink  

**Publication date:** 05/05/2025

**Categories:** [Amazon API Gateway](https://aws.amazon.com/blogs/publicsector/category/application-services/amazon-api-gateway-application-services/), [Amazon Bedrock](https://aws.amazon.com/blogs/publicsector/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/), [Artificial Intelligence](https://aws.amazon.com/blogs/publicsector/category/artificial-intelligence/), [AWS Lambda](https://aws.amazon.com/blogs/publicsector/category/compute/aws-lambda/), [Customer Solutions](https://aws.amazon.com/blogs/publicsector/category/post-types/customer-solutions/), [Generative AI](https://aws.amazon.com/blogs/publicsector/category/artificial-intelligence/generative-ai/), [Healthcare](https://aws.amazon.com/blogs/publicsector/category/public-sector/healthcare-public-sector/), [Public Sector](https://aws.amazon.com/blogs/publicsector/category/public-sector/)

![image1](/images/3-BlogsTranslated/blog2/1.png)

In precision medicine and pathogen surveillance, genomic sequencing has emerged as a cornerstone of research and public health response. However, the growth and impact of genomics face significant challenges surrounding data interoperability and standardization. Public health laboratories across the United States process tens of thousands of genomic samples every month, with each laboratory using locally optimized schemas and formats. These formats must be standardized before they can be exchanged with public health partners or submitted to public genomic repositories.

The scale of this challenge is considerable. Public health laboratory staff may spend 2 to 4 hours manually preparing data for submission to public genomic repositories such as the National Center for Biotechnology Information (NCBI). This equates to more than 400 hours annually for a single laboratory—time that could otherwise be dedicated to high-value analytical and response activities. Even more concerning, manual workflows can introduce errors, resulting in rejected or revised data submissions, which delays the release of critical genomic information to the broader scientific community.

To address this growing challenge, the [Digital Transformation Hub (DxHub)](https://dxhub.calpoly.edu/) at the [California Polytechnic State University (Cal Poly)](https://www.calpoly.edu/)—powered by [Amazon Web Services (AWS)](https://aws.amazon.com/) and part of the [AWS Cloud Innovation Centers (CIC)](https://aws.amazon.com/government-education/cloud-innovation-centers/) program—stepped in to help. DxHub collaborated with the Wisconsin State Laboratory of Hygiene (WSLH) and the Virginia Department of General Services Division of Consolidated Laboratory Services (DCLS) to build the AI Genomic Schema Harmonizer, a generative-AI-powered application designed to transform how labs prepare genomic data submissions for public repositories.

### **AI Genomics Schema Harmonizer**

The AI Genomics Schema Harmonizer reduces the burden of genomics data reporting. Instead of relying on traditional spreadsheet-based methods, the application uses generative AI to automatically align diverse laboratory terminology with standardized or required formats. By leveraging natural language processing (NLP), the Harmonizer can analyze lab-specific terminology and map it to standardized definitions in NCBI BioSample, ensuring consistent and accurate data submissions.

The impact goes far beyond simple field mapping. By simplifying schema harmonization, the Harmonizer supports a broader initiative within healthcare and life sciences: achieving semantic interoperability. This capability allows genomic data to be shared, understood, and used seamlessly across systems and organizations—a foundational requirement for modern public health surveillance and scientific research.

### **Solution Overview**

The application’s architecture is API-driven and leverages multiple AWS managed services to ensure security, scalability, and reliability. [Amazon Bedrock](https://aws.amazon.com/bedrock/) combined with the Anthropic Claude Sonnet 3.5 v2 [foundation model (FM)](https://aws.amazon.com/what-is/foundation-models/) provides secure processing of sensitive genomic metadata. [AWS Lambda](https://aws.amazon.com/lambda/) and [Amazon API Gateway](https://aws.amazon.com/api-gateway/) power the application’s backend logic. Data mapping definitions are securely stored in [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/).

The diagram below illustrates the solution architecture.

![image2](/images/3-BlogsTranslated/blog2/2.png)  
*Figure 1. Solution architecture diagram*

The system’s advanced natural language processing capabilities enable it to parse and analyze raw data structures and associated terminology, then map fields to corresponding standardized NCBI definitions using comprehensive definition libraries. Scientists perform a final review to validate mappings against current NCBI requirements and generate submission-ready files that meet federal repository standards for accuracy and timeliness.

“AI Genomics Schema Harmonizer has the potential to revolutionize genomic data submission workflows,” said Dr. Kelsey Florek, Senior Genomics and Data Scientist at WSLH. “Replacing manual data transformation steps and maintaining custom macros or scripts with a simple, broadly applicable approach allows our team to focus on core genomic analysis instead of data formatting.”

### **Student Experience at DxHub**

At the Cal Poly DxHub, students work alongside university and Amazon staff to develop innovative solutions for public sector challenges using the Amazon Working Backwards methodology. For Noor Dhaliwal, the student developer behind the GenomicsMetaDataMapper tool, this experience opened new horizons in applied AI.

“Working at DxHub gave me the opportunity to build a solution that impacts public health laboratories nationwide,” Dhaliwal said. “Learning to harness cutting-edge AI technologies like Amazon Bedrock while solving practical problems has been transformative. Building a tool that accelerates critical public health work showed me the true potential of cloud and AI technologies in the public sector.”

### **Measured Impact and Future Direction**

Initial results highlight the transformative potential of the AI Genomics Schema Harmonizer. Demonstrated impacts include eliminating the need for spreadsheet-based formulas and macros, improving accuracy by reducing manual input errors, and saving an estimated 2–4 hours per submission. While this proof-of-concept focused on a common challenge in genomic data submission, the solution has broad applicability across multiple genomics data interfaces.

As genomic sequencing continues to play a central role in infectious disease surveillance and clinical diagnostics, the need for efficient data transformation processes will only expand. The collaboration between DxHub and public health laboratories showcases how generative AI can address complex interoperability challenges while maintaining the rigorous standards required for scientific research.

To learn more about the AI Genomics Schema Harmonizer and how it can support your laboratory or agency, please contact **Dr. Kelsey Florek** at [Kelsey.Florek@slh.wisc.edu](mailto:Kelsey.Florek@slh.wisc.edu).

**Contributing authors:** Nick Osterbur, Dr. Dawn Heisey-Grove, and Darren Kraker

### **About Cal Poly DxHub**

Launched in 2017 as the first Cloud Innovation Center (CIC) located at a higher-education institution, the Cal Poly DxHub provides opportunities for nonprofits, educational institutions, and government organizations to collaborate on critical challenges, experiment with new ideas, and leverage AWS technical expertise to build cloud-based solutions. To learn more about the Cal Poly Digital Transformation Hub and how your organization can get involved, contact Nick Osterbur (nosterb@amazon.com) or visit the [DxHub website](https://dxhub.calpoly.edu/).

[Learn more about the AWS Cloud Innovation Centers program](https://aws.amazon.com/government-education/cloud-innovation-centers/).

TAGS: [Amazon API Gateway](https://aws.amazon.com/blogs/publicsector/tag/amazon-api-gateway/), [Artificial Intelligence](https://aws.amazon.com/blogs/publicsector/tag/artificial-intelligence/), [AWS Cloud Innovation Center](https://aws.amazon.com/blogs/publicsector/tag/aws-cloud-innovation-center/), [aws Lambda](https://aws.amazon.com/blogs/publicsector/tag/aws-lambda/), [AWS Public Sector](https://aws.amazon.com/blogs/publicsector/tag/aws-public-sector/), [Cal Poly](https://aws.amazon.com/blogs/publicsector/tag/cal-poly/), [customer story](https://aws.amazon.com/blogs/publicsector/tag/customer-story/), [healthcare](https://aws.amazon.com/blogs/publicsector/tag/healthcare/), [life sciences](https://aws.amazon.com/blogs/publicsector/tag/life-sciences/)

![image3](/images/3-BlogsTranslated/blog2/3.png)  
**Noor Dhaliwal**  
Noor is a Computer Engineering student at California Polytechnic State University, San Luis Obispo, and currently serves as a software engineering intern at the Cal Poly AWS Cloud Innovation Center (CIC). His work focuses on developing technical solutions to address complex challenges faced by public sector organizations.

![image4](/images/3-BlogsTranslated/blog2/4.png)  
**Dr. Kelsey Florek**  
Kelsey is a senior genomics and data scientist who leads the Bioinformatics Team within the Communicable Disease Division at the Wisconsin State Laboratory of Hygiene. Her work focuses on expanding equitable access to genomic data analytics and enhancing genomics integration in public health practice. She works closely with public health partners to build workforce capacity and promote the adoption of actionable genomic insights in disease surveillance and response.

![image5](/images/3-BlogsTranslated/blog2/5.png)  
**Logan Fink**  
Logan is the bioinformatics lead scientist in the Division of Consolidated Laboratory Services (DCLS) at the Department of General Services (DGS). He also serves as the Bioinformatic Regional Resource for the mid-Atlantic region of state public health laboratories, where he coordinates training and provides expertise in public health bioinformatics. Logan is passionate about advancing public health initiatives by exploring ways to leverage cloud technologies and fostering innovative approaches to problem solving.
