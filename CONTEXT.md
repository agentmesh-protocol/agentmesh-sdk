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
- 15 Tests alle gruen
- GitHub Actions CI Pipeline gruen
- Cloudflare Gateway live im Internet
- Dependencies sauber in setup.py

## Gateway

URL: https://agentmesh-gateway.agentmesh-protocol.workers.dev
Endpoints:
- GET  /health        -> status + kv check
- POST /v1/registry   -> Agent registrieren (persistent in KV)
- GET  /v1/registry   -> Agents suchen nach capability
- POST /v1/send       -> Nachricht senden

## SDK Struktur

agentmesh/__init__.py
agentmesh/identity.py     - AgentIdentity, Ed25519
agentmesh/message.py      - AgentMessage, RFC-001
agentmesh/agent.py        - Agent Klasse
agentmesh/registry.py     - AgentRegistry, RFC-002
agentmesh/llm_agent.py    - LLMAgent mit Claude API
agentmesh/gateway.py      - GatewayClient HTTP
tests/test_agent.py
tests/test_registry.py
demo.py                   - lokale Demo
demo_llm.py               - Claude API Demo
demo_gateway.py           - Gateway Demo
setup.py
.github/workflows/ci.yml

## Naechste Schritte

1. LangChain Adapter - bestehende Agents einbinden
2. RFC-003 Trust Score Verifikation
3. Twitter/X Build in Public starten
4. README ausbauen - Projekt professionell praesentieren

## Wichtige Regeln

- Python-Dateien NUR per Terminal mit cat EOF erstellen
- Nie per GitHub Web-Editor fuer Code
- API Keys nur als GitHub Secret oder export in Terminal
- Immer: git add, commit, push, Actions Tab pruefen
- Cloudflare Token muss manchmal direkt per export gesetzt werden
