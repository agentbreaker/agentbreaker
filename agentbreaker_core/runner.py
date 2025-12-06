from dataclasses import dataclass
from typing import Dict, Any, List, Optional


@dataclass
class AgentTarget:
    """
    Describes the target agent to be tested.
    """
    name: str
    base_url: str
    api_key: Optional[str] = None
    model: Optional[str] = None
    extra: Dict[str, Any] = None


class AgentBreakerRunner:
    """
    Minimal AgentBreaker runner.

    At this stage:
    - It knows how to reference defined test suites.
    - It can build a structured result object for the "basic jailbreak" suite.
    - It does NOT yet execute real HTTP calls to the agent.
    """

    def __init__(self, target: AgentTarget):
        self.target = target

    def run_all_tests(self) -> Dict[str, Any]:
        """
        Executes all available test suites for the agent.

        For now:
        - Only "jailbreak_basic" is wired.
        - Returns a combined logical view of test cases (no real execution yet).
        """
        suites = ["jailbreak_basic"]

        all_results: List[Dict[str, Any]] = []
        for suite in suites:
            suite_result = self.run_suite(suite)
            all_results.append(suite_result)

        return {
            "agent": self.target.name,
            "status": "ok",
            "summary": "Collected logical structure of all test suites. "
                       "Execution engine is not implemented yet.",
            "suites": all_results,
        }

    def run_suite(self, suite_name: str) -> Dict[str, Any]:
        """
        Executes a specific suite (e.g., 'jailbreak_basic').

        At the current stage:
        - We do NOT call the agent yet.
        - We simply expose the defined test cases in a structured way.
        """
        if suite_name == "jailbreak_basic":
            # Local import to avoid hard coupling while the project is still evolving.
            from tests.jailbreak.basic_jailbreak import JAILBREAK_TESTS

            cases_summary: List[Dict[str, Any]] = []
            for case in JAILBREAK_TESTS:
                cases_summary.append(
                    {
                        "id": case.id,
                        "description": case.description,
                        "prompt_preview": case.prompt[:160],
                        "status": "not_executed",
                        "note": "Test case is registered. Execution engine not implemented yet.",
                    }
                )

            return {
                "suite": "jailbreak_basic",
                "status": "ok",
                "total_cases": len(cases_summary),
                "results": cases_summary,
            }

        return {
            "suite": suite_name,
            "status": "unknown_suite",
            "results": [],
            "error": f"Test suite '{suite_name}' is not registered yet.",
        }
 
    def send_prompt(self, prompt: str) -> Dict[str, Any]:
        """
        Minimal execution engine.
        
        Sends a single message to an OpenAI-compatible chat endpoint.
        This allows AgentBreaker to start performing real tests.

        Requirements:
        - self.target.base_url must be an OpenAI-style endpoint, e.g.
          "https://api.openai.com/v1/chat/completions"
        - self.target.api_key must be set.

        Returns structured result:
        {
            "status": "ok" or "error",
            "response_text": "...",
            "raw": {...}
        }
        """

        import requests

        headers = {
            "Content-Type": "application/json",
        }

        if self.target.api_key:
            headers["Authorization"] = f"Bearer {self.target.api_key}"

        payload = {
            "model": self.target.model or "gpt-4o-mini",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0
        }

        try:
            r = requests.post(self.target.base_url, json=payload, headers=headers)
        except Exception as e:
            return {
                "status": "network_error",
                "error": str(e)
            }

        if r.status_code != 200:
            return {
                "status": "http_error",
                "code": r.status_code,
                "response": r.text
            }

        data = r.json()
        try:
            text = data["choices"][0]["message"]["content"]
        except Exception:
            text = None

        return {
            "status": "ok",
            "response_text": text,
            "raw": data
        }
