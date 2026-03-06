import pytest
from agentmesh import Agent, AgentMessage


def test_agent_has_uri():
    alice = Agent.create("alice")
    assert alice.uri.startswith("agent://alice-")


def test_two_agents_have_different_uris():
    alice = Agent.create("alice")
    bob = Agent.create("bob")
    assert alice.uri != bob.uri


def test_send_creates_message():
    alice = Agent.create("alice")
    bob = Agent.create("bob")
    msg = alice.send(to=bob, intent="Hello Bob")
    assert msg is not None
    assert msg.body["intent_text"] == "Hello Bob"


def test_message_is_signed():
    alice = Agent.create("alice")
    bob = Agent.create("bob")
    msg = alice.send(to=bob, intent="Hello Bob")
    assert msg.signature is not None
    assert len(msg.signature) > 0


def test_bob_verifies_alice_message():
    alice = Agent.create("alice")
    bob = Agent.create("bob")
    msg = alice.send(to=bob, intent="Hello Bob")
    assert bob.verify(msg) == True


def test_message_lands_in_inbox():
    alice = Agent.create("alice")
    bob = Agent.create("bob")
    alice.send(to=bob, intent="Hello Bob")
    assert len(bob.inbox) == 1


def test_multiple_messages_in_inbox():
    alice = Agent.create("alice")
    bob = Agent.create("bob")
    alice.send(to=bob, intent="Message 1")
    alice.send(to=bob, intent="Message 2")
    assert len(bob.inbox) == 2


def test_message_to_dict_has_required_fields():
    alice = Agent.create("alice")
    bob = Agent.create("bob")
    msg = alice.send(to=bob, intent="Hello")
    d = msg.to_dict()
    assert "agentmesh_version" in d
    assert "id" in d
    assert "from" in d
    assert "to" in d
    assert "signature" in d
