# EN MOSTAFA AI AGENT v2.1

EN MOSTAFA AI AGENT v2.1 is a local-first AI control agent foundation. It is not limited to WordPress. WordPress is only one integration adapter inside a broader architecture that can manage local files, execute PowerShell/CMD tasks, connect to REST APIs, work with MCP tools, call multiple LLM providers, and support software-development workflows for Python, PHP, JavaScript, C#, ASP.NET, and Visual Studio projects.

The goal of this repository is to provide a clean, modular base that can grow into a full AI Agent runtime: dashboard, REST API, MCP server, task engine, memory, strategy, planning, autonomous loop, local automation, and external-service adapters.

## Core Identity

- Local AI Control Agent for Windows-first automation.
- REST API server for dashboard, integrations, and external apps.
- Future MCP tool server for ChatGPT, Claude, Codex, and other AI clients.
- Task Engine for multi-step jobs, retries, progress, and verification.
- LLM Bridge that can connect to OpenAI/ChatGPT, Anthropic/Claude, OpenRouter, Groq, Gemini, Ollama, DeepSeek, Qwen, and other compatible providers.
- Local automation layer for PowerShell, CMD, file operations, builds, tests, and project scaffolding.
- Integration adapters for WordPress, LMS, hosting providers, local projects, Visual Studio, and ASP.NET workflows.

## Current Repository Status

This `v2.1` repository is intentionally small. It is the clean foundation layer, not the entire production runtime yet.

Current implemented files:

| File | Current responsibility |
|---|---|
| `src/app.py` | Flask entry point. Starts the local server on `127.0.0.1:5001`, registers routes, and serves the dashboard. |
| `src/routes.py` | REST API routes for listing sites, running AI tasks, checking status, and chat. |
| `src/wp_manager.py` | First integration adapter. Currently stores WordPress site records in memory and exposes basic status helpers. |
| `src/llm_bridge.py` | LLM boundary. Currently a mock placeholder that can be replaced with real provider connectors. |
| `templates/dashboard.html` | Simple dashboard page shown at `/`. |
| `requirements.txt` | Python dependencies: Flask, requests, and python-dotenv. |
| `docs/architecture.md` | Extended architecture document. |
| `docs/roadmap.md` | Planned development roadmap. |

## Full Agent Architecture

```text
+-------------------------+
| User / Operator         |
| Browser / API / IDE     |
+-----------+-------------+
            |
            v
+-----------+-------------+
| Dashboard + REST API    |
| src/app.py              |
| src/routes.py           |
+-----------+-------------+
            |
            v
+-----------+-------------+
| Agent Gateway           |
| routes -> LLM/Task layer|
+-----+-----------+-------+
      |           |
      v           v
+-----+----+  +---+------------------+
| LLM      |  | Integration Adapters |
| Bridge   |  | WordPress/LMS/API    |
+-----+----+  +---+------------------+
      |           |
      v           v
+-----+----+  +---+------------------+
| MCP/Tool |  | Local Automation     |
| Calling  |  | PowerShell/CMD/files |
+-----+----+  +---+------------------+
      |           |
      v           v
+-----+------------------------------+
| Task Engine + Memory + Planning    |
| execution, retries, verification   |
+------------------------------------+
```

## Main Modules and File Names

The following table documents the intended production-grade module layout. Some files are already present in this repository, while the advanced runtime files are planned or available in the extended workspace version and can be ported into `v2.1` step by step.

