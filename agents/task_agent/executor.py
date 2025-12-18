import json
import os

def execute_tasks(task_file: str):
    if not os.path.exists(task_file):
        print("❌ Task file does not exist.")
        return

    with open(task_file, "r") as f:
        data = json.load(f)

    steps = data.get("steps", [])

    if not steps:
        print("❌ No steps to execute.")
        return

    print("🚀 Executing tasks:")
    for idx, step in enumerate(steps, start=1):
        print(f"{idx}. {step}")

    print("✅ Execution complete (simulated).")
