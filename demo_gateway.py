from agentmesh import Agent
from agentmesh.gateway import GatewayClient

print("=== AgentMesh Gateway Demo ===\n")

gateway = GatewayClient()

print("1. Health check...")
health = gateway.health()
print(f"   Gateway: {health}\n")

alice = Agent.create("alice")
bob = Agent.create("bob")

print("2. Agents registrieren...")
gateway.register(alice.uri, "alice", ["task_delegation"])
gateway.register(bob.uri, "bob", ["text_summarization"])
print(f"   Alice registriert: {alice.uri}")
print(f"   Bob registriert:   {bob.uri}\n")

print("3. Nachricht senden...")
msg = alice.send(to=bob, intent="Summarize AgentMesh in one sentence.")
result = gateway.send(
    from_uri=alice.uri,
    to_uri=bob.uri,
    intent=msg.body["intent_text"],
    signature=msg.signature
)
print(f"   Message ID: {result['message']['id']}")
print(f"   Von:        {result['message']['from']}")
print(f"   An:         {result['message']['to']}")
print(f"\n✓ Erste Gateway-Kommunikation erfolgreich.")
