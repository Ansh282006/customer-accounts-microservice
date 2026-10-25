# Customer Accounts Microservice

![Build Status](https://github.com/Ansh282006/customer-accounts-microservice/actions/workflows/ci-build.yaml/badge.svg)

## Project Name
Customer Accounts Microservice

## Description
A RESTful microservice for managing customer accounts. It supports creating, reading, updating, deleting, and listing accounts. The project uses Flask and PostgreSQL, with automated tests, Continuous Integration via GitHub Actions, security headers (Talisman and CORS), Docker containerization, and deployment on Kubernetes.

## Features
- Create an account
- Read an account
- Update an account
- Delete an account
- List all accounts

## Tech Stack
- Python, Flask
- PostgreSQL, SQLAlchemy
- nosetests, Flake8, Pylint
- GitHub Actions (CI)
- Docker, Kubernetes, Tekton (CD)

## Getting Started
```bash
git clone https://github.com/Ansh282006/customer-accounts-microservice.git
cd customer-accounts-microservice
pip install -r requirements.txt
nosetests
flask run
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /accounts | Create an account |
| GET | /accounts | List all accounts |
| GET | /accounts/{id} | Read an account |
| PUT | /accounts/{id} | Update an account |
| DELETE | /accounts/{id} | Delete an account |
