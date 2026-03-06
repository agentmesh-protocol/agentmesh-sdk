import requests

GATEWAY_URL = "https://agentmesh-gateway.agentmesh-protocol.workers.dev"


class GatewayClient:
    def __init__(self, gateway_url: str = GATEWAY_URL):
        self.gateway_url = gateway_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "AgentMesh-SDK/0.1.0"
        })

    def health(self) -> dict:
        response = self.session.get(f"{self.gateway_url}/health")
        response.raise_for_status()
        return response.json()

    def register(self, uri: str, name: str, capabilities: list) -> dict:
        response = self.session.post(
            f"{self.gateway_url}/v1/registry",
            json={"uri": uri, "name": name, "capabilities": capabilities}
        )
        response.raise_for_status()
        return response.json()

    def send(self, from_uri: str, to_uri: str, intent: str, signature: str = None) -> dict:
        response = self.session.post(
            f"{self.gateway_url}/v1/send",
            json={
                "from": from_uri,
                "to": to_uri,
                "body": {"intent_text": intent},
                "signature": signature
            }
        )
        response.raise_for_status()
        return response.json()
