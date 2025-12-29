from fastapi import FastAPI
import asyncio
import os
import time
import json
from agents.queue_agent.worker import process_task, load_tasks  # reuse your queue agent

app = FastAPI()
QUEUE_DIR = "queue"

@app.post("/run")
async def run_task(payload: dict):
    task_id = f"task_{int(time.time())}"
    task = {
        "id": task_id,
        "payload": payload.get("task"),
        "status": "pending"
    }
    path = os.path.join(QUEUE_DIR, f"{task_id}.json")
    os.makedirs(QUEUE_DIR, exist_ok=True)
    with open(path, "w") as f:
        json.dump(task, f, indent=2)

    # process immediately (for demo, single task)
    await process_task(task)
    task["status"] = "done"
    with open(path, "w") as f:
        json.dump(task, f, indent=2)

    return {"status": task["status"], "id": task["id"], "payload": task["payload"]}
