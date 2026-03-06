from agentmesh import Agent

print("=== AgentMesh Demo v0.1 ===\n")

# Zwei Agents erstellen
alice = Agent.create("alice")
bob   = Agent.create("bob")

print(f"Alice: {alice.uri}")
print(f"Bob:   {bob.uri}\n")

# Alice schickt eine Nachricht an Bob
msg = alice.send(
    to=bob,
    intent="Summarize the Q3 report in 200 words, formal tone."
)

print(f"Message ID:  {msg.id}")
print(f"From:        {msg.to_dict()['from']}")
print(f"To:          {msg.to_dict()['to']}")
print(f"Intent:      {msg.body['intent_text']}")
print(f"Signature:   {msg.signature[:32]}...\n")

# Bob verifiziert die Nachricht
is_valid = bob.verify(msg)
print(f"Bob verifies message: {is_valid}")
print(f"Bob inbox count:      {len(bob.inbox)}")

if is_valid:
    print("\n✓ Erste AgentMesh Kommunikation erfolgreich.")
```

---

Commit message:
```
demo: first agent-to-agent communication
```

---

Danach noch eine letzte Datei — **"Add file" → "Create new file"**

Dateiname:
```
setup.py
