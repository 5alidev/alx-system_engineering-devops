# 1. Distributed web infrastructure
![Distributed web infrastructure](https://github.com/5alidev/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png?raw=true)

## Description:
With the addition of a second server and the implementation of a load balancer (HAproxy), this infrastructure now offers improved reliability and scalability. The load balancer distributes incoming traffic across the two servers, enhancing fault tolerance by eliminating single points of failure.

## Additional Elements
### Second Server
Adding a second server improves reliability and fault tolerance by providing redundancy. If one server fails, the other can continue to handle incoming requests, reducing the risk of downtime.

### Load Balancer (HAproxy)
Introducing a load balancer allows for the distribution of incoming traffic across multiple servers. This enhances scalability and performance by evenly distributing the workload and preventing any single server from becoming overwhelmed.

## What distribution algorithm your load balancer is configured with and how it works?
The load balancer is configured with a round-robin distribution algorithm. This algorithm works by sequentially routing incoming requests to each server in a rotation. For example, if there are three servers in the pool, the first request goes to server 1, the second request goes to server 2, and the third request goes to server 3. Subsequent requests continue in the same sequence. This distribution method ensures that the workload is evenly distributed among all servers, preventing any single server from being overwhelmed while maximizing resource utilization.

## Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both?
Our load balancer is configured with an Active-Active setup. In an Active-Active setup, all servers in the pool actively handle incoming requests simultaneously. This means that each server actively participates in processing traffic, distributing the workload across multiple servers to increase efficiency and scalability.

On the other hand, an Active-Passive setup involves one server actively handling requests while the others remain in standby mode, ready to take over if the active server fails. In this setup, only one server is actively processing traffic at any given time, with the passive servers serving as backups.

## How a database Primary-Replica (Master-Slave) cluster works?
In a Primary-Replica (Master-Slave) database cluster setup, there are two types of nodes: the primary node (also known as the master) and one or more replica nodes (also known as slaves).

In a Primary-Replica (Master-Slave) database cluster, the primary node handles all writes, while replica nodes copy its data for reading. Write operations are replicated to the replicas, ensuring data consistency. If the primary fails, a replica can take over. This setup provides fault tolerance and scalability, improving read performance.

## The Issues with this infrastructure
### SPOF
Single Point of Failure (SPOF) exists due to a single load balancer and potential hardware failures.

### Security issues
Security issues arise from the absence of a firewall and HTTPS, exposing the system to external threats.

### No monitoring
Lack of monitoring makes it difficult to detect and address performance issues, potential breaches, or system failures promptly.
