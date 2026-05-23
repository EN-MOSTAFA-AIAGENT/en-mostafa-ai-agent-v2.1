# EN MOSTAFA AI AGENT v2.1

EN MOSTAFA AI AGENT v2.1 is a clean local-first foundation for an AI control agent.
WordPress is supported as one integration adapter, but the architecture is broader: REST APIs, future MCP tools, local task execution through PowerShell/CMD, LLM connectors, and developer workflows for building or modifying projects in any programming stack, including Visual Studio and ASP.NET.

## Why `v2.1` exists

- Keep the old repository intact while building a fresh modern version.
- Provide a cleaner starting point for future development.
- Preserve the original `v1.x` behavior while introducing a more maintainable code structure.

## What this version includes

- `Flask` web server with REST endpoints.
- Lightweight integration adapter for external systems, starting with WordPress.
- AI bridge placeholder that can be connected to OpenAI, Anthropic, local models, or OpenAI-compatible providers.
- Simple dashboard template for visibility and operator actions.
- A documented architecture ready for MCP tools, Task Engine workflows, Memory, Planning, Strategy, and local automation.

## Architecture overview

This repo is intentionally small and modular. The complete professional architecture is documented in [`docs/architecture.md`](docs/architecture.md).

- `src/app.py` - application entry point and Flask server.
- `src/routes.py` - REST route definitions for agent and integration flows.
- `src/wp_manager.py` - first external-system adapter, currently focused on WordPress site registration/status.
- `src/llm_bridge.py` - model connector boundary for task execution and chat.
- `templates/dashboard.html` - simple dashboard UI.

### System diagram

```
+--------------------+       +-----------------------+
|   User / Browser   | <---> |   Flask Web Server    |
| Dashboard + REST   |       |   src/app.py          |
+--------------------+       +-----------------------+
                                      |
                                      +---> src/routes.py
                                      |       REST endpoints
                                      |
                                      +---> src/llm_bridge.py
                                      |       LLM connector boundary
                                      |
                                      +---> src/wp_manager.py
                                              first integration adapter

Planned extension surface:
MCP tools, Task Engine, Memory, Strategy, Planning, PowerShell/CMD,
Visual Studio/ASP.NET workflows, hosting providers, LMS systems, and other APIs.
```

## Project structure

- `src/` - application source code.
- `templates/` - HTML for the dashboard.
- `requirements.txt` - Python dependencies.
- `.gitignore` - local ignores.
- `docs/` - architecture and roadmap documentation.

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

- `docs/architecture.md` - full agent architecture, modules, REST/MCP/Task Engine, Memory, Strategy, Planning, Dashboard, Autonomous Loop, and extension points.
- `docs/roadmap.md` - planned features and task list for `v2.1`.

## Notes

This repository is intentionally kept as a minimal but extensible base. The legacy version remains available in the parent workspace for compatibility and reference.
