# Agile Development Methodology

**Project:** Social Media MVP 
**Methodology:** Agile  
**Framework:** Scrum, adapted for individual development  
**Project management tool:** GitHub Projects  

## 1. Methodology selection

The project will follow the Agile methodology, using Scrum as its main framework.

Agile emphasizes iterative development, frequent feedback, working software, collaboration and responding to change. These principles are appropriate for this project because the requirements may need clarification, the delivery window is limited, and the mandatory MVP features must be prioritized over optional enhancements.

Scrum provides a structured way to organize the work into time-boxed iterations, define sprint goals, review completed increments and adjust the backlog as the project progresses.

Since the project is completed individually, Scrum responsibilities will be take step by step by the same user. The process will remain lightweight while retaining sprint planning, backlog refinement, progress reviews and a retrospective at the end of each iteration.

## 2. Why Agile and Scrum are appropriate

### Incremental delivery

The application will be developed in small increments. Authentication, social posts, feed functionality and deployment will be implemented and verified progressively.

### Changing or uncertain requirements

Requirements and assumptions will be documented before implementation. If testing or technical investigation reveals a necessary change, the backlog and relevant documentation will be updated.

### Short delivery window

The backlog will prioritize the mandatory assessment requirements.

### Continuous quality assurance

Tests will be written alongside implementation. GitHub Actions will automatically run the configured checks on pushes, providing feedback throughout development.

## 3. Scrum practices adapted to individual development

### Product backlog

The product backlog will contain prioritized user stories, documentation tasks, technical tasks and defects. Each item will have a clear purpose and acceptance criteria.

### Sprint planning

At the beginning of each sprint, work will be selected according to priority, dependencies and the sprint goal.

### Daily progress tracking

A daily Scrum meeting is not required for a single-person project. Progress will instead be tracked by updating GitHub Issues and the project board whenever work starts, changes status or is completed.

### Sprint review

At the end of each sprint, the completed increment will be checked against its acceptance criteria. Demonstrable functionality and test results will be recorded where relevant.

### Sprint retrospective

After each sprint, the development process will be reviewed to identify what worked, what caused difficulties and what should change in the next sprint.

These adaptations preserve the useful planning and feedback practices of Scrum without pretending that a full Scrum team exists.

## 4. GitHub project management

GitHub will be used as the central platform for planning, implementation and traceability.

- **GitHub Issues:** user stories, technical tasks, defects and documentation tasks.
- **GitHub Projects:** backlog prioritization and sprint progress.
- **Labels:** work type, application area and priority.
- **Git branches:** isolated development work.
- **Commits:** small, meaningful and traceable changes.
- **Pull Requests:** review and integration of changes when appropriate.
- **GitHub Actions:** automated testing and build validation.

The project board will use the following workflow:

1. Backlog
2. To Do
3. In Progress
4. Review / Testing
5. Done

An item will only be marked Done after its acceptance criteria and applicable verification checks have been satisfied.

## 5. Sprint plan

The following four-sprint plan is provisional and will be adjusted according to progress and technical dependencies.

### Sprint 1 — Requirements and foundation

**Goal:** Establish a clear, manageable project scope and development plan.

- Complete the requirements specification.
- Document assumptions and acceptance criteria.
- Finalize the Agile methodology.
- Create the prioritized product backlog.
- Configure GitHub Issues, labels and Projects.
- Design the architecture and record key technical decisions.
- Prepare the repository and development conventions.

**Expected increment:** An agreed project baseline with traceable requirements, a usable backlog and documented architectural decisions.

### Sprint 2 — Authentication

**Goal:** Implement secure user identity and session management.

- Implement registration.
- Implement login and logout.
- Hash passwords using a maintained password-hashing implementation.
- Protect authenticated operations.
- Add authentication and validation tests.

**Expected increment:** Users can register, authenticate and log out, with relevant tests passing.

### Sprint 3 — Social posts and feed

**Goal:** Deliver the main social media user journey.

- Implement post creation.
- Implement the feed for posts from all users.
- Display author, text and creation date.
- Sort posts newest first.
- Validate input and protect post creation.
- Verify data persistence and add relevant tests.

**Expected increment:** An authenticated user can publish a post and see it in the feed, while visitors can view existing posts.

### Sprint 4 — Quality and delivery

**Goal:** Make the MVP reproducible and ready for assessment.

- Finalize Docker and Docker Compose.
- Configure persistent storage.
- Configure GitHub Actions.
- Run automated and manual acceptance tests.
- Complete the README and troubleshooting instructions.
- Verify the application from a clean checkout.
- Prepare and rehearse the ten-minute presentation.

**Expected increment:** A tested, containerized MVP with documented setup instructions and a successful CI workflow.

## 6. Prioritization

Work will be prioritized according to its contribution to the assessment requirements.

- **P0 — Blocker:** prevents essential development, execution or assessment.
- **P1 — High:** required for the mandatory MVP or submission.
- **P2 — Normal/Low:** useful improvements that do not block the mandatory deliverables.

Registration, authentication, post creation, the feed, persistence, Docker, testing and CI take precedence over optional functionality.

## 7. Definition of Ready

A backlog item is ready when:

- Its purpose is clear.
- Its acceptance criteria are documented.
- Its priority is assigned.
- Dependencies are understood.
- The expected result can be verified.

## 8. Definition of Done

A backlog item is complete when:

- Its acceptance criteria are satisfied.
- Relevant tests or document checks pass.
- The changes have been reviewed.
- No secrets or unintended generated files are included.
- The changes are committed and pushed.
- The corresponding issue and project status are updated.

Code changes must also pass the applicable CI checks before final integration when the workflow is available.

## 9. Progress monitoring and continuous improvement

Progress will be monitored through GitHub Projects, open Issues, commits and CI results.

At the end of each sprint, the planned goal will be compared with the delivered increment. Incomplete items will be reprioritized or returned to the backlog.

The retrospective will identify process improvements for the next sprint. Technical risks, including authentication defects, data loss and environment inconsistencies, will be addressed through focused testing and repeatable Docker validation.

## 10. Conclusion

Agile, implemented through a lightweight Scrum framework, provides a suitable balance between planning, adaptability and demonstrable progress for this individual academic project.

The combination of prioritized user stories, short iterations, acceptance criteria, GitHub Projects and automated testing makes the development process transparent and supports trace