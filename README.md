# EN MOSTAFA AI AGENT v2.1

This is a fresh, cleaner version of the EN MOSTAFA AI AGENT project.
It is designed to coexist with the original repository in the same workspace.

## Goals

- Keep the legacy version intact in the root workspace.
- Provide a modern `v2.1` implementation with a cleaner structure.
- Include a lightweight Flask-based foundation, WordPress API integration, AI operator, and dashboard.

## Structure

- `src/` — core application code
- `templates/` — dashboard and frontend templates
- `requirements.txt` — Python dependencies
- `.gitignore` — ignore logs, env files, bytecode

## Quick start

```bash
cd en-mostafa-ai-agent-v2.1
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python src/app.py
```

Then open `http://127.0.0.1:5001`.
