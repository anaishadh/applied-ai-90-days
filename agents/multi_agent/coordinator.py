import json
from agents import AGENTS

MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def run_pipeline(topic):
    memory = load_memory()
    memory["topic"] = topic

    for agent_name, meta in AGENTS.items():
        memory[meta["output"]] = f"Output of {agent_name} for topic '{topic}'"
        save_memory(memory)

    return memory

if __name__ == "__main__":
    run_pipeline("agentic AI fundamentals")
