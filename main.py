from agent.core import SkillBridgeAgent

def main():
    print("Welcome to Skill Bridge AI - Agent Edition")
    agent = SkillBridgeAgent()
    
    print("\n--- Generating Education Roadmap ---")
    roadmap1 = agent.generate_roadmap(
        track="Education & Technology",
        student_name="Vivek",
        current_info="Knows Python and SQL",
        goal="Data Scientist"
    )
    print(roadmap1)
    
    print("\n--- Generating Sports Roadmap ---")
    roadmap2 = agent.generate_roadmap(
        track="Sports Track",
        student_name="John Doe",
        current_info="Beginner Cricketer",
        goal="State Level Selection"
    )
    print(roadmap2)

if __name__ == "__main__":
    main()
