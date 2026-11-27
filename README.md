# 🤖 Transcript Summarizer Agent 📋

https://github.com/user-attachments/assets/7740ed26-431e-4b37-983b-6b08f543aab8

> 🎥 Watch **Transcript Summarizer Agent** in action! 📝

> [!CAUTION]
> The Vertex AI Agent Engine deployment is temporary and no longer active once the lab expires. The agent was deployed and tested successfully on Vertex AI Agent Engine (`us-central1`).

---

## Table of Contents

- [Introduction](#introduction)
- [Architecture Diagram](#architecture-diagram)
- [Project Structure](#project-structure)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Application Workflow](#application-workflow)
- [Screenshots](#screenshots)
- [Generative AI Capabilities & Integration](#generative-ai-capabilities--integration)
- [AI-Assisted Development](#ai-assisted-development)
- [Google Skills Challenge Lab Reference](#google-skills-challenge-lab-reference)
- [Future Enhancements](#future-enhancements)
- [Resources](#resources)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Introduction

**Transcript Summarizer Agent** is a stateful AI agent application developed as part of hands-on Google Cloud and generative AI learning experiences. It pairs a transcript summarization agent (`transcript_summarization_agent`) with deployment and querying utilities (`agent_engine_utils.py` and `query_agent_engine.py`), powered by **Google Agent Development Kit (ADK)**, **Gemini models**, and **Vertex AI Agent Engine** with **Google Cloud Logging** observability.

The project explores how to build and deploy interactive AI agents capable of summarizing multi-speaker conversations, extracting key issues, root causes, resolutions, and action items, maintaining multi-turn session history across sessions, and inspecting execution traces and runtime logs.

The repository organizes the agent package, Vertex AI Agent Engine deployment/query scripts, dependency specifications, and documentation into a clean, reproducible workspace (`adk_to_agent_engine`) ready for local testing and managed Agent Engine execution.

The project demonstrates practical concepts in ADK agent design, prompt/instruction engineering, managed session persistence, Cloud Logging integration, Python dependency management with `pip`, and serverless deployment on Vertex AI Agent Engine.

This repository documents my implementation and learning with Google Cloud Generative AI, ADK, Vertex AI Agent Engine, and Cloud Logging workflows, including project structure, supporting modules, and learning resources.

---

## Architecture Diagram

The following diagram illustrates the architecture of **Transcript Summarizer Agent**, connecting the user and ADK agent workflow with Vertex AI Agent Engine, session persistence, and Cloud Logging:

```mermaid
flowchart TD
    U["User / Client Prompt"] -->|" Transcript / Follow-up "| P["Agent Engine Playground / Client<br/>query_agent_engine.py"]

    subgraph AE ["Vertex AI Agent Engine (us-central1)"]
        P --> A["Transcript Summarizer Agent (ADK)<br/>transcript_summarization_agent"]
        A <--> G["Model<br/>Gemini (e.g., gemini-3.8-flash)"]
        A <--> S["Session Service & State<br/>(Session IDs & Events)"]
    end

    P -->|" CloudLoggingHandler "| L["Google Cloud Logging<br/>(Logs Explorer)"]
    A -->|" Spans & Traces "| T["Traces & Telemetry"]
    A -->|" Summary / Answer "| P
    P -->|" Final response "| U

    classDef user fill:#e8f0fe,stroke:#4285f4,color:#202124
    classDef app fill:#e6f4ea,stroke:#34a853,color:#202124
    classDef gcp fill:#fef7e0,stroke:#f9ab00,color:#202124
    classDef tool fill:#fce8e6,stroke:#ea4335,color:#202124
    classDef agent fill:#fef9e7,stroke:#f9ab00,color:#202124

    class U user
    class P app
    class AE,L gcp
    class A agent
    class G,S,T tool
```

> [!NOTE]
> This diagram provides a high-level overview of the ADK agent execution loop, managed session state, Cloud Logging integration, and Vertex AI Agent Engine hosting architecture.

### Architecture Overview

1. **User / Client Prompt**
   - Sends raw conversation transcripts (such as customer support calls, team standups, or incident reviews) and follow-up questions to the agent.

2. **Transcript Summarizer Agent**
   - Orchestrates transcript comprehension, structured summary generation, sentiment/action-item extraction, and multi-turn conversational responses using `agent.py` and Gemini models.

3. **Vertex AI Agent Engine & Session State (`us-central1`)**
   - Hosts the deployed agent (`Transcript Summarizer`), manages session IDs and event histories (`Sessions` and `Playground`), and exposes execution spans (`call_llm`, `generate_content`) and traces.

4. **Google Cloud Logging & Staging**
   - Initializes Vertex AI with the project ID, `us-central1` location, and GCS staging bucket (`gs://<project_id>-bucket`), while streaming application and runtime logs (`CloudLoggingHandler`) to Cloud Logging.

---

## Project Structure

The repository organizes the `adk_to_agent_engine` workspace, ADK agent package, Vertex AI Agent Engine utilities, and repository governance files into a clear layout.

```text
transcript-summarizer-agent/                       # Repository root directory
├── adk_to_agent_engine/                           # Workspace folder for ADK & Agent Engine files
│   ├── transcript_summarization_agent/            # Core Transcript Summarizer ADK Agent package
│   │   ├── __init__.py                            # Package initialization module
│   │   ├── agent.py                               # Agent definition, instructions, and model setup
│   │   ├── query_agent_engine.py                  # Vertex AI / Cloud Logging init and agent query logic
│   │   └── requirements.txt                       # Dependencies for the agent package
│   │
│   ├── agent_engine_utils.py                      # Helper utilities for Vertex AI Agent Engine
│   └── requirements.txt                           # Workspace-level Python dependencies
│
├── .gitignore                                     # Excludes secrets, caches, virtual envs, and OS files
├── CODE_OF_CONDUCT.md                             # Community conduct guidelines
├── CONTRIBUTING.md                                # Contribution workflows and guidelines
├── LICENSE                                        # Open-source license terms (Apache-2.0)
├── README.md                                      # Project documentation
└── SECURITY.md                                    # Security vulnerability reporting policy
```

> [!NOTE]
> This tree reflects the repository structure on main. Refer to `adk_to_agent_engine/transcript_summarization_agent/` and `adk_to_agent_engine/agent_engine_utils.py` for component implementations.

### Key Components

- `adk_to_agent_engine/transcript_summarization_agent/` — Contains the ADK agent (`agent.py`), Vertex AI and Cloud Logging initialization plus querying code (`query_agent_engine.py`), package initializer (`__init__.py`), and `requirements.txt`.
- `adk_to_agent_engine/agent_engine_utils.py` — Provides supporting helper utilities for working with Vertex AI Agent Engine.
- `adk_to_agent_engine/requirements.txt` — Lists workspace-level Python dependencies alongside the agent package's `requirements.txt`.
- `.gitignore` — Keeps `.env` files, credentials, virtual environments (`.venv/`), and Python caches (`__pycache__/`) out of version control.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` — Define contribution workflows, community standards, and security-reporting guidelines.

---

## Features

- **Structured Transcript Summarization:** Condenses support, standup, and incident transcripts into clear summaries covering issues, root causes, resolutions, and action items.
- **Multi-Turn Session Memory & Session IDs:** Persists conversation events across turns and allows resuming or inspecting prior sessions by Session ID in the Playground.
- **Follow-Up & Structured Extraction:** Supports follow-up questions on sentiment, compensation, or speaker details, as well as reformatting action items into tables or bullet lists.
- **Built-In Traces & Cloud Logging:** Surfaces execution spans (`call_llm`, model generation) in the Playground alongside `ReasoningEngine` and custom `CloudLoggingHandler` logs in Logs Explorer.
- **Clean Secret & Cache Hygiene:** Configured with `.gitignore` to prevent accidental commits of `.env` files, credentials, or build/cache artifacts.
- **Modular Agent & Utility Separation:** Keeps `transcript_summarization_agent` and `agent_engine_utils.py` cleanly organized for maintainability.

> [!NOTE]
> Actual runtime behavior depends on valid Google Cloud credentials, enabled APIs, allowed models, staging bucket permissions, and proper environment configuration.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language for ADK agent code and Agent Engine scripts |
| **Google Agent Development Kit (ADK)** | Agent definition and orchestration framework |
| **Vertex AI Agent Engine** | Managed runtime for deploying agents, sessions, and traces (`us-central1`) |
| **Gemini Models & Vertex AI** | Core LLM reasoning, transcript summarization, and conversational responses |
| **Google Cloud Logging** | Centralized log collection and LQL querying in Logs Explorer |
| **Google Cloud Storage (GCS)** | Staging bucket (`gs://<project_id>-bucket`) for Vertex AI initialization and artifacts |
| **`pip`** | Python package and environment dependency management |
| **Git & GitHub** | Version control and source code hosting |

> [!NOTE]
> The table describes the technologies and patterns reflected in the project implementation.

---

## Application Workflow

**Transcript Summarizer Agent** is structured around environment initialization, agent deployment to Vertex AI Agent Engine, interactive/programmatic querying, and observability inspection.

### 1️⃣ Environment & Dependency Setup

- Configure required environment variables (`GOOGLE_CLOUD_PROJECT`, `APP_NAME`, and any model/environment settings) in a local `.env` file while keeping `.env` out of version control.
- Install dependencies using
  `pip install -r adk_to_agent_engine/requirements.txt` and `pip install -r adk_to_agent_engine/transcript_summarization_agent/requirements.txt`.

### 2️⃣ Vertex AI & Cloud Logging Initialization

- Load environment variables via `load_dotenv()` and initialize `google.cloud.logging.Client` with `CloudLoggingHandler` (`name="transcript-summarizer"`).
- Initialize `vertexai.init(project=project_id, location="us-central1"`, `staging_bucket=f"gs://{project_id}-bucket")`.

### 3️⃣ Agent Deployment & Playground Testing

- Deploy `transcript_summarization_agent` (`Transcript Summarizer`) to Vertex AI Agent Engine and open the Playground tab.
- Send a transcript prompt to generate a structured summary, then send follow-up prompts (such as extracting action items into a table or checking sentiment) within the same session.

### 4️⃣ Session Persistence & Trace Inspection

- Switch between sessions or reopen a conversation by Session ID to verify multi-turn state retention.
- Inspect Events, Traces, associated spans (`call_llm`, model calls), and the Sessions tab for execution details.

### 5️⃣ Cloud Logging Verification

- Open Logs Explorer and filter by `resource.type="aiplatform.googleapis.com/ReasoningEngine"` or `logName="projects/<PROJECT_ID>/logs/transcript-summarizer"` to inspect runtime and model logs.

---

## Screenshots

This section showcases **Transcript Summarizer Agent** in action, including Cloud Shell / workspace setup, Vertex AI Agent Engine Playground sessions, traces, and Cloud Logging.

### Transcript Summarizer Agent UI

<img width="1076" height="600" alt="Transcript Summarizer Agent" src="https://github.com/user-attachments/assets/c17d97e2-9343-4107-b2e6-e7cea6e38d84" />

### Google Cloud Console Dashboard

<img width="1366" height="768" alt="Google Cloud Console Dashboard" src="https://github.com/user-attachments/assets/abf31155-5a98-47a0-8cb9-19ab23936405" />

### Project Source Code

<img width="1366" height="767" alt="Project Source Code - 1" src="https://github.com/user-attachments/assets/c93fc956-0889-4d3c-b236-a98461437b34" />
<img width="1366" height="768" alt="Project Source Code - 2" src="https://github.com/user-attachments/assets/fa5975b0-ed4e-49ac-9234-016f66f309a7" />

### Cloud Shell Terminal

<img width="1366" height="768" alt="Cloud Shell Terminal" src="https://github.com/user-attachments/assets/9b142765-9528-4c7f-892f-53debc0bc65d" />

### Agent Deployments, Revisions & Sessions

<img width="1366" height="768" alt="Agent Runtime Deployments - 1" src="https://github.com/user-attachments/assets/51dd0446-d1e1-4f41-853f-46cc151557c0" />
<img width="1366" height="768" alt="Agent Runtime Deployments - 2" src="https://github.com/user-attachments/assets/0e1ae94b-abf9-443a-b242-ead8a2aaf906" />
<img width="1366" height="768" alt="Revisions" src="https://github.com/user-attachments/assets/2fee120f-5b1c-4ff4-bc62-903f3c1582f6" />
<img width="1366" height="768" alt="Persisted Sessions List" src="https://github.com/user-attachments/assets/24970201-e5da-4c4c-ae5c-76bbc06e6979" />

### Agent Engine Playground

<img width="1366" height="768" alt="Query - 1" src="https://github.com/user-attachments/assets/75fa1ea2-0d0e-4041-828e-e0b3bd56ad7c" />
<img width="1366" height="768" alt="Query - 2" src="https://github.com/user-attachments/assets/cf408cec-72a9-48a3-99b1-c10b1004a89e" />
<img width="1366" height="768" alt="Query - 3" src="https://github.com/user-attachments/assets/daad2cb5-810e-4155-9ee5-d02e175e42e7" />
<img width="1366" height="768" alt="Query - 4" src="https://github.com/user-attachments/assets/49762c1d-1411-4102-97e4-40d94da8e0aa" />
<img width="1366" height="768" alt="Query - 5" src="https://github.com/user-attachments/assets/9dba454d-9f9a-470f-90a2-b886031171ee" />
<img width="1366" height="768" alt="Query - 6" src="https://github.com/user-attachments/assets/aae8d6dd-3111-452f-9a71-6970374c98f3" />

### Agent Engine Playground — Execution Traces

<img width="1366" height="768" alt="Traces - 1" src="https://github.com/user-attachments/assets/cf9075ba-3822-40b1-a564-92294e9abd0d" />
<img width="1366" height="768" alt="Traces - 2" src="https://github.com/user-attachments/assets/e4399f95-142d-4ae6-8c5c-0dfd7a5fede5" />
<img width="1366" height="768" alt="Traces - 3" src="https://github.com/user-attachments/assets/a51f4e04-47e7-4afc-a0d3-df9432961ef5" />
<img width="1366" height="768" alt="Traces - 4" src="https://github.com/user-attachments/assets/89fd1d41-1f61-4772-a64f-298dabfc05fe" />
<img width="1366" height="768" alt="Traces - 5" src="https://github.com/user-attachments/assets/e81c892f-2d81-4a39-8149-e2b6e7825191" />

### Observability, Models & Usage Metrics

<img width="1366" height="768" alt="OMU - 1" src="https://github.com/user-attachments/assets/00e71478-cb81-429d-904a-c5c79ce8dc25" />
<img width="1366" height="768" alt="OMU - 2" src="https://github.com/user-attachments/assets/79775a25-bef0-4ba4-9ede-8d574e93250a" />
<img width="1366" height="768" alt="OMU - 3" src="https://github.com/user-attachments/assets/02a38ad6-5c19-4f16-a134-0ae0b0cde2de" />
<img width="1366" height="768" alt="OMU - 4" src="https://github.com/user-attachments/assets/603bc223-f3e3-4f55-9558-1b4312321531" />
<img width="1366" height="768" alt="OMU - 5" src="https://github.com/user-attachments/assets/f94ccf3c-76f1-42cc-a2c7-95968936261b" />
<img width="1366" height="768" alt="OMU - 6" src="https://github.com/user-attachments/assets/fc0891f1-b127-47c9-a281-faa466979aea" />
<img width="1366" height="768" alt="OMU - 7" src="https://github.com/user-attachments/assets/f90a4045-097e-4ccd-8aff-966ebf430038" />

### Agent Engine Dashboard Logs

<img width="1366" height="Dashboard Logs - 1" alt="SS23" src="https://github.com/user-attachments/assets/7747cd14-793d-4d66-b4c3-a2f14fb4dcbd" />
<img width="1366" height="768" alt="Dashboard Logs - 2" src="https://github.com/user-attachments/assets/80593e80-b65c-4a9a-8291-fe221a4b3cc0" />
<img width="1366" height="768" alt="Dashboard Logs - 3" src="https://github.com/user-attachments/assets/8216679f-5331-44e1-b6d2-20a1842f29ea" />

### Logs Explorer

<img width="1366" height="768" alt="Logs Explorer" src="https://github.com/user-attachments/assets/43295aaf-8fa6-4177-8232-6a3c87113620" />

---

## Generative AI Capabilities & Integration

### ADK Agent Orchestration

- Defines and runs `transcript_summarization_agent` to parse multi-turn transcripts, extract structured summaries, and answer follow-up questions consistently.

### Vertex AI Agent Engine & Session State

- Manages deployed agent revisions, session IDs, conversation events, and execution traces on Vertex AI Agent Engine in `us-central1`.

### Gemini Model Reasoning & Cloud Logging

- Uses Gemini models to synthesize summaries, track conversational context, and format structured outputs, paired with Cloud Logging for operational visibility.

---

## AI-Assisted Development

AI tools can support the development and exploration of modern generative AI applications by helping explain unfamiliar code, investigate implementation issues, understand agent architectures, and improve technical documentation.

During the development and learning process for `Transcript Summarizer Agent`, AI assistance was used to support activities such as:

- Exploring Google ADK agent structure, prompts, and Vertex AI Agent Engine workflows.
- Testing transcript summarization prompts, multi-turn session follow-ups, and Logs Explorer queries.
- Structuring repository documentation, `.gitignore` rules, and contribution guides.

AI-generated suggestions and code should be reviewed critically, verified against the actual implementation, and tested before being adopted.

---

## Google Skills Challenge Lab Reference

This project was developed alongside hands-on Google Cloud learning lab modules.

### Challenge Lab

**Deploy ADK agents to Agent Runtime**

[Open the Google Skills lab](https://explore.qwiklabs.com/classrooms/21395/labs/115472)

### Learning Context

The repository serves as a personal source-code project associated with this learning experience.

It provides a place to explore and document:
- Building AI agents with Google ADK and Gemini models.
- Deploying agents to Vertex AI Agent Engine (`adk_to_agent_engine`).
- Managing Python dependencies with `requirements.txt`.
- Inspecting sessions, traces, and Cloud Logging output.

For official learning objectives, instructions, and environment setup requirements, refer to the lab link provided above.

--- 

## Future Enhancements

The following ideas could be considered for future versions of **Transcript Summarizer Agent**:

- **Structured Output Schemas:** Add typed output formats (such as JSON or standardized action-item schemas) for downstream CRM or ticketing integrations.
- **Automated Unit & Integration Tests:** Add `pytest` suites covering transcript summarization edge cases, session recall, and logging helpers.
- **Long-Transcript Chunking:** Support very long multi-speaker or meeting transcripts cleanly without losing early context or action items.
- **Evaluation Benchmarks:** Expand evaluation datasets in the Agent Engine Evaluation tab to measure summary accuracy and faithfulness.

> [!IMPORTANT]
> These are potential improvements, not claims that the features are already fully implemented.

---

## Resources

[![Google ADK](https://img.shields.io/badge/Google%20ADK-Documentation-4285F4?logo=google)](https://adk.dev/)
[![Agent Engine](https://img.shields.io/badge/Agent%20Engine-Documentation-4285F4?logo=googlecloud)](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Documentation-4285F4?logo=googlecloud)](https://cloud.google.com/docs)
[![Vertex AI](https://img.shields.io/badge/Vertex%20AI-Documentation-4285F4?logo=google)](https://cloud.google.com/vertex-ai/docs)
[![Gemini](https://img.shields.io/badge/Gemini-Documentation-8E75B2?logo=google)](https://ai.google.dev/gemini-api/docs)
[![Cloud Logging](https://img.shields.io/badge/Cloud%20Logging-Documentation-4285F4?logo=googlecloud)](https://cloud.google.com/logging/docs)
[![Python](https://img.shields.io/badge/Python-Documentation-3776AB?logo=python)](https://docs.python.org/3/)
[![Git](https://img.shields.io/badge/Git-Documentation-F05032?logo=git&logoColor=white)](https://git-scm.com/doc)
[![GitHub](https://img.shields.io/badge/GitHub-Documentation-181717?logo=github)](https://docs.github.com/)

---

## Disclaimer

**Transcript Summarizer Agent** is a learning and demonstration project associated with Google Cloud training.

The project utilizes third-party technologies and services, including Vertex AI Agent Engine, Vertex AI, Gemini, Google Cloud Logging, and Python packages. The availability, functionality, pricing, and policies of external cloud services are subject to their respective providers' terms.

Access to Qwiklabs / Google Cloud lab environments and temporary GCP projects expires after completion or quota exhaustion. A completed lab does not imply permanent public availability of the deployed agent service.

This repository is intended for educational and demonstration purposes. Do not commit API keys, access tokens, service-account credentials, `.env` files, or private configuration files to source control.

---

## Contributing

Contributions are welcome! If you would like to improve **Transcript Summarizer Agent**, fix a bug, add tests, or improve the documentation, please review the following guidelines:

- [Contributing Guide](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)

Please ensure that contributions are focused, documented, and tested where appropriate. Never include secrets or private configuration in issues, commits, or Pull Requests.

---

## License

This project is licensed under the **Apache License 2.0**.

See the [LICENSE](./LICENSE) file for details.

---

## Author

[**Sahil Sharma**](https://github.com/sahil-me)

Thank you for exploring **Transcript Summarizer Agent**! 

If you find the project useful, consider giving the repository a ⭐ to show your support.
