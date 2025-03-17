# AWS Cloud Practitioner Practice Questions - Answer Key

## AWS Cloud Design Principles

1. Which of the following are key AWS cloud design principles? (Select TWO)
   - **Answer: B, C**
   - **B. Implement infrastructure automation**
   - **C. Test systems at production scale**
   - Explanation: AWS promotes automating infrastructure deployment and testing systems at production scale before deployment as key design principles within the Well-Architected Framework.

2. According to AWS Well-Architected Framework, which principle helps organizations avoid costly overprovisioning?
   - **Answer: B**
   - **B. Implement elasticity**
   - Explanation: Elasticity allows systems to automatically scale up or down based on demand, preventing overprovisioning and reducing costs.

## Cost Optimization & Purchase Options

3. A company has a workload that runs constantly with steady usage for the next 3 years. Which purchase option would be most cost-effective?
   - **Answer: C**
   - **C. Reserved Instances**
   - Explanation: For steady, predictable workloads running for extended periods (1-3 years), Reserved Instances offer the highest discount (up to 72%) compared to On-Demand pricing.

4. Which of the following purchase options would be best for a batch processing workload that can be interrupted and resumed without issues?
   - **Answer: B**
   - **B. Spot Instances**
   - Explanation: Spot Instances provide the largest discount (up to 90%) for workloads that can handle interruptions, making them ideal for batch processing jobs that can be resumed.

5. A company uses a mix of Amazon EC2, AWS Lambda, and AWS Fargate. Which purchase option would provide the best flexibility and cost savings across these compute services?
   - **Answer: B**
   - **B. Compute Savings Plans**
   - Explanation: Compute Savings Plans offer flexibility across EC2, Lambda, and Fargate while providing savings of up to 66%. Unlike Reserved Instances, they apply to multiple compute services.

## Database Services

6. A company wants to migrate its on-premises PostgreSQL database to AWS with minimal management overhead. Which TWO services would meet this requirement? (Select TWO)
   - **Answer: A, C**
   - **A. Amazon RDS for PostgreSQL**
   - **C. Amazon Aurora PostgreSQL**
   - Explanation: Both Amazon RDS for PostgreSQL and Amazon Aurora PostgreSQL are managed database services compatible with PostgreSQL, requiring minimal management overhead compared to self-hosted options.

7. Which AWS database service provides automatic scalability, high availability, and enterprise-grade reliability while being compatible with PostgreSQL?
   - **Answer: B**
   - **B. Amazon Aurora**
   - Explanation: Amazon Aurora is designed for automatic scalability, high availability (99.99%), and enterprise reliability while maintaining PostgreSQL compatibility.

## Monitoring, Logging, and Auditing

8. A security team needs to review who made specific API calls in their AWS account. Which service should they use?
   - **Answer: B**
   - **B. AWS CloudTrail**
   - Explanation: CloudTrail records API calls and account activities, providing the audit trail needed to identify who made specific API calls.

9. Which AWS service allows you to set alarms when your AWS resources exceed defined thresholds?
   - **Answer: C**
   - **C. Amazon CloudWatch**
   - Explanation: CloudWatch enables setting alarms based on metrics and thresholds for AWS resources, triggering notifications or automated actions when thresholds are exceeded.

10. A company wants recommendations on potential security vulnerabilities, cost optimizations, and performance improvements. Which service should they use?
    - **Answer: B**
    - **B. AWS Trusted Advisor**
    - Explanation: Trusted Advisor provides recommendations across five categories: cost optimization, security, fault tolerance, performance, and service limits.

## Identity and Access Management

11. Which of the following is TRUE about the AWS account root user?
    - **Answer: B**
    - **B. It cannot be deleted or disabled**
    - Explanation: The root user is the account owner and cannot be deleted or fully disabled, though its access can be restricted by following security best practices.

12. A company wants to allow their customers to log in to their web application using their Google and Facebook accounts. Which AWS service should they use?
    - **Answer: B**
    - **B. Amazon Cognito**
    - Explanation: Amazon Cognito provides user identity and authentication capabilities for applications, supporting social identity providers like Google and Facebook.

## Networking Concepts

13. To make a subnet public, which TWO resources must be configured? (Select TWO)
    - **Answer: B, D**
    - **B. Internet Gateway**
    - **D. Route Table**
    - Explanation: A subnet becomes public when it has an Internet Gateway attached to the VPC and a route table entry directing traffic (0.0.0.0/0) to that Internet Gateway.

14. Which AWS networking component acts as a firewall at the instance level and only supports allow rules?
    - **Answer: B**
    - **B. Security Group**
    - Explanation: Security Groups act as instance-level firewalls that only support allow rules (stateful) and implicitly deny all traffic not explicitly allowed.

## AWS Architecture

15. Which statement correctly describes an AWS Region?
    - **Answer: C**
    - **C. A geographic area with multiple isolated Availability Zones**
    - Explanation: An AWS Region is a geographic area containing multiple Availability Zones that are isolated but connected via low-latency links.

16. Which AWS services can help achieve a loosely coupled architecture? (Select TWO)
    - **Answer: B, C**
    - **B. Amazon Simple Queue Service (SQS)**
    - **C. AWS Step Functions**
    - Explanation: SQS enables message-based decoupling between components, while Step Functions coordinates multiple services into serverless workflows without tight coupling.

## AWS Shared Responsibility Model

17. According to the AWS Shared Responsibility Model, which of the following is AWS responsible for?
    - **Answer: D**
    - **D. Physical security of data centers**
    - Explanation: AWS is responsible for the "security OF the cloud," which includes physical security of data centers, while customers are responsible for security IN the cloud.

18. A company is running a containerized application on Amazon ECS. According to the AWS Shared Responsibility Model, what is the customer responsible for? (Select TWO)
    - **Answer: A, C**
    - **A. Container security configuration**
    - **C. Data encryption**
    - Explanation: Under the shared responsibility model, customers are responsible for securing their container configurations and encrypting their data.

## Storage Solutions

19. A company wants to extend its on-premises tape backup system to AWS for long-term archival. Which service should they use?
    - **Answer: B**
    - **B. AWS Storage Gateway**
    - Explanation: AWS Storage Gateway's Tape Gateway configuration specifically addresses the need to extend on-premises tape backup systems to the AWS cloud.

20. Which AWS storage service would be most appropriate for storing immutable objects like images, videos, and log files?
    - **Answer: C**
    - **C. Amazon S3**
    - Explanation: Amazon S3 is an object storage service designed for storing and retrieving any amount of data, making it ideal for immutable objects like media files and logs.

## General Questions

21. Which AWS service provides pay-as-you-go pricing with no minimum commitments?
    - **Answer: D**
    - **D. Amazon EC2 On-Demand Instances**
    - Explanation: EC2 On-Demand Instances charge by the second with no long-term commitments or upfront payments required.

22. Which AWS service helps you organize and manage multiple AWS accounts under a single administrative entity?
    - **Answer: B**
    - **B. AWS Organizations**
    - Explanation: AWS Organizations allows you to consolidate multiple AWS accounts into an organization that you create and centrally manage.

23. A company wants to protect their web application from common web exploits like SQL injection and cross-site scripting. Which AWS service should they use?
    - **Answer: C**
    - **C. AWS WAF**
    - Explanation: AWS Web Application Firewall (WAF) is designed to protect web applications from common web exploits like SQL injection and cross-site scripting (XSS).
