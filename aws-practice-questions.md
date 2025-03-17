# AWS Cloud Practitioner Practice Questions

## AWS Cloud Design Principles

1. Which of the following are key AWS cloud design principles? (Select TWO)
   A. Design for fixed capacity to reduce costs
   B. Implement infrastructure automation
   C. Test systems at production scale
   D. Use only dedicated hardware for better reliability
   E. Maintain manual control of all infrastructure changes

2. According to AWS Well-Architected Framework, which principle helps organizations avoid costly overprovisioning?
   A. Build monolithic applications
   B. Implement elasticity
   C. Use only Reserved Instances
   D. Deploy all resources in a single Availability Zone

## Cost Optimization & Purchase Options

3. A company has a workload that runs constantly with steady usage for the next 3 years. Which purchase option would be most cost-effective?
   A. On-Demand Instances
   B. Spot Instances
   C. Reserved Instances
   D. Dedicated Hosts

4. Which of the following purchase options would be best for a batch processing workload that can be interrupted and resumed without issues?
   A. On-Demand Instances
   B. Spot Instances
   C. Reserved Instances
   D. Savings Plans

5. A company uses a mix of Amazon EC2, AWS Lambda, and AWS Fargate. Which purchase option would provide the best flexibility and cost savings across these compute services?
   A. Reserved Instances
   B. Compute Savings Plans
   C. EC2 Instance Savings Plans
   D. Dedicated Hosts

## Database Services

6. A company wants to migrate its on-premises PostgreSQL database to AWS with minimal management overhead. Which TWO services would meet this requirement? (Select TWO)
   A. Amazon RDS for PostgreSQL
   B. Amazon DynamoDB
   C. Amazon Aurora PostgreSQL
   D. Amazon Redshift
   E. Amazon EC2 with self-managed PostgreSQL

7. Which AWS database service provides automatic scalability, high availability, and enterprise-grade reliability while being compatible with PostgreSQL?
   A. Amazon DynamoDB
   B. Amazon Aurora
   C. Amazon Neptune
   D. Amazon ElastiCache

## Monitoring, Logging, and Auditing

8. A security team needs to review who made specific API calls in their AWS account. Which service should they use?
   A. Amazon CloudWatch
   B. AWS CloudTrail
   C. AWS Config
   D. AWS Trusted Advisor

9. Which AWS service allows you to set alarms when your AWS resources exceed defined thresholds?
   A. AWS CloudTrail
   B. AWS Config
   C. Amazon CloudWatch
   D. AWS Trusted Advisor

10. A company wants recommendations on potential security vulnerabilities, cost optimizations, and performance improvements. Which service should they use?
    A. AWS Compute Optimizer
    B. AWS Trusted Advisor
    C. AWS CloudTrail
    D. AWS Config

## Identity and Access Management

11. Which of the following is TRUE about the AWS account root user?
    A. It should be used for everyday administrative tasks
    B. It cannot be deleted or disabled
    C. It has limited access to certain AWS services
    D. Multi-factor authentication cannot be enabled for the root user

12. A company wants to allow their customers to log in to their web application using their Google and Facebook accounts. Which AWS service should they use?
    A. AWS IAM
    B. Amazon Cognito
    C. AWS Directory Service
    D. AWS IAM Identity Center

## Networking Concepts

13. To make a subnet public, which TWO resources must be configured? (Select TWO)
    A. NAT Gateway
    B. Internet Gateway
    C. VPC Endpoint
    D. Route Table
    E. Network ACL

14. Which AWS networking component acts as a firewall at the instance level and only supports allow rules?
    A. Network ACL
    B. Security Group
    C. Route Table
    D. Internet Gateway

## AWS Architecture

15. Which statement correctly describes an AWS Region?
    A. A single data center with multiple servers
    B. A collection of Edge Locations across multiple countries
    C. A geographic area with multiple isolated Availability Zones
    D. A facility used to cache content globally

16. Which AWS services can help achieve a loosely coupled architecture? (Select TWO)
    A. Amazon EC2 Auto Scaling
    B. Amazon Simple Queue Service (SQS)
    C. AWS Step Functions
    D. Amazon CloudFront
    E. AWS Trusted Advisor

## AWS Shared Responsibility Model

17. According to the AWS Shared Responsibility Model, which of the following is AWS responsible for?
    A. Customer data encryption
    B. IAM user permissions
    C. Application security
    D. Physical security of data centers

18. A company is running a containerized application on Amazon ECS. According to the AWS Shared Responsibility Model, what is the customer responsible for? (Select TWO)
    A. Container security configuration
    B. Hypervisor maintenance
    C. Data encryption
    D. Physical security of servers
    E. ECS cluster hardware maintenance

## Storage Solutions

19. A company wants to extend its on-premises tape backup system to AWS for long-term archival. Which service should they use?
    A. Amazon S3 Glacier
    B. AWS Storage Gateway
    C. Amazon EBS
    D. Amazon EFS

20. Which AWS storage service would be most appropriate for storing immutable objects like images, videos, and log files?
    A. Amazon EBS
    B. Amazon EFS
    C. Amazon S3
    D. AWS Storage Gateway

## General Questions

21. Which AWS service provides pay-as-you-go pricing with no minimum commitments?
    A. AWS Budgets
    B. AWS Cost Explorer
    C. AWS Organizations
    D. Amazon EC2 On-Demand Instances

22. Which AWS service helps you organize and manage multiple AWS accounts under a single administrative entity?
    A. AWS IAM
    B. AWS Organizations
    C. AWS Control Tower
    D. AWS Single Sign-On

23. A company wants to protect their web application from common web exploits like SQL injection and cross-site scripting. Which AWS service should they use?
    A. AWS Shield
    B. Amazon GuardDuty
    C. AWS WAF
    D. Amazon Inspector
