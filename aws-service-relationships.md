# AWS Service Relationships and Connections

## Monitoring, Logging, and Security Triad

**CloudWatch + CloudTrail + Config**
- **CloudWatch**: Monitors performance (what's happening now)
- **CloudTrail**: Records API activity (who did what and when)
- **Config**: Tracks resource configurations (what changed and compliance status)

**How they work together:**
1. CloudTrail logs show who made an API call to modify a resource
2. Config shows the configuration change that resulted
3. CloudWatch shows the performance impact of that change

**Real-world example:** A developer inadvertently modifies a security group to open port 22 to the world (0.0.0.0/0):
- CloudTrail records who made the API call and when
- Config shows the security group configuration changed from restricted to open
- CloudWatch could alert if suspicious traffic increases on port 22

## Security Services Ecosystem

**IAM + Shield + WAF + GuardDuty**
- **IAM**: Controls who can access what (authentication and authorization)
- **Shield**: Protects against DDoS attacks (network/transport layer)
- **WAF**: Filters malicious web traffic (application layer)
- **GuardDuty**: Detects suspicious activity and behavior

**Working together:**
1. IAM ensures only authorized users access resources
2. Shield protects infrastructure from volumetric attacks
3. WAF filters out application-level attacks
4. GuardDuty monitors for unusual patterns indicating compromise

## Storage Service Tiers

**S3 + Glacier + Storage Gateway**
- **S3**: Primary object storage for active data
- **Glacier**: Long-term archival of infrequently accessed data
- **Storage Gateway**: Connects on-premises systems to AWS storage

**Working together:**
1. Frequently accessed data stays in S3 Standard
2. Data accessed less often moves to S3 Standard-IA or One Zone-IA
3. Rarely accessed data archives to Glacier or Glacier Deep Archive
4. Storage Gateway provides local access to cloud data

## Compute and Auto Scaling Group

**EC2 + Auto Scaling + Load Balancer**
- **EC2**: Virtual servers for computing capacity
- **Auto Scaling**: Automatically adjusts capacity based on demand
- **ELB**: Distributes incoming traffic across multiple targets

**Working together:**
1. Load Balancer receives incoming requests
2. Distributes traffic across multiple EC2 instances
3. Auto Scaling adds/removes instances based on load
4. Health checks remove unhealthy instances from service

## Database Services Ecosystem

**RDS + DynamoDB + ElastiCache**
- **RDS**: Managed relational databases for structured data
- **DynamoDB**: NoSQL database for flexible schema requirements
- **ElastiCache**: In-memory cache for high-performance data access

**Working together:**
1. RDS stores structured application data
2. DynamoDB handles high-throughput, schema-less data needs
3. ElastiCache caches frequent queries to reduce database load

## Serverless Architecture Components

**Lambda + API Gateway + DynamoDB**
- **Lambda**: Run code without provisioning servers
- **API Gateway**: Create, publish, and secure APIs
- **DynamoDB**: NoSQL database with single-digit millisecond performance

**Working together:**
1. API Gateway receives and validates API requests
2. Triggers Lambda functions to process requests
3. Lambda reads/writes data to DynamoDB
4. No servers to manage throughout the entire flow

## Network Security Layers

**VPC + Security Groups + Network ACLs**
- **VPC**: Isolated network environment for resources
- **Security Groups**: Instance-level firewall (stateful)
- **Network ACLs**: Subnet-level firewall (stateless)

**Working together:**
1. VPC provides network isolation
2. Network ACLs filter traffic at the subnet boundary
3. Security Groups filter traffic at the instance level
4. Defense in depth with multiple security layers

## Content Delivery and DNS

**CloudFront + Route 53 + S3**
- **CloudFront**: Global content delivery network
- **Route 53**: DNS service and domain registration
- **S3**: Object storage for static content

**Working together:**
1. S3 stores static website content
2. CloudFront caches content at edge locations worldwide
3. Route 53 routes users to the nearest CloudFront edge location

## Identity Management for Applications

**Cognito + IAM + Directory Service**
- **Cognito**: Customer identity management
- **IAM**: AWS service access control
- **Directory Service**: Enterprise directory integration

**Working together:**
1. Cognito handles customer/external user authentication
2. IAM manages internal users and service authorization
3. Directory Service connects to existing enterprise directories

## Cost Management Suite

**Cost Explorer + Budgets + Trusted Advisor**
- **Cost Explorer**: Visualize and analyze costs
- **Budgets**: Set cost thresholds and alerts
- **Trusted Advisor**: Recommendations for cost optimization

**Working together:**
1. Cost Explorer identifies spending patterns and trends
2. Budgets set thresholds to control spending
3. Trusted Advisor suggests specific cost-saving opportunities
