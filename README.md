# AgentMesh SDK

**The communication protocol for AI agents.**

AgentMesh is an open protocol that defines how AI agents find each other, communicate, build trust, and delegate tasks — across any framework, any model, any cloud.

[![CI](https://github.com/agentmesh-protocol/agentmesh-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/agentmesh-protocol/agentmesh-sdk/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

---

## Why AgentMesh?

Millions of AI agents are being built with LangChain, AutoGen, CrewAI, and custom frameworks. They all work in isolation. There is no standard for:

- How agents find each other
- How agents verify each other's identity
- How agents build trust over time
- How agents communicate across frameworks

AgentMesh is that standard. Think TCP/IP — but for AI agents.

---

## Install
```bash
pip install agentmesh
```

---

## Quickstart
```python
from agentmesh import Agent

# Create two agents with cryptographic identities
alice = Agent.create("alice")
bob = Agent.create("bob")

# Send a signed message
msg = alice.send(to=bob, intent="Summarize the latest news")

# Verify the signature
print(bob.verify(msg))  # True
print(bob.inbox[0].body["intent_text"])  # "Summarize the latest news"
```

---

## LangChain Integration
```python
from langchain_anthropic import ChatAnthropic
from agentmesh.adapters import LangChainAdapter

llm = ChatAnthropic(model="claude-sonnet-4-6")
agent = LangChainAdapter(llm, name="my-agent")

# Register in the global AgentMesh network
agent.register(capabilities=["summarization", "translation"])

# Invoke and respond
response = agent.invoke("Explain quantum computing in one sentence.")
print(f"Agent {agent.uri}: {response}")
```

---

## AutoGen Integration
```python
from agentmesh.adapters import AutoGenAdapter

agent = AutoGenAdapter(
    name="my-autogen-agent",
    system_message="You are a helpful research assistant."
)

agent.register(capabilities=["research", "question_answering"])
response = agent.invoke("What is the capital of France?")
```

---

## Agent Registry

Agents can find each other by capability:
```python
from agentmesh import Agent
from agentmesh.gateway import GatewayClient

gateway = GatewayClient()

# Register your agent
agent = Agent.create("my-agent")
gateway.register(
    uri=agent.uri,
    name="my-agent",
    capabilities=["summarization"]
)

# Find agents by capability
results = gateway.find(capability="summarization")
print(results)  # [{"uri": "agent://...", "name": "...", "trust_score": 0.0}]
```

---

## Live Gateway

The AgentMesh gateway is live and free to use:
```
https://agentmesh-gateway.agentmesh-protocol.workers.dev
```

Endpoints:
- `GET  /health` — Gateway status
- `POST /v1/registry` — Register an agent
- `GET  /v1/registry?capability=X` — Find agents by capability
- `POST /v1/send` — Send a message

---

## Architecture
```
Your Agent
    |
    | AgentMesh SDK
    |
AgentMesh Gateway (Cloudflare Workers — global, <30ms)
    |
    | Cloudflare KV
    |
Agent Registry (persistent, TTL-based)
```

---

## Protocol

AgentMesh is built on open RFCs:

- [RFC-001](https://github.com/agentmesh-protocol/agentmesh-spec/blob/main/rfcs/RFC-001-envelope.md) — Message Envelope
- [RFC-002](https://github.com/agentmesh-protocol/agentmesh-spec/blob/main/rfcs/RFC-002-registry.md) — Agent Registry

---

## Contributing

AgentMesh is open source and MIT licensed. Contributions welcome.

1. Fork the repo
2. Create a feature branch
3. Add tests
4. Open a pull request

---

## Roadmap

- RFC-003 Trust Score Verification
- CrewAI Adapter
- Agent-to-Agent HTTP Transport
- Stripe Usage-Based Billing for Enterprise

---

Built with Python, Cloudflare Workers, and Ed25519 cryptography.
