# End-to-End-DevOps-Project-Terraform-Ansible-Docker-on-AWS
End-to-End DevOps Project: Terraform + Ansible + Docker on AWS

This repository demonstrates a **complete, real-world DevOps workflow** using **Terraform** for infrastructure provisioning and **Ansible** for configuration management and application deployment.

The goal of this project is that **anyone — even on their first attempt — can clone this repo, follow the steps, and successfully deploy the application**. This is one of my initial projects that I have done while learning devops from scratch.

---

## 📌 What You Will Build

You will build an automated system that:

* Provisions AWS infrastructure using Terraform
* Creates a secure VPC with public and private subnets
* Uses a Bastion Host as an Ansible Control Node
* Configures servers using Ansible
* Installs Docker, Nginx, and a database
* Builds and runs a Dockerized application
* Manages variables and secrets cleanly

This project reflects **how DevOps is done in real companies**, not toy examples.

---

## 🧠 Architecture Overview

```
Local Machine
     │
     │ SSH
     ▼
Bastion Host (Public Subnet)
     │
     │ Ansible / SSH
     ▼
Application Server (Private Subnet)
     │
     │ DB Connection
     ▼
Database Server (Private Subnet)
```

### Key Design Choices

* **Private subnets** for App & DB (security best practice)
* **NAT Gateway** for outbound internet access
* **No direct SSH** to private instances
* **Bastion host** as single entry point

---

## 🛠 Tools & Technologies

| Tool          | Purpose                      |
| ------------- | ---------------------------- |
| AWS EC2       | Compute                      |
| AWS VPC       | Networking                   |
| Terraform     | Infrastructure provisioning  |
| Ansible       | Configuration management     |
| Docker        | Application containerization |
| Nginx         | Web server                   |
| MariaDB       | Database (MySQL-compatible)  |
| Ansible Vault | Secrets management           |

---

## 📁 Repository Structure

```
.
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│
├── ansible-practice/
│   ├── inventory.ini
│   ├── site.yml
│   ├── vars/
│   │   ├── common.yml
│   │   ├── app.yml
│   │   └── db.yml
│   ├── secrets/
│   │   └── vault.yml
│   ├── app/
│   │   ├── Dockerfile
│   │   └── app.py
│
└── README.md
```

---

## ⚙️ Prerequisites

Before starting, ensure you have:

* AWS Account
* IAM user with EC2, VPC permissions
* Terraform installed (>= 1.3) on local machine
* SSH key pair
* Basic Linux knowledge

---

## 🏗 Step 1: Provision Infrastructure with Terraform

### 1. Go to Terraform directory

```bash
cd terraform
```

### 2. Initialize Terraform

```bash
terraform init
```

### 3. Review the plan

```bash
terraform plan
```

### 4. Apply the configuration

```bash
terraform apply
```

Terraform will create:

* VPC
* Subnets
* NAT Gateway
* Bastion, App, DB EC2 instances

> ⚠️ Save the **private IPs** of App and DB instances from Terraform outputs.

---

## 🔐 Step 2: Setup Ansible Control Node (Bastion)

SSH into Bastion:

```bash
ssh -i key.pem ec2-user@<BASTION_PUBLIC_IP>
```

Install Ansible:

```bash
sudo yum install ansible -y
```

---

## 📋 Step 3: Configure Ansible Inventory

Edit `inventory.ini`:

```ini
[bastion]
bastion ansible_connection=local

[app]
app ansible_host=<APP_PRIVATE_IP>

[db]
db ansible_host=<DB_PRIVATE_IP>

[all:vars]
ansible_user=ec2-user
ansible_ssh_private_key_file=~/.ssh/id_rsa
```

---

## 🔑 Step 4: Setup Passwordless SSH

From Bastion:

```bash
ssh-keygen
ssh-copy-id ec2-user@<APP_PRIVATE_IP>
ssh-copy-id ec2-user@<DB_PRIVATE_IP>
```

Verify:

```bash
ssh ec2-user@<APP_PRIVATE_IP>
```

---

## 🔒 Step 5: Configure Ansible Vault (Secrets)

Create vault file:

```bash
ansible-vault create secrets/vault.yml
```

Example contents:

```yaml
db_password: StrongPassword123
app_secret_key: supersecretkey
```

---

## 🧩 Step 6: Understand Variables Structure

### vars/common.yml

Used across all nodes

```yaml
common_packages:
  - git
  - curl
```

### vars/app.yml

Application-specific config

```yaml
app_dir: /opt/learning-app
docker_image: learning-app
docker_container: learning-app-container
app_port: 8080
```

### vars/db.yml

Database connection details

```yaml
db_name: learningdb
db_user: appuser
db_port: 3306
```

---

## ▶️ Step 7: Run the Ansible Playbook

```bash
ansible-playbook -i inventory.ini site.yml --ask-vault-pass
```

This will:

* Install Docker & Nginx on App server
* Install MariaDB on DB server
* Build Docker image
* Run the application container

---

## 🌐 Step 8: Access the Application

The application runs in a **private subnet**, so it is not directly accessible.

### Use SSH Port Forwarding

From your local machine:

```bash
ssh -i key.pem -L 8080:localhost:8080 ec2-user@<BASTION_PUBLIC_IP>
```

Open browser:

```
http://localhost:8080
```

---

## ✅ Step 9: Verify Without SSH (Recommended)

```bash
ansible app -i inventory.ini -m command -a "docker ps"
ansible app -i inventory.ini -m command -a "curl localhost:8080"
```

---

## ❗ Common Mistakes & Fixes

| Problem                  | Cause                    | Fix                        |
| ------------------------ | ------------------------ | -------------------------- |
| Docker permission denied | User not in docker group | Re-login or newgrp docker  |
| db_user undefined        | vars/db.yml not loaded   | Add vars_files to App play |
| nginx install fails      | Repo not enabled         | Enable amazon-linux-extras |

---

## 🎯 Key Learnings

* Infrastructure and configuration must be separated
* Private subnet architecture improves security
* Ansible Vault is essential for secrets
* Docker permissions require Linux group understanding
* SSH is for debugging, not scaling

---

## 🧠 Why This Project Matters

This project demonstrates:

* Real AWS networking patterns
* Proper Ansible variable scoping
* Secure secret handling
* Scalable automation practices

It is **interview-ready** and **industry-aligned**.

---

## 🏁 Final Notes

If you can complete this project end-to-end, you are **not a beginner** anymore.

Feel free to fork, modify, and extend this project.

---

⭐ **If this project helped you learn, consider starring the repo!**
