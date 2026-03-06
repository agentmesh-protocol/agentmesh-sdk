from agentmesh.agent import Agent
from agentmesh.gateway import GatewayClient


class CrewAIAdapter:
    def __init__(self, name: str, role: str, goal: str, gateway_url: str = None):
        self.agent = Agent.create(name)
        self.gateway = GatewayClient(gateway_url) if gateway_url else GatewayClient()
        self.name = name
        self.role = role
        self.goal = goal

    def register(self, capabilities: list) -> dict:
        return self.gateway.register(
            uri=self.agent.uri,
            name=self.name,
            capabilities=capabilities
        )

    def invoke(self, intent: str) -> str:
        import os
        import anthropic
        client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        system = f"You are {self.name}. Role: {self.role}. Goal: {self.goal}."
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            system=system,
            messages=[{"role": "user", "content": intent}]
        )
        return response.content[0].text

    def send(self, to_uri: str, intent: str) -> dict:
        fake_agent = type("F", (), {"uri": to_uri, "inbox": []})()
        msg = self.agent.send(to=fake_agent, intent=intent)
        return self.gateway.send(
            from_uri=self.agent.uri,
            to_uri=to_uri,
            intent=intent,
            signature=msg.signature
        )

    @property
    def uri(self) -> str:
        return self.agent.uri
