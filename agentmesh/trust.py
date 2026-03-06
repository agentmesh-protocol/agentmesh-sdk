import time
from agentmesh.gateway import GatewayClient


class TrustManager:
    def __init__(self, gateway_url: str = None):
        self.gateway = GatewayClient(gateway_url) if gateway_url else GatewayClient()
        self._updates = []

    def report(self, from_uri: str, about_uri: str, task_id: str,
               outcome: str, quality: str, signature: str = None) -> dict:
        if outcome not in ("success", "failure", "timeout"):
            raise ValueError(f"Invalid outcome: {outcome}")
        if quality not in ("confirmed", "rejected", "neutral"):
            raise ValueError(f"Invalid quality: {quality}")
        if from_uri == about_uri:
            raise ValueError("Agent cannot report trust about itself")

        record = {
            "from": from_uri,
            "about": about_uri,
            "task_id": task_id,
            "outcome": outcome,
            "quality": quality,
            "timestamp": int(time.time()),
            "signature": signature
        }
        self._updates.append(record)

        delta = self._calculate_delta(outcome, quality)
        return self.gateway.update_trust(about_uri, delta)

    def _calculate_delta(self, outcome: str, quality: str) -> float:
        delta = 0.0
        if outcome == "success":
            delta += 0.01
        elif outcome in ("failure", "timeout"):
            delta -= 0.05

        if quality == "confirmed":
            delta += 0.02
        elif quality == "rejected":
            delta -= 0.10

        return delta
