# ADR-001: Technology Stack Selection

## Context

The Social Media MVP requires user registration, login and logout, authenticated post creation, a public feed, persistent data storage, automated tests, containerization, and continuous integration.

The project is an academic MVP with a limited scope and development timeframe. The technology stack should be easy to understand, maintain, test, and run locally.

## Decision

The project will use the following technologies:

- **Python and Flask** for the backend web application.
- **HTML, CSS, and Bootstrap** for the user interface.
- **SQLite** for persistent relational data storage.
- **Werkzeug password hashing** for secure password storage and verification.
- **pytest** for automated testing.
- **Docker and Docker Compose** for containerization and reproducible execution.
- **GitHub Actions** for continuous integration.
- **GitHub Issues and Projects** for Agile work tracking.

The application will initially follow a monolithic architecture.

## Alternatives Considered

### Alternative 1: Django

Django provides many built-in features, including an ORM and authentication functionality. However, Flask offers a smaller starting point and more flexibility for a small application whose components will be implemented and tested explicitly.

### Alternative 2: A separate frontend and backend

A separate frontend framework and API backend could provide a clearer separation for a larger system. However, this would introduce additional complexity that is not necessary for the current MVP.

### Alternative 3: PostgreSQL

PostgreSQL is a strong choice for larger applications and more advanced database requirements. SQLite is sufficient for the current academic scope and reduces local setup requirements. The database choice can be reconsidered if project needs change.

### Alternative 4: Manual deployment without Docker

Running the application directly on the host would be simpler initially, but Docker and Docker Compose provide a more reproducible environment and directly support the project's containerization requirements.

## Consequences

### Positive Consequences

- The initial setup remains relatively simple.
- The application can be developed as a single deployable unit.
- SQLite reduces database setup overhead.
- pytest supports repeatable automated testing.
- Docker improves execution consistency.
- GitHub Actions automates essential validation steps.

### Trade-offs and Limitations

- SQLite may be less suitable for high-concurrency workloads than a dedicated database server.
- Flask requires deliberate configuration of authentication, validation, and security controls.
- A monolithic application may become harder to maintain as the feature set grows.
- Docker and CI configuration require additional setup and maintenance.

## Security Considerations

- Passwords must never be stored in plaintext.
- User input must be validated and safely rendered.
- Protected actions must enforce authentication on the server.
- Secrets must not be committed to version control.
- Session and application configuration must use appropriate security settings.

## Review Conditions

The decision may be revisited if the application grows beyond the MVP scope, database requirements change, or implementation and testing reveal limitations in the selected stack.