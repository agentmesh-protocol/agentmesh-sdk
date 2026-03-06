# AgentMesh — Projektkontext

Beim Start eines neuen Chats: "Wir bauen AgentMesh. Lies CONTEXT.md auf github.com/agentmesh-protocol/agentmesh-sdk und mach weiter."

## Was ist AgentMesh?

Das TCP/IP fuer AI-Agent-Kommunikation. Ein offenes Protokoll das definiert wie AI Agents sich finden, miteinander kommunizieren, Vertrauen aufbauen und Aufgaben delegieren.

## Repos

- agentmesh-spec: Protokoll-Dokumente (RFCs)
- agentmesh-sdk: Python SDK
- agentmesh-gateway: Cloudflare Worker — live unter agentmesh-gateway.agentmesh-protocol.workers.dev

## Aktueller Stand

Fertig:
- RFC-001 Nachrichtenformat
- RFC-002 Agent Registry
- AgentIdentity mit Ed25519 Keypair
- AgentMessage erstellen, signieren, verifizieren
- Agent send, verify, inbox
- AgentRegistry register, find, update_trust
- LLMAgent mit echter Claude API
- GatewayClient — SDK verbunden mit Cloudflare
- 15 Tests alle gruen
- GitHub Actions CI Pipeline gruen
- Cloudflare Gateway live im Internet

## Gateway

URL: https://agentmesh-gateway.agentmesh-protocol.workers.dev
Endpoints:
- GET  /health
- POST /v1/send
- POST /v1/registry

## SDK Struktur

agentmesh/__init__.py
agentmesh/identity.py
agentmesh/message.py
agentmesh/agent.py
agentmesh/registry.py
agentmesh/llm_agent.py
agentmesh/gateway.py
tests/test_agent.py
tests/test_registry.py
demo.py
demo_llm.py
demo_gateway.py
setup.py
.github/workflows/ci.yml

## Naechste Schritte

1. KV Storage - Registry persistent in Cloudflare speichern
2. RFC-003 Trust Score Verifikation
3. LangChain Adapter
4. Twitter/X Build in Public starten
5. requests zu setup.py hinzufuegen

## Wichtige Regeln

- Python-Dateien NUR per Terminal mit cat EOF erstellen
- Nie per GitHub Web-Editor fuer Code
- API Keys nur als GitHub Secret oder export in Terminal
- Immer: git add, commit, push, Actions Tab pruefen
- requests Library ist installiert aber noch nicht in setup.py
