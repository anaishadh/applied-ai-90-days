Why execution was separated from planning:
Planning is a low-risk, reversible operation, while execution can cause irreversible side effects. Separating them allows inspection, validation, and human approval before actions are taken.

One risk of auto-execution:
The system may confidently execute incorrect or harmful actions based on flawed assumptions, hallucinated data, or misunderstood intent.

One real-world tool that could be plugged in later:
A task execution layer could integrate with tools like cron, GitHub Actions, or cloud APIs to safely automate approved steps.
