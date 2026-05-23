# Roadmap and Tasks for en-mostafa-ai-agent-v2.1

This file describes the planned features and tasks for version `v2.1`.

## Phase 1 — Foundation

- [x] Create a clean repository structure for the new version.
- [x] Add lightweight Flask server with basic routes.
- [x] Add WordPress manager abstraction.
- [x] Add AI bridge placeholder.
- [x] Add dashboard template and README documentation.

## Phase 2 — Core Features

- [ ] Implement real WordPress API connectivity in `src/wp_manager.py`.
- [ ] Add persistent site registration and storage.
- [ ] Connect `llm_bridge` to a real LLM provider.
- [ ] Add more dashboard pages for site health and plugin status.
- [ ] Add endpoint to manage MasterStudy courses.

## Phase 3 — Advanced AI and Hosting

- [ ] Add AI task planner and tool-use support.
- [ ] Add knowledge base integration.
- [ ] Add Hostinger API integration.
- [ ] Add safe self-heal and recovery features.

## Phase 4 — Documentation and Release

- [ ] Add architecture diagrams and design docs.
- [ ] Add contribution guide and issue templates.
- [ ] Add GitHub Actions CI for linting and tests.
- [ ] Publish release notes for `v2.1`.

## How to contribute

1. Fork the repository.
2. Create a feature branch.
3. Implement the task in `src/`.
4. Update documentation in `docs/`.
5. Open a pull request.
