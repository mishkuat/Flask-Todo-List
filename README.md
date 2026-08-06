# Flask Todo List — Portfolio Project

A small, containerized Todo List web application built with Flask to demonstrate DevOps and full-stack skills.

<!-- Badges: add CI / coverage / image registry badges here -->

## Completed work

This repository contains the work completed so far for the Flask Todo List project:

- Application and frontend/back-end code (entry: `main.py`).
- Dockerfile and `docker-compose.yml` for containerized runs.
- Unit tests under `tests/` and test runner configuration (`pytest`).
- CI workflow at `.github/workflows/ci.yml` that runs linting and tests, builds the Docker image, and (on the configured branch) can push images to a registry.

The sections below explain how to run and test the application locally and with Docker.

## Tech Stack

- Python 3.9+
- Flask
- Docker
- pytest
- GitHub Actions (CI)

## What You’ll Find Here

- Application entry: `main.py`
- Dockerfile and `docker-compose.yml` for containerized runs
- Tests: `tests/test_app.py`
- Static assets: `instance/` and `static/`

## Run Locally

1. Clone the repo:

    ```bash
    git clone <repo-url>
    cd Flask-Todo-List
    ```

2. Create and activate a virtual environment, then install requirements:

```bash
    python -m venv .venv
    source .venv/bin/activate   # macOS / Linux
    .venv\Scripts\activate     # Windows PowerShell
    pip install -r requirements.txt
    ```

3. Run the app:

    ```bash
    python main.py
    # or
    flask run
    ```

Visit <http://localhost:5000>

## Docker

Build and run locally with Docker:

```bash
docker build -t yourname/flask-todo:latest .
docker run -p 5000:5000 yourname/flask-todo:latest
```

Push to registry (if you choose to publish):

```bash
docker tag yourname/flask-todo:latest your-dockerhub-username/flask-todo:latest
docker push your-dockerhub-username/flask-todo:latest
```

## Tests

Run unit tests with pytest:

```bash
pytest -q
```

## CI / CD (Overview)

- CI workflow is defined in `.github/workflows/ci.yml`. It runs linting and tests, builds the Docker image, and is configured to push images when triggered on the designated branch. See the workflow file for specifics.

## Project Structure

- [main.py](main.py) — application entry
- [Dockerfile](Dockerfile)
- [docker-compose.yml](docker-compose.yml)
- [requirements.txt](requirements.txt)
- [tests/test_app.py](tests/test_app.py)

## Contributing

Feel free to open issues or PRs. Suggested first steps for contributors:

1. Fork the repo and create a feature branch.
2. Run tests and ensure new code has tests.
3. Open a PR with a clear description of changes.

## License

Add license information here (e.g., MIT) or remove this section if not applicable.

## Contact

Add your name and preferred contact (LinkedIn / email) so recruiters can reach you.
