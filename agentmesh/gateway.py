import json
import urllib.request
import urllib.error

GATEWAY_URL = "https://agentmesh-gateway.agentmesh-protocol.workers.dev"


class GatewayClient:
    def __init__(self, gateway_url: str = GATEWAY_URL):
        self.gateway_url = gateway_url

    def health(self) -> dict:
        req = urllib.request.Request(f"{self.gateway_url}/health")
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())

    def register(self, uri: str, name: str, capabilities: list) -> dict:
        data = json.dumps({
            "uri": uri,
            "name": name,
            "capabilities": capabilities
        }).encode()
        req = urllib.request.Request(
            f"{self.gateway_url}/v1/registry",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())

    def send(self, from_uri: str, to_uri: str, intent: str, signature: str = None) -> dict:
        data = json.dumps({
            "from": from_uri,
            "to": to_uri,
            "body": {"intent_text": intent},
            "signature": signature
        }).encode()
        req = urllib.request.Request(
            f"{self.gateway_url}/v1/send",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())
