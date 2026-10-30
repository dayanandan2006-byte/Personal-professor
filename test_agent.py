import pytest
from agent.core import SkillBridgeAgent

def test_agent_initialization():
    agent = SkillBridgeAgent()
    assert agent.name == "Skill Bridge Personal Mentor"

def test_roadmap_generation():
    agent = SkillBridgeAgent()
    res = agent.generate_roadmap("Tech", "TestUser", "Python", "Dev")
    assert "[AI GENERATED ROADMAP]" in res
