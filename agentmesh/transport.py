import json
import time
import requests
from agentmesh.identity import AgentIdentity
from agentmesh.message import AgentMessage
from agentmesh.gateway import GatewayClient


class DirectTransport:
    def __init__(self, identity: AgentIdentity, gateway_url: str = None):
        self.identity = identity
        self.gateway = GatewayClient(gateway_url) if gateway_url else GatewayClient()
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "AgentMesh-SDK/0.1.0"
        })

    def send(self, to_uri: str, intent: str, timeout: int = 30) -> dict:
        registry = self.gateway.find(capability="")
        endpoint = None
        for agent in registry.get("results", []):
            if agent["uri"] == to_uri:
                endpoint = agent.get("endpoint")
                break

        msg = AgentMessage(
            from_agent=self.identity,
            to_uri=to_uri,
            intent=intent
        )
        msg.sign()
        envelope = msg.to_dict()

        if endpoint:
            try:
                response = self.session.post(
                    f"{endpoint}",
                    json=envelope,
                    timeout=timeout
                )
                response.raise_for_status()
                return {"transport": "direct", "result": response.json()}
            except Exception:
                pass

        result = self.gateway.send(
            from_uri=self.identity.uri,
            to_uri=to_uri,
            intent=intent,
            signature=msg.signature
        )
        return {"transport": "gateway", "result": result}
