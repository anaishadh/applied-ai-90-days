from planner import plan
from executor import execute

if __name__ == "__main__":
    task = input("Enter task: ")

    steps = plan(task)
    results = execute(steps)

print("\n--- Final Summary ---")

for r in results:
    if r["status"] == "success":
        print(f"✅ {r['agent']} succeeded in {r['attempts']} attempt(s)")
    else:
        print(f"❌ {r['agent']} failed after {r['attempts']} attempts")

