# Social Media MVP — Requirements Specification

**Project:** Social Media MVP (X / Twitter Lite)  
**Document status:** Draft  
**Version:** 0.1

## 1. Purpose and scope

The objective is to build a lightweight web-based social media application that allows users to register, log in, view posts published by all users and create their own posts.

The application must be easy to use, secure enough for the intended demonstration, and reproducible locally using Docker.

The project prioritizes the mandatory MVP functionality over optional social networking features.

## 2. Stakeholders

- **Client:** Startup requesting a demonstrable social media MVP.
- **Users:** People who register, authenticate and interact with the post feed.

## 3. Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | The system shall allow users to register using a unique username and password. | P0 |
| FR-02 | The system shall allow registered users to log in with valid credentials. | P0 |
| FR-03 | The system shall allow authenticated users to log out. | P1 |
| FR-04 | The system shall reject invalid login credentials. | P1 |
| FR-05 | The system shall allow authenticated users to create text posts. | P1 |
| FR-06 | The system shall display posts published by all users. | P1 |
| FR-07 | Each post shall display the author's username, post content and creation date. | P1 |
| FR-08 | The feed shall display the newest posts first. | P2 |
| FR-09 | The system shall persist user and post data across ordinary container restarts when persistent storage is retained. | P1 |
| FR-10 | The system shall prevent unauthenticated users from creating posts. | P0 |
| FR-11 | The system shall validate registration data and reject duplicate usernames. | P0 |
| FR-12 | The system shall validate post content and reject empty or invalid posts. | P1 |

## 4. Non-functional requirements

| ID | Requirement | Verification |
|---|---|---|
| NFR-01 | Passwords must never be stored as plain text. | Inspect password storage and test authentication. |
| NFR-02 | The application must be runnable locally using Docker Compose. | Build and start the application from a fresh checkout. |
| NFR-03 | The interface must be understandable and usable on desktop and mobile screen sizes. | Manually inspect the principal screens at different viewport sizes. |
| NFR-04 | Automated tests must cover registration, authentication, post creation and feed behavior. | Execute the test suite. |
| NFR-05 | GitHub Actions must install dependencies, run tests and validate the application build on pushes. | Inspect a successful workflow run. |
| NFR-06 | The database must retain data across ordinary container restarts when its persistent volume is retained. | Create a post, restart the application and verify the post remains. |
| NFR-07 | User input must be validated and post content must be rendered safely. | Test invalid inputs and HTML/script-like content. |
| NFR-08 | Setup instructions must document prerequisites, configuration, execution and testing. | Follow the README on a clean local checkout. |
| NFR-09 | Application configuration and secrets must not require committing real credentials to Git. | Inspect tracked files and configuration examples. |

## 5. Assumptions

1. The solution will be a web application.
2. Registration will initially use a username and password; email verification is not required.
3. The feed will be visible to all visitors, while creating posts requires authentication.
4. Posts will contain plain text, without image or video uploads.
5. Posts will display a consistent, human-readable creation date and time.
6. Posts will be ordered by creation time, newest first.
7. SQLite is the initial database candidate because the application is a small local MVP.
8. The application will use server-side sessions and a maintained password-hashing implementation.
9. Docker Compose will be the primary local execution workflow.
10. The initial scope excludes likes, comments, following, direct messages, notifications, editing and deleting posts.

## 6. Acceptance criteria

### AC-01 — Registration
Given a visitor who has not registered, when they submit valid registration details, then an account is created and duplicate usernames are rejected.

### AC-02 — Login
Given a registered user, when they submit correct credentials, then an authenticated session is established.

### AC-03 — Invalid credentials
Given invalid login credentials, when a login attempt is submitted, then authentication fails without exposing sensitive information.

### AC-04 — Logout
Given an authenticated user, when they log out, then their authenticated session is invalidated.

### AC-05 — Create a post
Given an authenticated user, when they submit valid post content, then the post is stored and associated with that user.

### AC-06 — View the feed
Given that posts exist, when a visitor opens the feed, then posts from all users are displayed with author, content and creation date.

### AC-07 — Newest first
Given multiple posts with different creation times, when the feed is displayed, then newer posts appear before older posts.

### AC-08 — Protected operations
Given an unauthenticated visitor, when they attempt to create a post directly through the application's protected endpoint, then the operation is rejected.

### AC-09 — Password security
Given a registered user, when the account is stored, then the database contains a password hash rather than the original password.

### AC-10 — Persistence
Given a registered user and an existing post, when the application container is restarted without deleting persistent storage, then the account and post remain available.

### AC-11 — Local reproducibility
Given a clean checkout and the documented prerequisites, when the documented Docker workflow is followed, then the application starts successfully.

## 7. Out of scope

- Following other users.
- Likes and comments.
- Private messaging.
- Image or video uploads.
- Email verification and password recovery.
- Administrative dashboards.

## 8. Traceability and validation

Each functional requirement will be mapped to one or more user stories and automated tests where practical. Acceptance criteria will be used to determine whether a feature is complete.

Requirements may be revised when technical constraints or implementation findings justify a change. Changes will be reflected in this document and, where applicable, in the GitHub backlog.
