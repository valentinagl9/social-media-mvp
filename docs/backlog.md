# Product Backlog

## 1. Purpose

The Product Backlog contains the features, technical tasks, and quality requirements needed to deliver the Social Media MVP. Items are prioritized according to their importance to the core functionality and the project assessment criteria.

The backlog will be managed using GitHub Issues and GitHub Projects. Items may be refined as development progresses.

## 2. Product Goal

Deliver a lightweight social media web application where users can register, log in, publish text posts, and view a public feed of posts ordered from newest to oldest.

The application must protect user credentials, persist data across ordinary Docker restarts when the database volume is retained, and include automated tests and a continuous integration workflow.

## 3. Priority Levels

- **P0 — Critical:** Required for the minimum viable product or essential security.
- **P1 — High:** Required for quality, deployment, or assessment completeness.
- **P2 — Medium:** Useful improvements that can be completed after the core requirements.

## 4. Epics and User Stories

### Epic E1 — User Authentication

**US-01 — Register an account**

As a visitor, I want to create an account so that I can use the application.

Priority: P0

Acceptance criteria:
- A visitor can submit a username and password.
- A valid submission creates a new account.
- Duplicate usernames are rejected with a clear error.
- Passwords are stored as secure hashes, not plaintext.
- Invalid input is handled safely.

**US-02 — Log in**

As a registered user, I want to log in so that I can access authenticated functionality.

Priority: P0

Acceptance criteria:
- A registered user can log in with valid credentials.
- Invalid credentials are rejected.
- A successful login establishes an authenticated session.
- The password is verified against its stored hash.

**US-03 — Log out**

As an authenticated user, I want to log out so that my session is ended.

Priority: P0

Acceptance criteria:
- A logged-in user can log out.
- The session is cleared or invalidated.
- Protected actions are no longer available after logout.

### Epic E2 — Posts and Public Feed

**US-04 — Create a post**

As an authenticated user, I want to publish a text post so that I can share content.

Priority: P0

Acceptance criteria:
- Authenticated users can submit a non-empty text post.
- Empty or invalid posts are rejected.
- The post is associated with its author and creation timestamp.
- Unauthenticated visitors cannot create posts.

**US-05 — View the public feed**

As a visitor, I want to view posts from all users so that I can discover published content.

Priority: P0

Acceptance criteria:
- The feed is publicly accessible.
- Each post displays its author's username, text, and creation date or time.
- Posts are ordered from newest to oldest.
- The feed handles the case where no posts exist.

### Epic E3 — Persistence and Deployment

**US-06 — Persist application data**

As a user, I want accounts and posts to remain available after an ordinary application restart so that my data is not lost.

Priority: P0

Acceptance criteria:
- User accounts and posts are stored in a persistent database.
- Docker Compose configures persistent database storage.
- Data remains available after the application is restarted when the database volume is retained.

**US-07 — Run the application with Docker**

As a developer, I want to run the application using Docker so that setup and execution are consistent.

Priority: P1

Acceptance criteria:
- A Dockerfile defines the application image.
- Docker Compose configures the application and its required services.
- The application can be started using documented commands.

### Epic E4 — Testing and Continuous Integration

**US-08 — Automate application tests**

As a developer, I want automated tests so that I can verify core functionality and detect regressions.

Priority: P1

Acceptance criteria:
- Tests cover registration and login.
- Tests cover post creation and public feed behavior.
- Tests verify that unauthenticated users cannot create posts.
- Tests can run using documented commands.

**US-09 — Run continuous integration**

As a developer, I want GitHub Actions to validate changes automatically so that errors are detected early.

Priority: P1

Acceptance criteria:
- A GitHub Actions workflow runs on push.
- The workflow installs project dependencies.
- The workflow runs automated tests.
- The workflow builds the Docker image.

### Epic E5 — Documentation and Project Management

**US-10 — Document setup and usage**

As a developer or evaluator, I want clear setup and usage instructions so that I can run and evaluate the application.

Priority: P1

Acceptance criteria:
- The README documents prerequisites and setup.
- The README explains how to run the application and tests.
- Docker commands and relevant configuration are documented.
- No real secrets or credentials are included.

**US-11 — Manage development with Agile practices**

As a project developer, I want to track work in GitHub Projects so that priorities, progress, and outstanding tasks remain visible.

Priority: P1

Acceptance criteria:
- Work items are recorded as GitHub Issues.
- Issues have appropriate labels and priorities.
- The project board shows the current status of each item.
- Work is reviewed and updated as development progresses.

## 5. Initial Implementation Order

1. Establish the project structure and application configuration.
2. Implement account registration and authentication.
3. Implement post creation and the public feed.
4. Add and run automated tests.
5. Configure Docker and persistent database storage.
6. Configure GitHub Actions.
7. Complete documentation and presentation preparation.

This order is an initial plan and may be adjusted as development progresses.

## 6. Scope Exclusions

The MVP does not include likes, comments, following, direct messages, notifications, or editing and deleting posts unless these features are explicitly required later.

## 7. Backlog Maintenance

The backlog will be reviewed regularly. Items may be clarified, reprioritized, divided into smaller tasks, or updated when implementation reveals new requirements. Completion will be assessed against the acceptance criteria of each item.