import sys
from agency import ProjectChimera

def main():
    """
    Main Entry Point for Project Chimera Agency.
    Orchestrates the Swarm (Planner, Worker, Judge) based on user goals.
    """
    print("--- Project Chimera: Autonomous Influencer Network ---")
    print("Status: Governance Active | CFO Judge: Online | Swarm: Standby")
    
    if len(sys.argv) > 1:
        goal = " ".join(sys.argv[1:])
        print(f"Goal Ingested: {goal}")
        # In a real implementation, this would trigger:
        # agency = ProjectChimera()
        # agency.run_campaign(goal)
    else:
        print("Usage: python main.py <campaign_goal>")

if __name__ == "__main__":
    main()
