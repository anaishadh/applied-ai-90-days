AGENTS = {
    "research_agent": {
        "role": "Collect facts and references",
        "input": "topic",
        "output": "raw_notes"
    },
    "analysis_agent": {
        "role": "Analyze notes and extract insights",
        "input": "raw_notes",
        "output": "analysis"
    },
    "writer_agent": {
        "role": "Write structured output",
        "input": "analysis",
        "output": "draft"
    },
    "review_agent": {
        "role": "Review and improve draft",
        "input": "draft",
        "output": "final"
    }
}
