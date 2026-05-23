# Architecture

EN MOSTAFA AI AGENT v2.1 is built as a lightweight, modular WordPress AI control system.
The design focuses on clear separation of responsibilities and easy extension.

## Components

### `src/app.py`
The Flask application entry point.
- Starts the server on `127.0.0.1:5001`
- Registers API routes
- Serves the dashboard

### `src/routes.py`
Defines the REST APIs for the project.
- `/wp/sites` — list WordPress sites
- `/wp/operator/run` — execute AI tasks
- `/wp/status` — get site status
- `/wp/ai/chat` — conversational AI endpoint

### `src/wp_manager.py`
Simple WordPress manager abstraction.
- Holds site configuration
- Provides status checks
- Designed to be extended for real WordPress API calls

### `src/llm_bridge.py`
AI bridge layer.
- Executes tasks through a mock AI interface
- Returns structured JSON responses
- Can be extended to connect to real LLM providers

### `templates/dashboard.html`
A simple browser dashboard.
- Shows version and quick links
- Ready to be expanded into a proper admin-style UI

## How requests flow

1. User opens the dashboard in the browser.
2. Browser requests endpoints from Flask.
3. Flask routes the request to `src/routes.py`.
4. The route handler interacts with `WPManager` and/or `LLMBridge`.
5. Results are returned as JSON to the frontend.

## Extension points

- Add a real WordPress API client in `src/wp_manager.py`
- Replace the mock AI bridge with a real LLM provider in `src/llm_bridge.py`
- Improve the dashboard UI and add frontend routes
- Add persistent site storage and configuration
