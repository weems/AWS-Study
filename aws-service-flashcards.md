# AWS Service Flashcards - Primary Functions

## Compute Services

**Amazon EC2 (Elastic Compute Cloud)**
- Virtual servers in the cloud
- Resizable compute capacity
- Complete control over computing resources
- Multiple purchasing options (On-Demand, Reserved, Spot, Dedicated Hosts)

**AWS Lambda**
- Run code without provisioning or managing servers
- Pay only for compute time consumed
- Scales automatically
- Event-driven execution

**Amazon ECS (Elastic Container Service)**
- Fully managed container orchestration service
- Runs Docker containers
- Integrates with AWS ecosystem
- Eliminates need to operate container orchestration software

**Amazon EKS (Elastic Kubernetes Service)**
- Managed Kubernetes service
- Runs Kubernetes without installing/maintaining Kubernetes control plane
- Certified Kubernetes conformant
- Integrates with AWS services for observability and security

**Amazon Lightsail**
- Simplified virtual private server solution
- Low, predictable pricing
- Includes compute, storage, and networking
- Easy for developers, small businesses, students, and hobbyists

## Storage Services

**Amazon S3 (Simple Storage Service)**
- Object storage with industry-leading scalability and durability
- Store any amount of data
- 99.999999999% durability
- Various storage classes for different access patterns

**Amazon EBS (Elastic Block Store)**
- Persistent block storage volumes for EC2 instances
- Independent lifecycle from instances
- Automatic replication within Availability Zones
- Different volume types for various workloads

**Amazon EFS (Elastic File System)**
- Fully managed NFS file system
- Elastic capacity that grows and shrinks automatically
- Shared access for multiple EC2 instances
- Regional service with multi-AZ resilience

**AWS Storage Gateway**
- Hybrid cloud storage service
- Connect on-premises environments with AWS storage
- File, volume, and tape gateway types
- Local caching for low-latency access to frequently used data

**Amazon S3 Glacier**
- Low-cost archive storage
- Long-term data retention
- Various retrieval options (minutes to hours)
- 99.999999999% durability

## Database Services

**Amazon RDS (Relational Database Service)**
- Managed relational database service
- Supports multiple database engines (MySQL, PostgreSQL, Oracle, SQL Server, MariaDB)
- Automated backups, patching, and scaling
- Multi-AZ deployments for high availability

**Amazon Aurora**
- MySQL and PostgreSQL-compatible relational database
- 5x performance of standard MySQL, 3x of PostgreSQL
- Distributed, fault-tolerant, self-healing storage
- Up to 15 read replicas with minimal lag

**Amazon DynamoDB**
- Fully managed NoSQL database
- Single-digit millisecond performance
- Serverless with automatic scaling
- Multi-region, multi-master capabilities

**Amazon Redshift**
- Fully managed data warehouse
- Query petabytes of structured data
- Columnar storage technology
- Optimize for analytics workloads

**Amazon ElastiCache**
- In-memory caching service
- Redis and Memcached compatible
- Microsecond response times
- Improves application performance

## Networking & Content Delivery

**Amazon VPC (Virtual Private Cloud)**
- Isolated section of AWS cloud
- Complete control over virtual networking environment
- Multiple layers of security
- Connect to your data center with VPN or Direct Connect

**Amazon CloudFront**
- Global content delivery network (CDN)
- Low-latency content delivery
- DDoS protection integration
- Pay-as-you-go pricing model

**Amazon Route 53**
- Highly available and scalable Domain Name System (DNS)
- Domain registration
- Health checking and routing policies
- Integrates with other AWS services

**AWS Direct Connect**
- Dedicated network connection to AWS
- Reduce network costs
- Increase bandwidth
- Consistent network experience

**Elastic Load Balancing**
- Distribute incoming application traffic
- Three types: Application, Network, and Classic
- Automatically scales with traffic
- Integrates with Auto Scaling

## Security, Identity & Compliance

**AWS IAM (Identity and Access Management)**
- Manage access to AWS services
- Create and manage AWS users and groups
- Use permissions to allow/deny access
- Implement MFA for additional security

**Amazon Cognito**
- Add user sign-up/sign-in to mobile/web apps
- Social identity provider integration
- Scales to millions of users
- Support for various compliance regulations

**AWS Shield**
- DDoS protection service
- Standard protection included at no cost
- Advanced protection available for additional features
- Real-time visibility into DDoS events

**AWS WAF (Web Application Firewall)**
- Protect web applications from common exploits
- Create custom rules to block attack patterns
- Monitor web requests to your application
- Integration with CloudFront and Application Load Balancer

**AWS KMS (Key Management Service)**
- Create and control encryption keys
- Integrated with many AWS services
- Centralized key management
- FIPS 140-2 validated

## Management & Governance

**Amazon CloudWatch**
- Monitoring and observability service
- Collect and track metrics
- Collect and monitor log files
- Set alarms and automate responses

**AWS CloudTrail**
- Track user activity and API usage
- Record AWS account activity
- Keep history of events
- Simplify security analysis and compliance

**AWS Config**
- Assess, audit, and evaluate configurations
- Track configuration changes
- Evaluate compliance against desired configurations
- Troubleshoot and simplify compliance auditing

**AWS Trusted Advisor**
- Online resource to optimize AWS environment
- Real-time guidance
- Recommendations in 5 categories
- Improve security and performance

**AWS Systems Manager**
- Operational hub for AWS applications
- Group resources and take action
- Maintain security and compliance
- Automate operational tasks

## Cost Management

**AWS Cost Explorer**
- Visualize and manage AWS costs
- Analyze cost and usage data
- Create custom reports
- Forecast future costs

**AWS Budgets**
- Set custom budgets
- Track costs and usage
- Receive alerts when exceeding thresholds
- Apply to specific dimensions

**AWS Cost and Usage Report**
- Most comprehensive set of AWS cost and usage data
- Track AWS usage at hourly or daily level
- Downloads to S3 bucket
- Includes usage for all services and account identifiers
