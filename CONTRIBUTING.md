<!---
Copyright 2026 Sahíl Sharma. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Contribute to Transcript Summarizer Agent

Everyone is welcome to contribute, and we value every contribution. Code contributions are not the only way to support the project. Improving agent reasoning workflows, summarization prompts, Vertex AI Agent Engine deployment scripts, session state handling, Cloud Logging observability, error handling, performance, security, testing, or documentation are all valuable ways to contribute to **Transcript Summarizer Agent**.

This project was developed as part of hands-on exploration into building stateful AI agents with Google Agent Development Kit (ADK), Gemini models, and serverless deployment on Vertex AI Agent Engine (`adk_to_agent_engine`) with Cloud Logging integration. Contributions that improve summarization accuracy, multi-turn session reliability, maintainability, and practical cloud-native AI agent patterns are especially welcome.

If you find this project helpful, consider sharing it with others, referencing it in your blogs or projects, discussing it on social platforms, or simply giving the repository a ⭐️ to support the project and the community.

**However you choose to contribute, please be mindful and respect our [Code of Conduct](https://github.com/sahil-me/transcript-summarizer-agent/blob/main/CODE_OF_CONDUCT.md).**

## Ways to contribute

There are several ways you can contribute to **Transcript Summarizer Agent**.

- **ADK Agent Workflows & Prompts:** Enhance agent system instructions, summarization structure (issues, root causes, resolutions, action items), and multi-turn follow-up responses in `transcript_summarization_agent/agent.py`.
- **Vertex AI Agent Engine Deployment & Client Queries:** Improve deployment utilities (`agent_engine_utils.py`), remote querying (`query_agent_engine.py`), and managed session handling on Vertex AI Agent Engine.
- **Gemini Model Configuration:** Improve model selection, generation settings, structured output formatting (bullet points, tables), and response consistency.
- **Observability & Cloud Logging:** Enhance structured logging (`CloudLoggingHandler`), execution trace inspection, and diagnostic visibility in Google Cloud Logs Explorer and Agent Engine Playground.
- **Python & Dependency Management:** Maintain clean Python typing, async/sync execution, error handling, and `requirements.txt` consistency across root and agent modules.
- **Performance Optimization:** Reduce response latency, optimize staging bucket serialization, and streamline local-to-remote Agent Engine execution.
- **Security & Credential Handling:** Help ensure safe handling of API keys, Google Cloud credentials, GCS bucket names, `.env` isolation, and least-privilege IAM access.
- **Testing:** Add or improve unit tests, session persistence checks, and end-to-end Playground / Agent Engine integration tests.
- **Documentation:** Improve the `README`, setup instructions, architecture diagrams, ADK-to-Agent-Engine walkthroughs, and contribution guides.

> All contributions are valuable to the project and its learning community. 🥰

## Submitting a bug-related issue or feature request

Feel free to open an issue when you encounter a bug or have an idea for improving **Transcript Summarizer Agent**. Include relevant error logs, reproduction steps, Python/ADK versions, or Google Cloud / Vertex AI Agent Engine configuration context when appropriate.

Please check the existing issues before creating a new one. This helps avoid duplicate reports and makes it easier to track existing problems.

### Did you find a bug?

**Transcript Summarizer Agent** becomes more reliable through community feedback, issue reporting, testing, and meaningful contributions.

Before reporting an issue, please make sure the bug has not already been reported under the repository's **Issues** section.

When submitting a bug report, please include the following information:
- Your operating system and development environment (e.g., Windows, macOS, Linux, Cloud Shell).
- Python version (`python --version`) and Google ADK / Vertex AI SDK versions.
- Execution target (local ADK runner, `query_agent_engine.py`, or deployed Vertex AI Agent Engine Playground).
- Steps to reproduce the issue (including sample non-sensitive transcript inputs, if applicable).
- A short description of the expected behavior and what actually happened.
- Relevant error messages, stack traces, or Cloud Logging / terminal logs.
- The affected component, such as `transcript_summarization_agent` (`agent.py`, `query_agent_engine.py`), `agent_engine_utils.py`, or `requirements.txt`.
- Screenshots or terminal outputs, if applicable.
- Any other information that may help reproduce or understand the issue.

Please do not include **API keys**, **passwords**, **authentication tokens**, **service-account credentials**, `.env` **files**, **GCP project IDs/URLs with sensitive context**, or other **sensitive information** in an issue.

### Do you want a new feature?

If there is a new feature you'd like to see in **Transcript Summarizer Agent**, please open an issue and describe:

1. **Motivation**

   Explain the problem, limitation, or use case that the feature would address.

2. **Feature Description**

   Describe the proposed feature and how you would expect it to work from a user or caller perspective.

3. **ADK, Agent Engine & AI Integration**

   If the feature affects AI or runtime capabilities, explain how it should influence agent instructions, session memory behavior, model selection, or summary output formatting.

4. **Service & Project Architecture**

   If the feature affects `transcript_summarization_agent`, `agent_engine_utils.py`, Cloud Logging, or Vertex AI Agent Engine deployment, describe the expected changes to modules, scripts, or configuration files.

5. **Implementation Details**

   If you have an implementation idea, architecture suggestion, or code snippet, feel free to include it.

6. **Additional References**

   If the feature is inspired by an external project, paper, design, or technical reference, please include the relevant link.

A clear and well-written feature request makes it easier to evaluate and discuss the proposal.

## Do you want to improve Vertex AI Agent Engine deployment and utilities?

The `agent_engine_utils.py` and `query_agent_engine.py` modules handle packaging, staging, querying, and observability for the deployed agent on Vertex AI Agent Engine.

You can contribute by:

- Improving deployment lifecycle scripts, staging bucket handling, and error reporting in `agent_engine_utils.py`.
- Enhancing remote session querying, streaming response handling, and Cloud Logging integration in `query_agent_engine.py`.
- Keeping dependency specifications aligned across root `requirements.txt` and `transcript_summarization_agent/requirements.txt`.
- Improving parity between local ADK testing and deployed Vertex AI Agent Engine execution.

When modifying deployment or query scripts, ensure that environment variables remain cleanly decoupled and outputs stay clear and predictable.

## Do you want to improve ADK agent and summarization logic?

The `transcript_summarization_agent` module (`agent.py`) drives the conversational intelligence, transcript extraction, and multi-turn session reasoning of the application.

You can contribute by:

- Refining system instructions and few-shot examples for accurate issue, root-cause, resolution, and action-item extraction across diverse transcript styles (support calls, standups, interviews).
- Improving handling of edge cases such as malformed transcripts, missing speaker labels, or off-topic prompts.
- Enhancing multi-turn session context retention for follow-up questions and structured table/bullet transformations.
- Ensuring clean separation between core agent definitions and cloud deployment wrappers.

## Do you want to improve testing and reliability?

Testing ensures the agent and deployment utilities remain stable and easy to maintain.

You can contribute by:

- Adding unit tests for agent configuration, prompt formatting, and helper utilities.
- Adding integration tests for session creation, multi-turn recall, and `query_agent_engine.py` invocations.
- Testing error handling when Vertex AI endpoints, GCS staging buckets, or credentials are unavailable.
- Improving test coverage and reproducible setup instructions.

## Do you want to improve documentation?

We're always looking for improvements that make **Transcript Summarizer Agent** clearer and easier to understand.

You can contribute by:

- Fixing typos or grammatical errors.
- Improving the `README` and local / Vertex AI Agent Engine setup guides.
- Documenting the project architecture, folder structure (`transcript_summarization_agent/` and `agent_engine_utils.py`), session persistence flow, and Cloud Logging queries.
- Adding example transcripts, follow-up prompts, and Playground / Logs Explorer verification steps.

Documentation contributions are especially appreciated when they help new contributors understand the project, set up their environment, and get started safely.

## Fixing outstanding issues

If you notice an existing issue and have a fix in mind, feel free to **[start contributing](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)** and open a Pull Request.

### Making code changes

<details>
<summary><strong>Step-by-step contribution workflow</strong></summary>

#### 1. Fork the repository

Go to the [Transcript Summarizer Agent repository](https://github.com/sahil-me/transcript-summarizer-agent) on GitHub and click the **Fork** button.

#### 2. Clone your forked repository

Replace `<username>` with your GitHub username.

```bash
git clone https://github.com/<username>/transcript-summarizer-agent.git
```

Navigate into the project directory:

```bash
cd transcript-summarizer-agent
```

#### 3. Create a new branch

Create a separate branch for your feature or bug fix.

```bash
git checkout -b feature/your-feature-name
```

For a bug fix, you can use a name such as:

```bash
git checkout -b fix/issue-description
```

#### 4. Ensure Python and virtual environment tools are installed

Verify your Python installation:

```bash
python --version
```

#### 5. Install dependencies

Create and activate a virtual environment, then install dependencies for the workspace and agent module:

```bash
python -m venv .venv

# On Windows (PowerShell): .venv\Scripts\Activate.ps1

# On macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt

pip install -r transcript_summarization_agent/requirements.txt
```

#### 6. Configure environment variables

Configure your local `.env` file or environment variables (`GOOGLE_CLOUD_PROJECT`, `APP_NAME`, and GCS staging bucket settings) according to the project's instructions, keeping `.env` untracked.

> Never commit API keys, tokens, `.env` files, service account JSON files, or secrets to the repository.

#### 7. Run the project locally or query Agent Engine

Run or test the agent locally via ADK or query your deployed Vertex AI Agent Engine instance to verify everything works before making changes:

```bash
python transcript_summarization_agent/query_agent_engine.py
```

#### 8. Make your changes

- Develop the feature or fix the issue.
- Follow the existing project structure, Python naming conventions, and clean code practices.
- Keep changes focused and maintainable.
- Avoid unrelated modifications.
- Test your changes thoroughly across relevant components.

#### 9. Run tests

Run your test suite or verification scripts to ensure no regressions were introduced:

```bash
pytest
```

Verify that the agent summarizes transcripts accurately, preserves session context, and handles errors gracefully.

#### 10. Commit your changes

From the repository root, review the files you have changed and stage only the intended changes.

```bash
git status

git add <file-or-directory>

git commit -m "Describe your change"
```

Avoid committing `.env` files, virtual environments (`.venv/`), `__pycache__/`, build artifacts, or unrelated modifications.

#### 11. Push to your fork

```bash
git push origin feature/your-feature-name
```

Replace the branch name if you used a different one.

#### 12. Create a Pull Request

Open your fork on GitHub and create a Pull Request targeting the original Transcript Summarizer Agent repository.

In your Pull Request description:
- Explain what you changed.
- Reference any related issue.
- Describe agent prompt, session handling, Cloud Logging, or Vertex AI Agent Engine configuration updates.
- Include logs, test outputs, or Playground screenshots when appropriate.

#### 13. Address feedback

If maintainers leave comments or request changes, address the feedback and push the required updates to your branch.

Thank you for taking the time to review and improve the project!

</details>

## Contribution Guidelines

To keep the project maintainable and welcoming:
- Keep Pull Requests focused on a single feature, fix, or improvement.
- Avoid unnecessary changes to unrelated files.
- Follow existing Python style guidelines and project conventions.
- Test changes locally or in Vertex AI Agent Engine before submitting a Pull Request.
- Keep API keys, credentials, .env files, and sensitive configuration out of the repository.
- Provide clear commit messages and Pull Request descriptions.
- Be respectful and constructive when reviewing or discussing contributions.

## I want to become a maintainer of the project. How do I get there?

**Transcript Summarizer Agent** is a learning and demonstration project focused on building stateful AI agents with Google ADK, Gemini models, and Vertex AI Agent Engine.

Contributors interested in improving agent workflows, summarization prompts, Vertex AI Agent Engine integrations, Cloud Logging observability, testing, documentation, and architecture are welcome.

If you are interested in contributing at a deeper level, consistently submitting meaningful improvements, reviewing Pull Requests, improving documentation, or helping maintain the project, feel free to get involved and collaborate.

Thank you for contributing to **Transcript Summarizer Agent**! 📝
