# 🚀 Automated CI/CD Pipeline with GitHub Actions, Docker & AWS

A fully automated CI/CD pipeline that builds a Docker image, publishes it to Docker Hub, deploys it to an AWS EC2 instance over SSH, and serves the application securely through Nginx with HTTPS powered by Let's Encrypt.

---

## 📌 Project Overview

This project demonstrates an end-to-end Continuous Integration and Continuous Deployment (CI/CD) workflow.

Every time code is pushed to the GitHub repository:

1. GitHub Actions is triggered.
2. The application is built into a Docker image.
3. The Docker image is pushed to Docker Hub.
4. GitHub Actions connects securely to an AWS EC2 instance via SSH.
5. The latest Docker image is pulled.
6. The existing container is stopped and removed.
7. A new container is started automatically.
8. Nginx reverse proxies incoming requests to the Docker container.
9. HTTPS is secured using Let's Encrypt with automatic certificate renewal.

No manual deployment is required.

---

## 🏗️ Architecture

```
Developer
    │
git push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Build Docker Image
    ├── Push to Docker Hub
    └── SSH into EC2
             │
             ▼
        Docker Pull
             │
             ▼
      Restart Container
             │
             ▼
         Nginx Reverse Proxy
             │
             ▼
      HTTPS (Let's Encrypt)
             │
             ▼
         End Users
```

---

## ⚙️ Technologies Used

- GitHub Actions
- Docker
- Docker Hub
- AWS EC2
- Ubuntu Server
- Nginx
- Let's Encrypt
- Certbot
- SSH
- Git

---

## 📂 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app.py
├── .gitignore
└── README.md
```

---

## 🚀 CI/CD Workflow

Every push to the repository automatically performs the following:

- Checkout repository
- Build Docker image
- Push Docker image to Docker Hub
- Connect to EC2 over SSH
- Pull latest Docker image
- Stop previous container
- Remove old container
- Launch updated container
- Serve application through Nginx
- HTTPS remains active via Let's Encrypt

---

## 🔒 Security

The deployment pipeline uses:

- GitHub Secrets for sensitive credentials
- SSH key authentication
- HTTPS via Let's Encrypt
- Automatic SSL certificate renewal using Certbot

No secrets are stored inside the repository.

---

## 🌍 Deployment

The application is deployed on:

- AWS EC2
- Docker
- Nginx Reverse Proxy
- HTTPS (Let's Encrypt)

Deployment requires only:

```bash
git push
```

Everything else is fully automated by GitHub Actions.

---

## 📈 Features

- Fully automated deployment
- Dockerized application
- Continuous Integration
- Continuous Deployment
- Zero manual deployment steps
- Secure HTTPS
- Automatic SSL renewal
- Production-ready reverse proxy
- Cloud deployment on AWS

---

## 📖 What I Learned

This project helped me understand:

- CI/CD fundamentals
- GitHub Actions workflows
- Docker image lifecycle
- Docker Hub integration
- AWS EC2 deployment
- SSH automation
- Reverse proxy configuration
- HTTPS configuration
- SSL certificate management
- Automated application delivery

---

## 🎯 Future Improvements

- Blue/Green Deployments
- Health Checks
- Rollback Strategy
- Kubernetes Deployment
- Terraform Infrastructure Provisioning
- Monitoring with Prometheus & Grafana
- Container Orchestration
- Multi-stage Docker Builds

---

## 📸 Demo

Pipeline execution:

```
git push
        │
        ▼
GitHub Actions
        │
        ▼
Build Docker Image
        │
        ▼
Push Docker Hub
        │
        ▼
SSH into EC2
        │
        ▼
Pull Latest Image
        │
        ▼
Restart Container
        │
        ▼
Nginx Reverse Proxy
        │
        ▼
HTTPS Live Website
```

---

## 👨‍💻 Author

Built as part of my DevOps learning journey using GitHub Actions, Docker, AWS, Nginx, and Let's Encrypt.

## https://flask3rd.duckdns.org
