import os
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from agentmesh.adapters import LangChainAdapter
from agentmesh.gateway import GatewayClient

print("=== AgentMesh LangChain Adapter Demo ===\n")

llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

mesh_agent = LangChainAdapter(llm, name="langchain-agent")

print(f"Agent URI: {mesh_agent.uri}\n")

print("1. Im Gateway registrieren...")
result = mesh_agent.register(capabilities=["text_analysis", "summarization"])
print(f"   Registriert: {result}\n")

print("2. Intent ausfuehren...")
response = mesh_agent.invoke("Explain AgentMesh in one sentence.")
print(f"   Antwort: {response}\n")

print("3. Andere Agents im Netzwerk suchen...")
gateway = GatewayClient()
found = gateway.find(capability="summarization")
print(f"   Agents mit summarization: {len(found.get('results', []))}")
print(f"\n Erster LangChain Agent im AgentMesh Netzwerk!")
