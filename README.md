# EN MOSTAFA AI AGENT v2.1

A new, cleaner edition of the EN MOSTAFA AI AGENT system, designed to run side-by-side with the legacy version.
This repo is a modern foundation for a WordPress AI control center with a lightweight Flask backend, structured code layout, and cleaner documentation.

## Why `v2.1` exists

- Keep the old repository intact while building a fresh modern version.
- Provide a cleaner starting point for future development.
- Preserve the original `v1.x` behavior while introducing a more maintainable code structure.

## What this version includes

- `Flask` web server with REST endpoints.
- Lightweight WordPress site manager abstraction.
- AI interaction bridge for task execution and chat.
- Simple dashboard template for quick visibility.
- A documented structure ready for extension.

## Architecture overview

This repo is intentionally small and modular:

- `src/app.py` — application entry point and Flask server.
- `src/routes.py` — REST route definitions for WordPress and AI flows.
- `src/wp_manager.py` — WordPress site connection and status helper.
- `src/llm_bridge.py` — AI task execution and chat interface.
- `templates/dashboard.html` — simple dashboard UI.

### System diagram

```
+--------------------+       +-----------------------+
|   User / Browser   | <---> |   Flask Web Server    |
|  (Dashboard + API) |       |   src/app.py          |
+--------------------+       +-----------------------+
            |                         |
            |                         +---> src/routes.py
            |                         |       (API endpoints)
            |                         |
            |                         +---> src/wp_manager.py
            |                         |       (WordPress helpers)
            |                         |
            |                         +---> src/llm_bridge.py
            |                                 (AI task bridge)
            |
            v
+--------------------+
| WordPress Sites    |
| + Hostinger, LMS   |
+--------------------+
```

## Project structure

- `src/` — application source code
- `templates/` — HTML for the dashboard
- `requirements.txt` — Python dependencies
- `.gitignore` — local ignores
- `docs/` — architecture and roadmap documentation

## Installation

```powershell
cd c:\mcp-agent\en-mostafa-ai-agent-v2.1
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src\app.py
```

Open the dashboard at:

```text
http://127.0.0.1:5001
```

## Usage

- `GET /healthz` — check service status
- `GET /wp/sites` — list configured WordPress sites
- `POST /wp/operator/run` — execute an AI task on a site
- `POST /wp/ai/chat` — send a chat message to the AI bridge

## Next development tasks

See `docs/roadmap.md` for the full feature list and roadmap.

## Documentation

- `docs/architecture.md` — system architecture and component roles.
- `docs/roadmap.md` — planned features and task list for `v2.1`.

## Notes

This repository is intentionally kept as a minimal but extensible base. The legacy version remains available in the parent workspace for compatibility and reference.