| Layer | File name | Purpose |
|---|---|---|
| App entry | `src/app.py` | Flask application entry point and dashboard host. |
| REST routes | `src/routes.py` | HTTP API endpoints for agent, chat, status, and integrations. |
| WordPress adapter | `src/wp_manager.py` | WordPress site registry and API adapter. |
| LLM bridge | `src/llm_bridge.py` | Provider abstraction for model calls and chat. |
| Dashboard | `templates/dashboard.html` | Browser UI for controlling and monitoring the agent. |
| MCP server | `mcp_server.py` | FastMCP/SSE tool server for AI clients. |
| Tool definitions | `llm_tools.py` | Tool schemas and tool executor used by LLM tool calling. |
| Tool registry | `tool_registry.py` | Registers tools, tracks status, call counts, and errors. |
| Tool manifest | `tool_manifest.py` | Describes tool capabilities, workflows, and retry policies. |
| AI operator | `ai_operator.py` | Main high-level executor: analyze intent, build plan, execute steps, summarize. |
| Agent core | `agent_core.py` | Coordinates brain, executor, memory, strategy, rules, and monitoring. |
| Task engine | `task_engine.py` | Stores tasks/steps, runs multi-step workflows, tracks progress. |
| System executor | `system_executor.py` | Executes local shell commands through CMD/PowerShell with diagnostics. |
| Shell reliability | `shell_reliability.py` | Selects shell, diagnoses environment, retries command execution. |
| Memory | `memory_engine.py` | Stores previous executions, success/failure, duration, and errors. |
| Strategy | `strategy_engine.py` | Learns successful commands and fallback strategies. |
| Planning | `planning_graph.py` | Builds ordered execution graphs and dependencies. |
| Decisions | `decision_engine.py` | Chooses next task and recovery strategy. |
| State | `state_manager.py` | Stores current task, steps, and final result. |
| Dynamic rules | `dynamic_rules.py` | Learns simple command replacement rules from failures. |
| Autonomous loop | `autonomous_loop.py` | Continuous loop that pulls goals, runs tasks, evaluates results. |
| Goal manager | `goal_manager.py` | Manages backlog, goals, and task completion state. |
| Self monitor | `self_monitor.py` | Evaluates task outcomes and suggests improvements. |
| Self improvement | `self_improvement.py` | Generates improvement tasks when the queue is empty. |
| Knowledge | `knowledge_manager.py` | Stores/searches uploaded documents, snippets, URLs, and project knowledge. |
| Feedback | `feedback_loop.py` | Records execution feedback and agent performance signals. |
| Project reader | `project_reader.py` | Scans local projects and reads large files in chunks. |
| Browser automation | `browser_use_adapter.py` | Browser-use/Playwright bridge for visual and browser workflows. |
| Visual capture | `visual_capture_manager.py` | Validated screenshots and visual checks. |
| Hostinger adapter | `hostinger_client.py` | Hosting provider client. |
| Hostinger routes | `hostinger_routes.py` | REST API for hosting management. |
| LMS adapter | `masterstudy_manager.py` | LMS course/resource/quiz operations. |
| Assessment import | `assessment_builder.py` | Parses imported educational content and builds assessments. |
| Elementor adapter | `elementor_engine.py` | Page/layout helper for Elementor-backed sites. |

## REST API Architecture

The REST layer is used by the dashboard, local tools, ASP.NET apps, browser extensions, and external integrations.

Current endpoints:

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | `GET` | Open dashboard. |
| `/healthz` | `GET` | Service health check. |
| `/wp/sites` | `GET` | List registered sites. |
| `/wp/operator/run` | `POST` | Execute an AI task. |
| `/wp/status?site=name` | `GET` | Get site status. |
| `/wp/ai/chat` | `POST` | Chat endpoint through `LLMBridge`. |

Planned production endpoints:

| Endpoint | Purpose |
|---|---|
| `/run` | General task execution, not tied to WordPress. |
| `/system/status` | Runtime, tool, provider, and process status. |
| `/llm/status` | Active LLM provider/model/key status. |
| `/llm/configure` | Configure OpenAI, Claude, Ollama, OpenRouter, etc. |
| `/knowledge/upload` | Upload files or text into the knowledge base. |
| `/tasks/create` | Create a long-running task. |
| `/tasks/<id>` | Query task progress/result. |
| `/projects/scan` | Scan a local project folder. |
| `/shell/run` | Safe local command execution. |
| `/wp/*` | WordPress adapter endpoints. |
| `/hostinger/*` | Hosting adapter endpoints. |

