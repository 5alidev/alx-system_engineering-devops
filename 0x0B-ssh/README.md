# 0x0B. SSH

This repository contains solutions to the SSH project tasks.

## Tasks

### 0. Use a private key
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

**Requirements:**
- Only use ssh single-character flags
- Cannot use -l
- Do not need to handle the case of a private key protected by a passphrase

### 1. Create an SSH key pair
Write a Bash script that creates an RSA key pair.

**Requirements:**
- Name of the created private key must be school
- Number of bits in the created key to be created 4096
- The created key must be protected by the passphrase betty

### 2. Client configuration file
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

**Requirements:**
- SSH client configuration must be configured to use the private key ~/.ssh/school
- SSH client configuration must be configured to refuse to authenticate using a password

### 3. Let me in!
Now that you have successfully connected to your server, we would also like to join the party. Add the SSH public key below to your server so that we can connect using the ubuntu user.

## Author
Created by [Khalid Benhamou]