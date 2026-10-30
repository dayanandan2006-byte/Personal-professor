def build_roadmap_prompt(track, current_info, goal, score_data, market_trends):
    return f"""
    Act as a Personal AI Mentor for the {track}.
    Current Student Info: {current_info}
    Goal: {goal}
    Student Assessment Score: {score_data}
    Current Market Trends: {market_trends}
    
    Please provide a structured, personalized roadmap.
    """
