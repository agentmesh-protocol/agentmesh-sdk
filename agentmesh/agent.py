from agentmesh.identity import AgentIdentity
from agentmesh.message import AgentMessage


class Agent:
    """
    Main AgentMesh agent class.
    Create, send, and verify messages between agents.
    """

    def __init__(self, name: str):
        self.identity = AgentIdentity(name)
        self.name = name
        self.uri = self.identity.uri
        self.inbox = []

    @classmethod
    def create(cls, name: str) -> "Agent":
        return cls(name)

    def send(self, to: "Agent", intent: str) -> AgentMessage:
        msg = AgentMessage(
            from_agent=self.identity,
            to_uri=to.uri,
            intent=intent
        )
        msg.sign()
        to.inbox.append(msg)
        return msg

    def verify(self, msg: AgentMessage) -> bool:
        if msg.signature is None:
            return False
        payload = msg._payload_bytes()
        signature_bytes = bytes.fromhex(msg.signature)
        return msg.from_agent.verify(payload, signature_bytes)

    def __repr__(self):
        return f"<Agent name={self.name} uri={self.uri}>"
```

---

Commit message:
```
feat: add Agent class with send and verify
