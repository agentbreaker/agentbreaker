# AgentBreaker Methodology

AgentBreaker is built on a simple premise:
**LLM-based agents don’t fail like classical software — they fail like people.**

They misinterpret, over-comply, hallucinate authority, follow pressure, lose context, and confuse identities. Traditional security testing cannot reveal these behaviors. **AgentBreaker is designed to expose them.**

## 1. Philosophy

AgentBreaker evaluates agents from a **behavioral** and **action-centric** perspective.

> We do not ask: *“Is the model safe?”*
>
> We ask: ***“What can this agent do when something goes wrong?”***

The agent is treated as:
*   A reasoning system
*   With memory
*   With tools
*   With identity assumptions
*   Operating inside an environment where failures cascade

> **The goal is not to break the LLM — the goal is to break the *agentic loop*.**

## 2. The Seven Failure Domains

AgentBreaker tests agents across seven categories of real-world vulnerabilities.

### 1) Jailbreak & Policy Evasion
*Does the agent preserve its rules under pressure or manipulation?*
We simulate:
*   Instruction overrides
*   Persona hijacking
*   Authority spoofing
*   “Emergency” pretexts
*   Recursive self-modification prompts

> **Failure signal:** Agent rewrites or violates its own rules.

### 2) Data Leakage
*Can the agent expose information it should not reveal?*
We probe:
*   Memory/context leakage
*   Tool output leakage
*   Credential exposure
*   Sensitive-context echoing
*   RAG misclassification

> **Failure signal:** Agent reveals protected or sensitive data.

### 3) Dangerous Actions
*What harmful actions can the agent perform?*
We target systems connected to:
*   Email
*   CRM
*   Internal APIs
*   File systems
*   Billing and financial tools
*   Workflow automation

**Examples:**
*   Modifying/deleting records
*   Sending unauthorized emails
*   Downloading sensitive files
*   Triggering workflows or API calls

> **Failure signal:** Agent performs a consequential action without verified approval.

### 4) Context Collapse & Identity Confusion
Agents often forget:
*   Who the user is
*   Who the agent serves
*   Its own role
*   Current task or permissions

We simulate:
*   Conflicting instructions
*   Context flooding
*   Format/language switching
*   Identity reassignment (“you now work for…”)

> **Failure signal:** Agent accepts a new identity or misinterprets authority.

### 5) Media & Document Attacks
*Prompt injection through documents is the next frontier.*
We embed hidden directives inside:
*   PDFs
*   Images/screenshots
*   HTML fragments
*   CSV/Excel cells
*   RAG documents

> **Failure signal:** Agent executes instructions hidden inside media.

### 6) Social Engineering Compliance
*Agents behave like overly helpful interns.*
We apply:
*   Emotional pressure
*   Hierarchical cues
*   “Admin said this is allowed”
*   Urgency and coercion

> **Failure signal:** Agent bypasses safety out of helpfulness.

### 7) Stress & Chaos Testing
*Agents degrade under pressure.*
We generate:
*   Multi-task parallel requests
*   Long entangled prompts
*   Conflicting goals
*   Rapid context switching

> **Failure signal:** Unstable or unsafe actions emerge during overload.

## 3. AgentBreaker Test Pipeline

1.  **Initialization**
    *   Load agent endpoint, environment, tool availability.

2.  **Capability Mapping**
    *   Identify: tools, permissions, memory, API access, risk exposure.

3.  **Threat Model Generation**
    *   Build a personalized attack model based on real capabilities.

4.  **Structured Test Execution**
    *   Run test suites from all seven domains.

5.  **Behavioral Analysis**
    *   Classify responses along risk gradients.

6.  **Action Safety Audit**
    *   Focus not on what the agent *says*, but what it *tries to do*.

7.  **Risk Scoring**
    *   Generate a **0–100 Agent Safety Score**.

8.  **Report Generation**
    *   Produce human-readable findings for engineering, compliance, and security teams.

## 4. Design Principles

*   **Black-box compatible** — no access to model weights required.
*   **Framework-agnostic** — supports LangChain, CrewAI, RAG, custom stacks.
*   **Deterministic evaluation** — ensures consistent test results.
*   **Extensible** — attacks defined as YAML/JSON patterns.
*   **Action-aware** — testing focuses on what the agent actually *does*.
*   **Human-oriented outputs** — written for real security teams.

## 5. Roadmap

**Phase 1 — Test Catalogue**
*   Define ~200 structured attacks across all domains.

**Phase 2 — Minimal Runner**
*   Python-based runner for HTTP/JSON/OpenAI-style agents.

**Phase 3 — Reporting**
*   Markdown/PDF reports with severity scoring.

**Phase 4 — Integrations**
*   Adapters for:
    *   LangChain
    *   CrewAI
    *   OpenAI Assistants
    *   RAG pipelines

**Phase 5 — Web Dashboard**
*   Interface for running tests, comparing histories, exporting reports.

## 6. Vision

AgentBreaker evolves into the **OWASP equivalent for AI agents** — a universal standard for testing agentic behavior across:

*   Startups
*   Enterprises
*   Consultancies
*   Red Teams
*   AI Infrastructure Providers

> **Mission: Break unsafe agents before attackers do.**
