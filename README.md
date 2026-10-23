# Social Media MVP

A lightweight social media web application developed for the Software Engineering Workshop assessment.

The goal is to allow users to register, authenticate, publish text posts, and view a public feed ordered from newest to oldest.

> **Project status:** Initial documentation and planning completed. Application implementation is in progress.

## Features

The planned MVP includes:

- User registration and login.
- Secure password hashing.
- User logout and session management.
- Authenticated text-post creation.
- A public feed displaying the author, content, and creation date of each post.
- Newest-first feed ordering.
- Persistent data storage across ordinary Docker restarts when the database volume is retained.
- Automated tests and continuous integration.

## Technology Stack

- Python
- Flask
- HTML, CSS, and Bootstrap
- SQLite
- Werkzeug password hashing
- pytest
- Docker and Docker Compose
- GitHub Actions

## Project Documentation

- [Requirements](docs/requirements.md)
- [Development Methodology](docs/methodology.md)
- [Product Backlog](docs/backlog.md)
- [System Architecture](docs/architecture.md)
- [Technology Stack Decision](docs/adr/ADR-001-technology-stack.md)

## Agile Project Management

The project uses an Agile approach to organize work incrementally.

GitHub Issues records the user stories, while GitHub Projects tracks their status and planned iteration.

The current workflow is:

`Backlog → Todo → In Progress → Testing → Done`

Iteration labels group the planned work:

- `Sprint 1` — Foundation and Authentication
- `Sprint 2` — Posts and Feed
- `Sprint 3` — Persistence and Docker
- `Sprint 4` — Quality and Delivery

## Prerequisites

The following tools will be required to run the completed application:

- Git
- Python, using the version specified by the project configuration
- pip
- Docker Desktop with Docker Compose

## Setup and Execution

**The following instructions will be finalized after the application structure and dependencies are implemented.**

The intended workflow is:

1. Clone the repository.
2. Set up the Python environment and install dependencies.
3. Configure the required environment variables, if any.
4. Start the application locally or with Docker Compose.
5. Open the application using the local address documented by the application.

Exact commands will be added after the implementation is ready.

## Running Automated Tests

The application uses `pytest` to run automated tests for its core functionality.

### Prerequisites

- Python 3.12 or compatible.
- Project dependencies installed.

### Setup

Activate your virtual environment and install the dependencies:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Run all tests

From the project root, run:

```bash
pytest
```

### Run a specific test module

For example:

```bash
pytest tests/test_registration.py
pytest tests/test_login.py
pytest tests/test_posts.py
pytest tests/test_feed.py
pytest tests/test_persistence.py
```

The test suite covers user registration and login, post creation, rejection of unauthenticated post creation, public feed behavior, and data persistence.

## Continuous Integration

A GitHub Actions workflow will be configured to install dependencies, run tests, and build the Docker image on push.

## Data Persistence

The application will use SQLite. Docker Compose will configure persistent database storage so that ordinary application restarts do not delete accounts and posts when the database volume is retained.

## Scope

The MVP focuses on authentication, text posts, and a public feed.

Features such as likes, comments, following, direct messages, and notifications are outside the initial scope.

## Security Notes

- Passwords must be stored as secure hashes.
- User input must be validated and safely rendered.
- Secrets and local database files must not be committed to the repository.
- Production deployment and high-scale operation are outside the initial academic MVP scope.

## License

This project was created for educational purposes as part of the Software Engineering Workshop assessment. A formal license can be added if required.