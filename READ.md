# DevOps Intern Project 🚀

This project demonstrates a **complete DevOps pipeline** for a simple Flask app.

## Features
- Flask app (`app.py`)
- Dockerized app (`Dockerfile`)
- Kubernetes manifests (`deployment.yaml`, `service.yaml`)
- CI/CD pipeline (`Jenkinsfile`)
- Monitoring with Prometheus & Grafana
- Automation with Ansible

## How to Run
```bash
docker build -t devops-intern-app -f docker/Dockerfile .
docker run -d -p 5000:5000 devops-intern-app

