# 0. Simple web stack
![simple web stack](https://github.com/5alidev/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.png?raw=true)

## Descripttion:
This web infrastructure consists of one server with Nginx as the web server, handling HTTP requests. It also includes an application server for executing application logic, alongside the application code files. The MySQL database stores and manages the application's data. The domain name, foobar.com, is configured with a www record pointing to the server's IP address, 8.8.8.8. However, this setup may face challenges such as single points of failure, downtime during maintenance, and limitations in scaling to handle high traffic.

## What is a server?
A server is a computer program or hardware device that provides functionality or services to other computers or users within a network.

## What is the role of the domain name?
The role of the domain name is to provide a human-friendly way to access resources on the internet, like websites and email servers, by using easy-to-remember names instead of complex numerical IP addresses.

## What type of DNS record www is in www.foobar.com?
In the domain name "www.foobar.com," "www" is typically an A record (Address record), which maps a domain name to an IPv4 address.

## What is the role of the web server?
The role of a web server is to handle HTTP requests from clients (like web browsers) and respond by sending back web pages or other resources requested by the clients.

## What is the role of the application server?
The role of an application server is to provide access to business logic and application functionality for client applications.

## What is the role of the database?
The role of a database is to store, organize, manage, and retrieve structured information or data. It provides a structured format for storing data, allowing users to easily access, modify, and manage the data according to their needs

## What is the server using to communicate with the computer of the user requesting the website?
The server communicates with the computer of the user requesting the website using the HTTP (Hypertext Transfer Protocol) protocol.

# The issues with this infrastructure:
## SPOF
Single Point of Failure (SPOF): The infrastructure has a single server, which means that if this server fails for any reason (hardware failure, software crash, etc.), the entire system will go down, resulting in downtime for the website.

## Downtime when maintenance needed
Downtime during Maintenance: When maintenance is needed, such as deploying new code that requires restarting the web server (Nginx), the website will experience downtime during the restart process. This can lead to inconvenience for users and potential loss of business.

## Cannot scale if too much incoming traffic
With only one server and one application server, the infrastructure cannot easily scale to handle a large influx of incoming traffic. As traffic increases, the server may become overloaded, leading to slower performance or even crashes.
