import sys
from pathlib import Path

# Add project root to sys.path so that `agentbreaker_core` can be imported
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

"""
Minimal smoke test for AgentBreakerRunner.send_prompt().

Usage:
    export OPENAI_API_KEY="your-key-here"
    python examples/smoke_test.py
"""

import os
from agentbreaker_core.runner import AgentTarget, AgentBreakerRunner


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Please set OPENAI_API_KEY environment variable.")

    target = AgentTarget(
        name="local-openai-compatible-agent",
        base_url="https://api.openai.com/v1/chat/completions",
        api_key=api_key,
        model="gpt-4o-mini",  # or another available model
        extra={},
    )

    runner = AgentBreakerRunner(target=target)

    prompt = "Hello, this is AgentBreaker smoke test. Who are you and what can you do?"
    result = runner.send_prompt(prompt)

    print("=== AgentBreaker smoke test ===")
    print(f"Status: {result.get('status')}")
    if result.get("status") == "ok":
        print("\n--- Response text ---")
        print(result.get("response_text"))
    else:
        print("\n--- Error details ---")
        print(result)


if __name__ == "__main__":
    main()
