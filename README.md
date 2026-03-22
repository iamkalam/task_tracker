# Task Tracker with Docker and GitHub Actions CI/CD

This project is a simple Python task tracker app for demoing:
- App development in Python (Flask)
- Docker containerization
- CI/CD with GitHub Actions
- Docker Hub image push using GitHub Secrets

## Project Structure

```text
task-tracker/
├── .github/workflows/ci-cd.yml
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   └── index.html
└── .dockerignore
```

## 1. Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`

## 2. Run with Docker

Build image:

```bash
docker build -t task-tracker:local .
```

Run container:

```bash
docker run -p 5000:5000 task-tracker:local
```

Open `http://localhost:5000`

## 3. GitHub Actions CI/CD Pipeline

Workflow file: `.github/workflows/ci-cd.yml`

Jobs:
1. `ci`: installs dependencies and runs a syntax check.
2. `docker-build-push`: builds and pushes Docker image to Docker Hub.

## 4. Required GitHub Secrets

Go to GitHub repository settings:
`Settings -> Secrets and variables -> Actions -> New repository secret`

Add these secrets:
- `DOCKERHUB_USERNAME` : your Docker Hub username
- `DOCKERHUB_TOKEN` : Docker Hub access token (not your password)

The workflow logs into Docker Hub using:

```yaml
- name: Login to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_TOKEN }}
```

## 5. Presentation Script (Quick)

1. Show `app.py` and run locally.
2. Show `Dockerfile` and run inside container.
3. Show `.github/workflows/ci-cd.yml`.
4. Explain secrets usage and why credentials are never hardcoded.
5. Push to `main` and show pipeline jobs running in GitHub Actions.
