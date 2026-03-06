import os
from agentmesh.adapters import AutoGenAdapter
from agentmesh.gateway import GatewayClient

print("=== AgentMesh AutoGen-Style Adapter Demo ===\n")

agent = AutoGenAdapter(
    name="autogen-agent",
    system_message="You are a helpful assistant. Keep answers concise."
)

print(f"Agent URI: {agent.uri}\n")

print("1. Im Gateway registrieren...")
result = agent.register(capabilities=["conversation", "question_answering"])
print(f"   Registriert: {result}\n")

print("2. Intent ausfuehren...")
response = agent.invoke("What is AgentMesh in one sentence?")
print(f"   Antwort: {response}\n")

print("3. Andere Agents im Netzwerk suchen...")
gateway = GatewayClient()
found = gateway.find(capability="question_answering")
print(f"   Agents mit question_answering: {len(found.get('results', []))}")
print(f"\n AutoGen-Style Agent im AgentMesh Netzwerk!")
