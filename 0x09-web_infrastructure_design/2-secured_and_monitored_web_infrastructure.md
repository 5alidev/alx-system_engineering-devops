# 2. Secured and monitored web infrastructure
![Secured and monitored web infrastructure](https://github.com/5alidev/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png?raw=true)

## Description
In our enhanced infrastructure, we've bolstered security and monitoring capabilities with the addition of three firewalls, ensuring better protection against unauthorized access. Furthermore, by implementing an SSL certificate, we've enabled HTTPS encryption for www.foobar.com, enhancing data security during transmission. To stay on top of system health and performance, we've integrated three monitoring clients, facilitating data collection for services like Sumo Logic, which enables proactive monitoring and timely detection of any anomalies or issues.

## Added Elements
### Firewalls:
We're adding firewalls to enhance security by controlling incoming and outgoing network traffic, thus safeguarding against unauthorized access and potential cyber threats.

### SSL Certificate:
The SSL certificate is being implemented to enable HTTPS encryption for www.foobar.com, ensuring secure communication between the server and users' browsers, thereby protecting sensitive data from interception or tampering.

### Monitoring:
We're incorporating monitoring clients to collect data for services like Sumo Logic, enhancing our ability to monitor system health, detect anomalies, and promptly address any issues, thereby improving overall performance and reliability.

## What are firewalls for?
Firewalls are network security devices or software applications designed to monitor and control incoming and outgoing traffic based on predetermined security rules. They act as barriers between trusted internal networks and untrusted external networks.

## Why is the traffic served over HTTPS?
Traffic is served over HTTPS to ensure secure communication between the client (such as a web browser) and the server. HTTPS (Hypertext Transfer Protocol Secure) encrypts the data transmitted between the client and server, providing confidentiality and integrity.

## What monitoring is used for?
Monitoring is used to keep track of the health, performance, and availability of various components within a system or network. It involves collecting and analyzing data from servers, applications, databases, and other infrastructure elements to ensure they are functioning as expected.

## How the monitoring tool is collecting data?
Monitoring tools collect data by continuously querying or polling various metrics from the components they are monitoring. This process involves sending requests to the target systems or devices and retrieving specific information, such as CPU usage, memory utilization, network traffic, disk I/O, application performance metrics, error logs, and more.

## Explain what to do if you want to monitor your web server QPS?
To monitor your web server's QPS, first, choose a monitoring tool like Prometheus or Datadog. Install the monitoring agent on your web server and configure it to collect QPS metrics. Set up alerts to notify you of any unusual spikes in traffic. Visualize the metrics using the monitoring tool's dashboard to track QPS over time. Regularly analyze the data to optimize server performance and ensure it can handle incoming traffic effectively.

## the issues with this infrastructure
Terminating SSL at the load balancer level poses a security risk because the decrypted traffic is then transmitted in plain text within the internal network, potentially exposing sensitive information to unauthorized access.

Having only one MySQL server capable of accepting writes creates a single point of failure (SPOF), as any failure in the MySQL server could result in downtime and data loss.

Having servers with all the same components might be a problem because it increases homogeneity, making the infrastructure vulnerable to widespread failures or security breaches if a vulnerability affects all instances of a particular component.
