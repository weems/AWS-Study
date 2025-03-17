# Additional AWS Cloud Practitioner Exam Study Resources

## Key Exam Information

- **Exam Code:** CLF-C02
- **Questions:** 65 multiple-choice/multiple-response
- **Time Limit:** 90 minutes
- **Passing Score:** 700/1000
- **Cost:** $100 USD
- **Format:** Online or testing center
- **Language:** Available in multiple languages

## Core Domains and Weightings

1. **Cloud Concepts (24%)**
   - Define the AWS Cloud and its value proposition
   - Identify aspects of AWS Cloud economics
   - Describe different cloud architecture design principles

2. **Security and Compliance (30%)**
   - Define the AWS shared responsibility model
   - Define AWS Cloud security and compliance concepts
   - Identify AWS access management capabilities
   - Identify resources for security support

3. **Technology (33%)**
   - Define methods of deploying and operating in the AWS Cloud
   - Define the AWS global infrastructure
   - Identify core AWS services
   - Identify resources for technology support

4. **Billing and Pricing (16%)**
   - Compare and contrast various pricing models for AWS
   - Recognize various account structures in relation to AWS billing and pricing
   - Identify resources available for billing support

## Study Strategies

### For Visual Learners
- Create mind maps of AWS service categories
- Draw the AWS shared responsibility model
- Sketch the AWS global infrastructure (regions, AZs, edge locations)
- Watch AWS YouTube videos and training

### For Auditory Learners
- Explain concepts out loud
- Discuss AWS topics with colleagues or study groups
- Use audio recordings to review key concepts
- Try teaching concepts to others

### For Reading/Writing Learners
- Write summaries of key services
- Create comparison tables for similar services
- Take detailed notes from AWS documentation
- Write practice questions

### For Kinesthetic Learners
- Set up free tier AWS account and practice using services
- Complete AWS hands-on labs
- Build simple projects using AWS services
- Use AWS interactive training tools

## Memory Techniques

### Acronyms

**SPEAR** for AWS advantages:
- **S**ecurity
- **P**erformance
- **E**lasticity
- **A**vailability
- **R**eliability

**CUPS** for what you don't manage with AWS:
- **C**apital expenses
- **U**tility bills
- **P**hysical security
- **S**erver maintenance

**DR McPASS** for AWS storage services:
- **D**ynamoDB (NoSQL)
- **R**DS (relational)
- **M**emory DB/ElastiCache (in-memory)
- **C**loud Directory
- **P**arameter Store
- **A**urora (MySQL/PostgreSQL compatible)
- **S**3 (object storage)
- **S**torage Gateway (hybrid)

### Analogies

- **EC2 is like renting a computer** - You decide on size, OS, and configuration
- **S3 is like a unlimited filing cabinet** - Store any number of files of any size
- **RDS is like hiring a database administrator** - Manages backups, updates, etc.
- **CloudFront is like having copies of your book in libraries worldwide** - Content closer to users

## Common Exam Scenarios

1. **Company migrating from on-premises to AWS**
   - Focus on migration strategies, cost benefits, and security considerations

2. **Designing fault-tolerant architectures**
   - Multiple AZs, regions, backups, and disaster recovery

3. **Optimizing costs on AWS**
   - Reserved Instances, Savings Plans, S3 storage classes, right-sizing

4. **Securing AWS resources**
   - IAM policies, least privilege, MFA, encryption, VPC security

5. **Supporting global users**
   - CloudFront, Route 53, regional deployment, edge locations

## Quick Reference Tables

### EC2 Instance Purchasing Options

| Option | Best For | Payment Model | Price Discount | Commitment |
|--------|----------|---------------|----------------|------------|
| On-Demand | Variable workloads | Pay-as-you-go | None | None |
| Spot | Interruptible workloads | Variable (market-based) | Up to 90% | None |
| Reserved | Steady-state workloads | Partial upfront, all upfront, no upfront | Up to 72% | 1 or 3 years |
| Savings Plans | Flexible compute usage | Hourly commitment | Up to 72% | 1 or 3 years |
| Dedicated | Compliance/licensing | Premium pricing | Varies | Varies |

### Storage Options Comparison

| Service | Type | Use Cases | Performance | Durability |
|---------|------|-----------|-------------|------------|
| S3 | Object | Static files, backups | Moderate | 99.999999999% |
| EBS | Block | EC2 instance storage | High | 99.999% |
| EFS | File | Shared file storage | Moderate | High |
| S3 Glacier | Object Archive | Long-term archival | Low (minutes to hours) | 99.999999999% |
| Snow Family | Physical | Large data migration | Varies | N/A |

###