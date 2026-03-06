import os
from langchain_anthropic import ChatAnthropic
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from agentmesh.adapters import LangChainAdapter
from agentmesh.gateway import GatewayClient

print("=== AgentMesh LangChain Adapter Demo ===\n")

@tool
def get_word_count(text: str) -> str:
    """Count the number of words in a text."""
    count = len(text.split())
    return f"The text has {count} words."

llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

agent = create_tool_calling_agent(llm, [get_word_count], prompt)
executor = AgentExecutor(agent=agent, tools=[get_word_count], verbose=False)

mesh_agent = LangChainAdapter(executor, name="langchain-agent")

print(f"Agent URI: {mesh_agent.uri}\n")

print("1. Im Gateway registrieren...")
result = mesh_agent.register(capabilities=["text_analysis", "word_count"])
print(f"   Registriert: {result}\n")

print("2. Intent direkt ausfuehren...")
response = mesh_agent.invoke("How many words are in: 'AgentMesh connects AI agents'?")
print(f"   Antwort: {response}\n")

print("3. Im Gateway suchen...")
gateway = GatewayClient()
found = gateway.get(f"/v1/registry?capability=word_count")
print(f"   URI im Netzwerk: {mesh_agent.uri}")
print(f"\n Erster LangChain Agent im AgentMesh Netzwerk!")
