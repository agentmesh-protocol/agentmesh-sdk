import os
from autogen import ConversableAgent
from agentmesh.adapters import AutoGenAdapter
from agentmesh.gateway import GatewayClient

print("=== AgentMesh AutoGen Adapter Demo ===\n")

autogen_agent = ConversableAgent(
    name="autogen-assistant",
    system_message="You are a helpful assistant. Keep answers concise.",
    llm_config={
        "config_list": [{
            "model": "claude-sonnet-4-6",
            "api_key": os.environ.get("ANTHROPIC_API_KEY"),
            "api_type": "anthropic"
        }]
    },
    human_input_mode="NEVER"
)

mesh_agent = AutoGenAdapter(autogen_agent, name="autogen-agent")

print(f"Agent URI: {mesh_agent.uri}\n")

print("1. Im Gateway registrieren...")
result = mesh_agent.register(capabilities=["conversation", "question_answering"])
print(f"   Registriert: {result}\n")

print("2. Intent ausfuehren...")
response = mesh_agent.invoke("What is AgentMesh in one sentence?")
print(f"   Antwort: {response}\n")

print("3. Alle Agents im Netzwerk...")
gateway = GatewayClient()
found = gateway.find(capability="question_answering")
print(f"   Agents mit question_answering: {len(found.get('results', []))}")
print(f"\n Erster AutoGen Agent im AgentMesh Netzwerk!")
