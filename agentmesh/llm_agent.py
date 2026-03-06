import os
import requests
import anthropic
from agentmesh.agent import Agent
from agentmesh.message import AgentMessage


class LLMAgent(Agent):
    def __init__(self, name: str, system_prompt: str = None,
                 backend: str = "anthropic", model: str = None,
                 ollama_url: str = "http://localhost:11434"):
        super().__init__(name)
        self.system_prompt = system_prompt or f"You are {name}, an AI agent in the AgentMesh network."
        self.backend = backend
        self.ollama_url = ollama_url

        if backend == "anthropic":
            self.model = model or "claude-sonnet-4-6"
            self.client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        elif backend == "ollama":
            self.model = model or "llama3"
            self.client = None
        else:
            raise ValueError(f"Unknown backend: {backend}")

    @classmethod
    def create(cls, name: str, system_prompt: str = None,
               backend: str = "anthropic", model: str = None,
               ollama_url: str = "http://localhost:11434") -> "LLMAgent":
        return cls(name, system_prompt, backend, model, ollama_url)

    def invoke(self, text: str) -> str:
        if self.backend == "anthropic":
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                system=self.system_prompt,
                messages=[{"role": "user", "content": text}]
            )
            return response.content[0].text
        elif self.backend == "ollama":
            response = requests.post(
                f"{self.ollama_url}/api/chat",
                json={
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": text}
                    ],
                    "stream": False
                },
                timeout=60
            )
            response.raise_for_status()
            return response.json()["message"]["content"]

    def receive_and_respond(self, msg: AgentMessage) -> str:
        if not self.verify(msg):
            raise ValueError("Message signature invalid")
        return self.invoke(msg.body["intent_text"])
