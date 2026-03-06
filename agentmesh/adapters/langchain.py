from agentmesh.agent import Agent
from agentmesh.gateway import GatewayClient


class LangChainAdapter:
    def __init__(self, langchain_llm, name: str, gateway_url: str = None):
        self.llm = langchain_llm
        self.agent = Agent.create(name)
        self.gateway = GatewayClient(gateway_url) if gateway_url else GatewayClient()
        self.name = name

    def register(self, capabilities: list) -> dict:
        return self.gateway.register(
            uri=self.agent.uri,
            name=self.name,
            capabilities=capabilities
        )

    def invoke(self, intent: str) -> str:
        from langchain_core.messages import HumanMessage
        result = self.llm.invoke([HumanMessage(content=intent)])
        return result.content

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
