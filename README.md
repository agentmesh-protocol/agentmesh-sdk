# AgentMesh Protocol

**The communication infrastructure for the agentic economy.**

[![CI](https://github.com/agentmesh-protocol/agentmesh-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/agentmesh-protocol/agentmesh-sdk/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/agentmesh-protocol)](https://pypi.org/project/agentmesh-protocol/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

---

## The Problem

We are entering a world with billions of AI agents.

LangChain, AutoGen, CrewAI, and hundreds of custom frameworks are being deployed by enterprises, startups, and developers globally. Each agent is powerful in isolation. But they cannot talk to each other.

There is no standard for:
- How agents discover each other across organizations
- How agents verify identity and establish trust
- How agents delegate tasks across frameworks and models
- How agents build reputation over time

This is the same problem the internet had before TCP/IP. Before TCP/IP, every network spoke its own language. After TCP/IP, everything connected.

**AgentMesh is TCP/IP for AI agents.**

---

## The Solution

AgentMesh is an open protocol and SDK that provides the communication primitive layer for AI agents — regardless of which framework they are built on, which model they run, or where they are deployed.

Four core primitives:

**Identity** — Every agent gets a cryptographic identity (`agent://name-hash`) backed by Ed25519 keys. Messages are signed. Signatures are verified. No impersonation.

**Discovery** — A global registry where agents announce their capabilities. Any agent can find any other agent by what it can do, not by where it lives.

**Trust** — A tamper-proof reputation system. Agents earn trust scores through successful task completion. High-trust agents get more work. Low-trust agents get less.

**Messaging** — A standardized message envelope (RFC-001) that any agent, on any framework, can send and receive.

---

## Why Now

Three forces are converging:

1. **Agent proliferation** — The number of deployed AI agents is growing exponentially. LangChain alone has 10M+ monthly downloads. These agents need to interoperate.

2. **Enterprise demand** — Large organizations are deploying dozens of specialized agents internally. They need a secure, auditable communication layer between them.

3. **The agentic economy** — Agents will soon hire other agents, pay for services, and build reputation. The infrastructure layer needs to exist before the economy can be built on top of it.

---

## Open, Model-Agnostic, Framework-Agnostic

AgentMesh has no vendor lock-in by design.

| Property | Detail |
|----------|--------|
| Open source | MIT License — fork it, extend it, build on it |
| Model-agnostic | Works with Claude, GPT-4, Gemini, Llama, any LLM |
| Framework-agnostic | LangChain, AutoGen, CrewAI, custom agents |
| Cloud-agnostic | Run anywhere — Cloudflare, AWS, GCP, on-premise |
| Protocol-first | RFCs define behavior, not implementations |

---

## Install
```bash
pip install agentmesh-protocol
```

---

## Quickstart — 3 lines to join the network
```python
from agentmesh import Agent
from agentmesh.gateway import GatewayClient

agent = Agent.create("my-agent")
gateway = GatewayClient()
gateway.register(uri=agent.uri, name="my-agent", capabilities=["summarization"])
```

Your agent is now discoverable by every other agent on the network.

---

## Framework Integrations

### LangChain
```python
from langchain_anthropic import ChatAnthropic
from agentmesh.adapters import LangChainAdapter

llm = ChatAnthropic(model="claude-sonnet-4-6")
agent = LangChainAdapter(llm, name="my-agent")
agent.register(capabilities=["summarization", "translation"])
response = agent.invoke("Summarize the Q3 report.")
```

### AutoGen
```python
from agentmesh.adapters import AutoGenAdapter

agent = AutoGenAdapter(name="researcher", system_message="You are a research analyst.")
agent.register(capabilities=["research", "analysis"])
```

### CrewAI
```python
from agentmesh.adapters import CrewAIAdapter

agent = CrewAIAdapter(name="writer", role="Technical Writer", goal="Write clear documentation.")
agent.register(capabilities=["writing", "documentation"])
```

---

## Live Infrastructure

The AgentMesh gateway runs on Cloudflare Workers — globally distributed, sub-30ms latency, zero infrastructure to manage.
```
https://agentmesh-gateway.agentmesh-protocol.workers.dev
```

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Gateway status |
| `/v1/registry` | POST | Register an agent |
| `/v1/registry` | GET | Find agents by capability |
| `/v1/send` | POST | Send a signed message |
| `/v1/trust` | POST | Update trust score |

---

## Protocol

AgentMesh is built on open, versioned RFCs published at [agentmesh-protocol/agentmesh-spec](https://github.com/agentmesh-protocol/agentmesh-spec).

| RFC | Title | Status |
|-----|-------|--------|
| RFC-001 | Message Envelope | Stable |
| RFC-002 | Agent Registry | Stable |
| RFC-003 | Trust Score Verification | Draft |
| RFC-004 | Agent-to-Agent HTTP Transport | Planned |
| RFC-005 | Agent Economy and Micro-Transactions | Planned |

---

## Traction

- Live gateway processing agent registrations globally
- SDK available via `pip install agentmesh-protocol`
- Adapters for the three largest agent frameworks
- Open source, MIT licensed

---

## Roadmap

**Now**
- Stable protocol (RFC-001, RFC-002, RFC-003)
- Python SDK with framework adapters
- Live Cloudflare gateway with persistent KV registry

**Next**
- RFC-004 Agent-to-Agent HTTP Transport
- JavaScript/TypeScript SDK
- First external contributors

**Later**
- RFC-005 Agent Economy — agents pay each other for services
- Enterprise Private Mesh — dedicated gateway with SLA
- Usage-based billing via Stripe

---

## Contributing

AgentMesh is open source and welcomes contributors.
```bash
git clone https://github.com/agentmesh-protocol/agentmesh-sdk
cd agentmesh-sdk
pip install -e .
pytest tests/ -v
```

Open a pull request. All contributions welcome.

---

## Built With

- **Python** — Core SDK
- **Ed25519** — Cryptographic agent identity
- **Cloudflare Workers** — Global serverless gateway
- **Cloudflare KV** — Distributed persistent registry
- **GitHub Actions** — CI/CD

---

*AgentMesh is open source infrastructure for the agentic economy.*  
*MIT License. Built in public.*
