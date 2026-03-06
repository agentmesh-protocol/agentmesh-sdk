from agentmesh import Agent, AgentRegistry, AgentRecord


def make_record(name, capabilities):
    agent = Agent.create(name)
    return AgentRecord(
        uri=agent.uri,
        name=name,
        capabilities=capabilities
    )


def test_register_agent():
    registry = AgentRegistry()
    record = make_record("bob", ["text_summarization"])
    registry.register(record)
    assert registry.get(record.uri) is not None


def test_find_by_capability():
    registry = AgentRegistry()
    record = make_record("bob", ["text_summarization"])
    registry.register(record)
    results = registry.find("text_summarization")
    assert len(results) == 1
    assert results[0].name == "bob"


def test_find_unknown_capability():
    registry = AgentRegistry()
    record = make_record("bob", ["text_summarization"])
    registry.register(record)
    results = registry.find("image_generation")
    assert len(results) == 0


def test_trust_score_filter():
    registry = AgentRegistry()
    record = make_record("bob", ["text_summarization"])
    registry.register(record)
    results = registry.find("text_summarization", min_trust=0.5)
    assert len(results) == 0


def test_update_trust():
    registry = AgentRegistry()
    record = make_record("bob", ["text_summarization"])
    registry.register(record)
    registry.update_trust(record.uri, 0.8)
    updated = registry.get(record.uri)
    assert updated.trust_score == 0.8


def test_trust_capped_at_one():
    registry = AgentRegistry()
    record = make_record("bob", ["text_summarization"])
    registry.register(record)
    registry.update_trust(record.uri, 999.0)
    assert registry.get(record.uri).trust_score == 1.0


def test_find_sorted_by_trust():
    registry = AgentRegistry()
    alice = make_record("alice", ["translation"])
    bob = make_record("bob", ["translation"])
    registry.register(alice)
    registry.register(bob)
    registry.update_trust(alice.uri, 0.9)
    registry.update_trust(bob.uri, 0.3)
    results = registry.find("translation")
    assert results[0].name == "alice"