## MCP + Tool-Use Architecture

MCP is the tool layer for AI clients. REST is for apps and dashboards. MCP is for models.

The MCP server should expose tools such as:

| Tool | Purpose |
|---|---|
| `agent_capabilities` | Return all available tool groups. |
| `tool_manifest` | Return detailed tool descriptions and workflows. |
| `project_scan` | Inspect a local project without loading every file. |
| `read_file_chunked` | Read large files safely in chunks. |
| `run_powershell` | Run Windows PowerShell commands. |
| `run_local_shell` | Run CMD commands. |
| `verify_artifact` | Verify files, URLs, text, or images after a tool claims success. |
| `list_sites` | List configured WordPress or integration sites. |
| `get_site_info` | Get site information from an adapter. |
| `search_knowledge` | Search uploaded knowledge. |
| `visual_capture` | Capture and validate screenshots. |

Typical MCP flow:

```text
User asks ChatGPT/Claude/Codex:
"Analyze this ASP.NET project and fix build errors."

LLM calls:
project_scan -> read_file_chunked -> run_powershell("dotnet build")

Agent returns:
stdout, stderr, exit code, file paths, and verified result.

LLM explains:
what failed, what changed, and how it was verified.
```

## Task Engine

The Task Engine is responsible for turning a natural-language request into a durable execution workflow.

Responsibilities:

- Create a `task_id`.
- Split work into ordered steps.
- Save each step and status in SQLite.
- Execute each step with retries.
- Pass context between steps.
- Resume incomplete tasks.
- Store stdout/stderr/results.
- Verify final outcome.
- Report progress to the dashboard.

Example:

```text
Task: "Create an ASP.NET Web API and add authentication"

Steps:
1. Scan target folder.
2. Run dotnet new webapi.
3. Add authentication packages.
4. Modify Program.cs.
5. Add controller/service files.
6. Run dotnet build.
7. Run dotnet test.
8. Verify generated files and build output.
```

## Memory / Strategy / Planning

### Memory

Memory stores previous executions:

- command or task text
- success/failure
- duration
- error message
- timestamp

This allows the agent to recognize similar tasks and avoid repeating known failures.

### Strategy

Strategy tracks which commands and workflows work best. It can store:

- success rate
- average duration
- fallback command
- known failure pattern

Example:

```text
If "pip install" fails repeatedly:
try "py -3.11 -m pip install ..."
```

### Planning

Planning converts user intent into executable steps:

- classify task domain
- choose tools
- build dependency graph
- order steps
- mark risky operations
- decide verification requirements

The key files for this layer are:

- `planning_graph.py`
- `decision_engine.py`
- `dynamic_rules.py`
- `state_manager.py`
- `ai_operator.py`

## Autonomous Loop

The Autonomous Loop is the long-running agent mode. Instead of waiting for one request at a time, it continuously pulls tasks from a goal queue.

```text
while running:
    task = goal_manager.get_next_task()

    if no task:
        self_improvement.generate_improvement_tasks()
        sleep()
        continue

    result = agent_core.handle_task(task)

    if result completed:
        goal_manager.mark_task_done(task)

    self_monitor.evaluate_task(result)
    self_monitor.suggest_improvements()
```

Main files:

- `autonomous_loop.py`
- `goal_manager.py`
- `agent_core.py`
- `self_monitor.py`
- `self_improvement.py`
- `feedback_loop.py`

## Dashboard

The current dashboard is intentionally simple. The production dashboard should become an AI Control Center.

Dashboard sections:

- System status
- LLM provider status
- REST/MCP health
- Task queue and progress
- Activity log
- Chat with tools
- Local projects
- PowerShell/CMD runner
- WordPress adapter
- LMS adapter
- Hosting adapter
- Knowledge uploads
- Settings and API keys

Important: the dashboard should not be presented as a WordPress-only interface. WordPress should be one page or one adapter inside a broader agent dashboard.

## Local Automation and PowerShell

