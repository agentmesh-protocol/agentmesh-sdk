import os
from agentmesh import Agent
from agentmesh.llm_agent import LLMAgent

print("=== AgentMesh LLM Demo ===\n")

alice = Agent.create("alice")
bob = LLMAgent.create(
    name="bob",
    system_prompt="You are Bob, a helpful summarization agent. Keep answers concise."
)

print(f"Alice: {alice.uri}")
print(f"Bob:   {bob.uri}\n")

msg = alice.send(
    to=bob,
    intent="Explain what AgentMesh is in 2 sentences."
)

print(f"Alice asks: {msg.body['intent_text']}\n")

reply = bob.receive_and_respond(msg)

print(f"Bob replies: {reply.body['intent_text']}")
print(f"\n✓ Erste echte LLM Agent-Kommunikation erfolgreich.")
