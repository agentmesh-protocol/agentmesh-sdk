import os
from agentmesh.adapters import CrewAIAdapter
from agentmesh.gateway import GatewayClient

print("=== AgentMesh CrewAI Adapter Demo ===\n")

researcher = CrewAIAdapter(
    name="researcher",
    role="Senior Research Analyst",
    goal="Find and summarize key information on any topic"
)

writer = CrewAIAdapter(
    name="writer",
    role="Technical Writer",
    goal="Write clear and concise content based on research"
)

print(f"Researcher URI: {researcher.uri}")
print(f"Writer URI:     {writer.uri}\n")

print("1. Agents registrieren...")
researcher.register(capabilities=["research", "summarization"])
writer.register(capabilities=["writing", "content_creation"])
print("   Beide registriert\n")

print("2. Researcher analysiert...")
research = researcher.invoke("What are the top 3 benefits of AI agent communication protocols?")
print(f"   Research: {research[:150]}...\n")

print("3. Writer schreibt basierend auf Research...")
article = writer.invoke(f"Write a one-paragraph summary based on this research: {research[:300]}")
print(f"   Article: {article[:150]}...\n")

print("4. Alle Agents im Netzwerk...")
gateway = GatewayClient()
found = gateway.find(capability="research")
print(f"   Agents mit research: {len(found.get('results', []))}")
print(f"\n Erstes CrewAI-Style Team im AgentMesh Netzwerk!")
