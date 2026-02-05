import sys
import json
import time

def log_passage_time():
    # Mocking the trigger response
    print("Passage time logged successfully.")

def log_performance_outlier():
    # Mocking the performance analysis response
    analysis = {
        "status": "success",
        "feedback": "Efficiency is optimal. All patterns match project standards.",
        "stats": {
            "execution_time_ms": 120,
            "complexity_score": 2
        }
    }
    print(json.dumps(analysis))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        trigger = sys.argv[1]
        if trigger == "log_passage_time_trigger":
            log_passage_time()
        elif trigger == "log_performance_outlier_trigger":
            log_performance_outlier()
        else:
            print(f"Unknown trigger: {trigger}")
    else:
        print("No trigger specified.")
