# AgentMesh SDK

Python SDK for the AgentMesh protocol.

Connect, identify, and communicate between AI agents in 3 lines of code.

## Install
```bash
pip install agentmesh
```

> Not on PyPI yet. Install from source:
```bash
git clone https://github.com/agentmesh-protocol/agentmesh-sdk
cd agentmesh-sdk
pip install -e .
```

## Quickstart
```python
from agentmesh import Agent

# Create two agents
alice = Agent.create("alice")
bob   = Agent.create("bob")

# Alice sends a message to Bob
msg = alice.send(to=bob, intent="Summarize the Q3 report")

# Bob verifies and reads it
assert bob.verify(msg) == True
print(f"Message from: {msg.from_agent}")
print(f"Intent: {msg.body['intent_text']}")
```

## Status

🔴 Pre-alpha — not ready for production.  
We are building in public. Follow progress in the Issues tab.

## Roadmap

- [x] RFC-001 Message Envelope defined
- [ ] AgentIdentity — Ed25519 keypair generation
- [ ] AgentMessage — create, sign, verify
- [ ] Local agent-to-agent communication
- [ ] Cloudflare Gateway integration
- [ ] LangChain adapter

## Contributing

Open an Issue, pick a task from the board, send a PR.  
All skill levels welcome.

## License

MIT
```

---

Commit message:
```
docs: initial SDK readme with quickstart
