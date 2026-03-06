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
- RFC-003 Trust Score Verification
- AgentIdentity mit Ed25519 Keypair
- AgentMessage erstellen, signieren, verifizieren
- Agent send, verify, inbox
- AgentRegistry register, find, update_trust
- TrustManager RFC-003 Implementierung
- LLMAgent mit echter Claude API
- GatewayClient SDK verbunden mit Cloudflare
- KV Storage persistent in Cloudflare
- LangChain Adapter
- AutoGen Adapter
- CrewAI Adapter
- Professionelles VC-style README
- 15 Tests alle gruen
- GitHub Actions CI Pipeline gruen
- GitHub Actions Publish Pipeline gruen
- Cloudflare Gateway live im Internet mit 4 Endpoints
- pip install agentmesh-protocol auf PyPI live (v0.1.1)

## PyPI

URL: https://pypi.org/project/agentmesh-protocol/
Install: pip install agentmesh-protocol
Version: 0.1.1

## Gateway

URL: https://agentmesh-gateway.agentmesh-protocol.workers.dev
Endpoints:
- GET  /health        -> status + kv check
- POST /v1/registry   -> Agent registrieren (persistent in KV)
- GET  /v1/registry   -> Agents suchen nach capability
- POST /v1/send       -> Nachricht senden
- POST /v1/trust      -> Trust Score updaten

## SDK Struktur

agentmesh/__init__.py
agentmesh/identity.py
agentmesh/message.py
agentmesh/agent.py
agentmesh/registry.py
agentmesh/llm_agent.py
agentmesh/gateway.py
agentmesh/trust.py
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
CONTEXT.md
.github/workflows/ci.yml
.github/workflows/publish.yml

## Unterstuetzte Frameworks

- Nativer AgentMesh: Agent, LLMAgent
- LangChain: LangChainAdapter
- AutoGen: AutoGenAdapter
- CrewAI: CrewAIAdapter

## Naechste Schritte

1. Auf Twitter/X posten - Build in Public starten
2. RFC-004 Agent-to-Agent HTTP Transport
3. JavaScript/TypeScript SDK
4. Erste externe Contributors gewinnen

## Wichtige Regeln

- Python-Dateien NUR per Terminal mit cat EOF erstellen
- Nie per GitHub Web-Editor fuer Code
- Anthropic API Key: sk-ant-api03-...
- Cloudflare Token direkt per export setzen wenn noetig
- Immer: git add, commit, push, Actions Tab pruefen
- Neue PyPI Releases: neue GitHub Release erstellen -> triggert publish.yml
