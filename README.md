# Social Media MVP

A lightweight social media web application developed for the Software Engineering Workshop assessment.

Users can register, log in, publish text posts, and browse a public feed ordered from newest to oldest.

## Features

- User registration, login, and logout.
- Secure password hashing.
- Session-based authentication.
- Authenticated text-post creation.
- Public feed displaying post authors, content, and creation dates.
- Newest-first feed ordering.
- SQLite data persistence.
- Automated tests with pytest.
- Continuous integration with GitHub Actions.
- Docker and Docker Compose support.

## Technology Stack

- Python 3.12
- Flask
- SQLite
- Werkzeug password hashing
- HTML, CSS, and Bootstrap
- pytest
- Docker and Docker Compose
- GitHub Actions

## Prerequisites

For local development:

- Git
- Python 3.12 or compatible
- pip

For containerized execution:

- Docker Desktop with Docker Compose

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/valentinagl9/social-media-mvp.git
cd social-media-mvp
```

### 2. Create and activate a virtual environment

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

The application reads `SECRET_KEY` from the environment. If it is not set, the development configuration uses a placeholder key that must not be used in production.

For local development, you can set a temporary key in your terminal:

```bash
export SECRET_KEY="replace-with-a-local-development-secret"
```

Do not commit real secrets, passwords, or credentials to Git.

The SQLite database is stored at `instance/social_media.sqlite`. The application creates the instance directory when it initializes.

## Run the Application Locally

From the project root, with the virtual environment activated:

```bash
flask --app app:create_app run --debug
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

Stop the local development server with `Ctrl+C`.

## Running Automated Tests

Run the full test suite from the project root:

```bash
pytest
```

Run an individual test module:

```bash
pytest tests/test_registration.py
pytest tests/test_login.py
pytest tests/test_logout.py
pytest tests/test_posts.py
pytest tests/test_feed.py
pytest tests/test_persistence.py
```

The tests cover registration, login, logout, post creation, rejection of unauthenticated post creation, public feed behavior, and data persistence.

## Run with Docker

Make sure Docker Desktop is running.

Build the image and start the application:

```bash
docker compose up --build -d
```

The Compose configuration maps host port `5001` to container port `5000`. Open [http://localhost:5001](http://localhost:5001).

View the container status:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs web
```

Stop the application:

```bash
docker compose down
```

### Docker data persistence

Docker Compose uses a named volume, `social_media_data`, mounted at `/app/instance` inside the container. The SQLite database is stored in this directory so that accounts and posts survive ordinary container recreation while the volume is retained.

Do not run `docker compose down -v` unless you intend to delete the Compose volume and its stored data.

### Docker configuration

The Compose service reads `SECRET_KEY` from the environment. If it is not supplied, the Compose configuration uses a development-only placeholder.

For local use, you can export a value before starting Compose:

```bash
export SECRET_KEY="replace-with-a-local-development-secret"
docker compose up --build -d
```

Use a strong, securely managed secret in production. Never commit real secret values to the repository.

## Continuous Integration

GitHub Actions runs the CI workflow on pushes and pull requests. The workflow:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs dependencies from `requirements.txt`.
4. Runs the automated test suite with `pytest`.
5. Builds the Docker image.

Check the **Actions** tab in the GitHub repository to view workflow results.

## Project Documentation

- [Requirements](docs/requirements.md)
- [Development Methodology](docs/methodology.md)
- [Product Backlog](docs/backlog.md)
- [System Architecture](docs/architecture.md)
- [Technology Stack Decision](docs/adr/ADR-001-technology-stack.md)

## Agile Project Management

The project uses an Agile approach to organize work incrementally.

GitHub Issues records the user stories, while GitHub Projects tracks their status and planned iteration.

The workflow is:

`Backlog → Todo → In Progress → Testing → Done`

Planned iterations:

- `Sprint 1` — Foundation and Authentication
- `Sprint 2` — Posts and Feed
- `Sprint 3` — Persistence and Docker
- `Sprint 4` — Quality and Delivery

## Scope

The MVP focuses on authentication, text posts, and a public feed. Likes, comments, following, direct messages, and notifications are outside the initial scope.

## Security Notes

- Passwords are stored as secure hashes.
- The application should validate user input and safely render content.
- Local databases, environment files, and real secrets must not be committed.
- The development secret fallback is not suitable for production.
- Production hardening and high-scale deployment are outside the initial academic MVP scope.

## License

This project was created for educational purposes as part of the Software Engineering Workshop assessment. A formal license can be added if required.
