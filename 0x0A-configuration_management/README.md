# Configuration Management Project with Puppet

## Overview

The "Configuration Management" project aims to demonstrate the use of Puppet for managing configurations in a system environment. Puppet is a powerful configuration management tool that automates the deployment and management of software and configurations across multiple servers.

In this project, we utilize Puppet to perform various configuration management tasks, including file creation, package installation, and command execution. By leveraging Puppet's declarative language and resource model, we ensure consistent and reliable configuration across our infrastructure.

## Tasks

### Task 1: Create a File

**Requirements:**

- File path: `/tmp/school`
- File permission: `0744`
- File owner: `www-data`
- File group: `www-data`
- File content: `I love Puppet`

### Task 2: Install a Package

**Requirements:**

- Package: `flask` (from `pip3`)
- Version: `2.1.0`

### Task 3: Execute a Command

**Requirements:**

- Command: `pkill killmenow`

## Getting Started

To run the Puppet manifests for this project, follow these steps:

1. Ensure Puppet is installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the Puppet manifests.
4. Apply the manifests using the `puppet apply` command.

Example:

```bash
puppet apply site.pp

