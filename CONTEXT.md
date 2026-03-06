# AgentMesh — Projektkontext

Beim Start eines neuen Chats: "Wir bauen AgentMesh. Lies CONTEXT.md auf github.com/agentmesh-protocol/agentmesh-sdk und mach weiter."

## Was ist AgentMesh?

Das TCP/IP fuer AI-Agent-Kommunikation. Ein offenes Protokoll das definiert wie AI Agents sich finden, miteinander kommunizieren, Vertrauen aufbauen und Aufgaben delegieren.

## Repos

- agentmesh-spec: Protokoll-Dokumente (RFCs)
- agentmesh-sdk: Python SDK
- agentmesh-gateway: Cloudflare Worker live unter agentmesh-gateway.agentmesh-protocol.workers.dev

## Aktueller Stand

Fertig:
- RFC-001 Nachrichtenformat
- RFC-002 Agent Registry
- AgentIdentity mit Ed25519 Keypair
- AgentMessage erstellen, signieren, verifizieren
- Agent send, verify, inbox
- AgentRegistry register, find, update_trust
- LLMAgent mit echter Claude API
- GatewayClient SDK verbunden mit Cloudflare
- KV Storage persistent in Cloudflare
- LangChain Adapter
- AutoGen Adapter
- CrewAI Adapter
- Professionelles README mit Badges und Quickstart
- 15 Tests alle gruen
- GitHub Actions CI Pipeline gruen
- Cloudflare Gateway live im Internet
- Alle Dependencies sauber in setup.py

## Unterstuetzte Frameworks

| Framework | Adapter | Klasse |
|-----------|---------|--------|
| Nativer AgentMesh | eingebaut | Agent, LLMAgent |
| LangChain | LangChainAdapter | agentmesh.adapters |
| AutoGen | AutoGenAdapter | agentmesh.adapters |
| CrewAI | CrewAIAdapter | agentmesh.adapters |

## Gateway

URL: https://agentmesh-gateway.agentmesh-protocol.workers.dev
Endpoints:
- GET  /health        -> status + kv check
- POST /v1/registry   -> Agent registrieren (persistent in KV)
- GET  /v1/registry   -> Agents suchen nach capability
- POST /v1/send       -> Nachricht senden

## SDK Struktur

agentmesh/__init__.py
agentmesh/identity.py
agentmesh/message.py
agentmesh/agent.py
agentmesh/registry.py
agentmesh/llm_agent.py
agentmesh/gateway.py
agentmesh/adapters/__init__.py
agentmesh/adapters/langchain.py
agentmesh/adapters/autogen.py
agentmesh/adapters/crewai.py
tests/test_agent.py
tests/test_registry.py
demo.py
demo_llm.py
demo_gateway.py
demo_langchain.py
demo_autogen.py
demo_crewai.py
setup.py
README.md
.github/workflows/ci.yml

## Dependencies

cryptography>=41.0.0
requests>=2.31.0
anthropic>=0.18.0
langchain>=0.1.0
langchain-anthropic>=0.1.0
langchain-core>=0.1.0
pyautogen
crewai

## Naechste Schritte

1. Twitter/X Build in Public starten
2. RFC-003 Trust Score Verifikation
3. pip install agentmesh auf PyPI veroeffentlichen
4. Erste externe Contributors gewinnen

## Wichtige Regeln

- Python-Dateien NUR per Terminal mit cat EOF erstellen
- Nie per GitHub Web-Editor fuer Code
- Anthropic API Key: sk-ant-api03-...
- Cloudflare Token muss manchmal direkt per export gesetzt werden
- Immer: git add, commit, push, Actions Tab pruefen
