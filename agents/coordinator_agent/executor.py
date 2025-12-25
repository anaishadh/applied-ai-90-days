def execute(plan_steps):
    results = []

    max_retries = 2

    for step in plan_steps:
        agent = step["agent"]
        task = step["task"]

        attempt = 0
        success = False

        while attempt < max_retries and not success:
            try:
                if agent == "research":
                    result = f"Research result for: {task}"
                elif agent == "automation":
                    if attempt == 0:
                        raise RuntimeError("Temporary automation failure")
                    result = f"Automation decision for: {task}"
                else:
                    result = "Unknown agent"

                results.append({
                    "agent": agent,
                    "status": "success",
                    "output": result,
                    "attempts": attempt + 1
                })
                success = True

            except Exception as e:
                attempt += 1
                if attempt == max_retries:
                    results.append({
                        "agent": agent,
                        "status": "failed",
                        "error": str(e),
                        "attempts": attempt
                    })

    return results
