import json
import uuid
import time
from agentmesh.identity import AgentIdentity


class AgentMessage:
    """
    A signed message between two AgentMesh agents.
    Follows RFC-001 envelope format.
    """

    def __init__(self, from_agent: AgentIdentity, to_uri: str, intent: str):
        self.id = f"msg_{uuid.uuid4().hex[:8]}"
        self.from_agent = from_agent
        self.to_uri = to_uri
        self.timestamp = int(time.time())
        self.body = {
            "intent_text": intent,
            "confidence": 1.0
        }
        self.signature = None

    def sign(self) -> "AgentMessage":
        payload = self._payload_bytes()
        self.signature = self.from_agent.sign(payload).hex()
        return self

    def _payload_bytes(self) -> bytes:
        payload = {
            "id": self.id,
            "from": self.from_agent.uri,
            "to": self.to_uri,
            "timestamp": self.timestamp,
            "body": self.body
        }
        return json.dumps(payload, sort_keys=True).encode()

    def to_dict(self) -> dict:
        return {
            "agentmesh_version": "0.1",
            "id": self.id,
            "from": self.from_agent.uri,
            "to": self.to_uri,
            "timestamp": self.timestamp,
            "msg_type": "INTENT",
            "body": self.body,
            "signature": self.signature
        }

    def __repr__(self):
        return f"<AgentMessage id={self.id} from={self.from_agent.uri}>"
```

---

Commit message:
```
feat: add AgentMessage with signing — RFC-001
