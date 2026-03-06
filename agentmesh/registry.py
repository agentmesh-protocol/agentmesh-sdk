import json
import time
from typing import Optional


class AgentRecord:
    def __init__(self, uri: str, name: str, capabilities: list, ttl: int = 3600):
        self.uri = uri
        self.name = name
        self.capabilities = capabilities
        self.trust_score = 0.0
        self.registered_at = int(time.time())
        self.ttl = ttl

    def is_expired(self) -> bool:
        return int(time.time()) > self.registered_at + self.ttl

    def to_dict(self) -> dict:
        return {
            "uri": self.uri,
            "name": self.name,
            "capabilities": self.capabilities,
            "trust_score": self.trust_score,
            "registered_at": self.registered_at,
            "ttl": self.ttl
        }


class AgentRegistry:
    def __init__(self):
        self._agents: dict[str, AgentRecord] = {}

    def register(self, record: AgentRecord) -> bool:
        self._agents[record.uri] = record
        return True

    def find(self, capability: str, min_trust: float = 0.0) -> list:
        results = []
        for record in self._agents.values():
            if record.is_expired():
                continue
            if capability in record.capabilities:
                if record.trust_score >= min_trust:
                    results.append(record)
        results.sort(key=lambda r: r.trust_score, reverse=True)
        return results

    def get(self, uri: str) -> Optional[AgentRecord]:
        record = self._agents.get(uri)
        if record and not record.is_expired():
            return record
        return None

    def update_trust(self, uri: str, delta: float):
        record = self._agents.get(uri)
        if record:
            record.trust_score = max(0.0, min(1.0, record.trust_score + delta))