The agent should support local Windows automation through:

- `PowerShell`
- `CMD`
- Python scripts
- `dotnet`
- `npm`
- `git`
- file operations
- test/build commands

Example local tasks:

- Create a new ASP.NET project.
- Open and analyze a Visual Studio solution.
- Modify C# services/controllers.
- Run `dotnet build`.
- Run `dotnet test`.
- Create a Python package.
- Fix a JavaScript project.
- Scan a local folder and summarize its architecture.

## Visual Studio and ASP.NET Integration

This architecture can integrate with Visual Studio and ASP.NET in three ways:

1. Through REST API calls from a .NET app.
2. Through MCP tools exposed to an AI client.
3. Through local PowerShell/CMD execution using `dotnet`, `msbuild`, and `nuget`.

Example C# integration:

```csharp
using System.Net.Http.Json;

var client = new HttpClient
{
    BaseAddress = new Uri("http://127.0.0.1:5001")
};

var payload = new
{
    task = "Analyze this ASP.NET project, run dotnet build, and report errors",
    site = (string?)null
};

var response = await client.PostAsJsonAsync("/wp/operator/run", payload);
var body = await response.Content.ReadAsStringAsync();
Console.WriteLine(body);
```

## LLM Provider Connectors

The LLM layer should be provider-agnostic. The rest of the system should not care whether the active model is OpenAI, Claude, Ollama, Gemini, or another provider.

Supported/target providers:

| Provider | Notes |
|---|---|
| OpenAI / ChatGPT | Native OpenAI API and tool calling. |
| Anthropic / Claude | Messages API and tool-use. |
| OpenRouter | Multi-model OpenAI-compatible gateway. |
| Groq | Fast OpenAI-compatible inference. |
| DeepSeek | OpenAI-compatible API. |
| Qwen | DashScope/OpenAI-compatible API. |
| Gemini | Google Generative Language API. |
| Ollama | Local model runtime. |
| Mock | Testing mode without external API keys. |

## WordPress and LMS Positioning

WordPress is supported, but it should not define the whole product.

WordPress/LMS features can include:

- site registration
- health checks
- plugin list/update workflows
- content creation
- REST plugin integration
- MasterStudy LMS courses
- lessons
- quizzes
- resources such as PDF, URLs, videos

These features should live inside adapters, while the core agent remains general-purpose.

## Security Principles

- Local-first by default.
- Keep API keys in `.env` or private config, never committed.
- Require explicit confirmation for destructive shell or remote operations.
- Verify every generated artifact.
- Prefer structured APIs over UI scraping.
- Keep adapters separated from the core task engine.
- Do not let a WordPress task accidentally affect a local project, and do not let a local shell task accidentally affect a production site.

## Roadmap

1. Replace mock `src/llm_bridge.py` with real provider connectors.
2. Add persistent site/config storage.
3. Add `TaskEngine` with SQLite-backed steps.
4. Add `SystemExecutor` for PowerShell/CMD.
5. Add MCP server and tool schemas.
6. Add Memory, Strategy, Planning, and Dynamic Rules.
7. Expand dashboard into a full control center.
8. Add local project and ASP.NET adapters.
9. Add WordPress/LMS/Hosting adapters as separate modules.
10. Add artifact verification and safe execution policies.

## Installation

```powershell
cd C:\mcp-agent\en-mostafa-ai-agent-v2.1
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src\app.py
```

Open:

```text
http://127.0.0.1:5001
```

## Current Usage

```http
GET  /healthz
GET  /wp/sites
GET  /wp/status?site=example
POST /wp/operator/run
POST /wp/ai/chat
```

Example:

```powershell
Invoke-RestMethod `
  -Method POST `
  -Uri http://127.0.0.1:5001/wp/operator/run `
  -ContentType "application/json" `
  -Body '{"task":"analyze local project structure","site":null}'
```

## Documentation

- `docs/architecture.md` - detailed architecture document.
- `docs/roadmap.md` - planned development roadmap.
