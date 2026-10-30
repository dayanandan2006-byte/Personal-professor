from .llm import generate_response
from .prompt_builder import build_roadmap_prompt
from tools.data_query import get_student_score
from tools.web_search import search_trends

class SkillBridgeAgent:
    def __init__(self):
        self.name = "Skill Bridge Personal Mentor"
        
    def generate_roadmap(self, track, student_name, current_info, goal):
        # Use tools to enrich context
        score = get_student_score(student_name)
        trends = search_trends(goal)
        
        prompt = build_roadmap_prompt(track, current_info, goal, score, trends)
        response = generate_response(prompt)
        return response
