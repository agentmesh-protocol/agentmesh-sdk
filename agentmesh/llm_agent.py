import os
import anthropic
from agentmesh.agent import Agent
from agentmesh.message import AgentMessage


class LLMAgent(Agent):
    def __init__(self, name: str, system_prompt: str = None):
        super().__init__(name)
        self.system_prompt = system_prompt or f"You are {name}, an AI agent in the AgentMesh network."
        self.client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    @classmethod
    def create(cls, name: str, system_prompt: str = None) -> "LLMAgent":
        return cls(name, system_prompt)

    def receive_and_respond(self, msg: AgentMessage) -> str:
        if not self.verify(msg):
            raise ValueError("Message signature invalid")

        response = self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            system=self.system_prompt,
            messages=[
                {"role": "user", "content": msg.body["intent_text"]}
            ]
        )

        return response.content[0].text
