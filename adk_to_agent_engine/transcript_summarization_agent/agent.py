import os
from functools import cached_property
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.models import Gemini
from google.genai import Client, types

RETRY_OPTIONS = types.HttpRetryOptions(initial_delay=1, max_delay=3, attempts=30)

load_dotenv()


class GlobalGemini(Gemini):
    """Gemini model that always calls the global Vertex AI endpoint.

    Agent Runtime sets GOOGLE_CLOUD_LOCATION to the region the agent is
    deployed in (us-central1), but current Gemini models are served from the
    global endpoint, so the model client is pinned to "global" here.
    """

    @cached_property
    def api_client(self) -> Client:
        return Client(
            vertexai=True,
            project=os.getenv("GOOGLE_CLOUD_PROJECT"),
            location="global",
            http_options=types.HttpOptions(retry_options=self.retry_options),
        )


root_agent = Agent(
    name="transcript_summarization_agent",
    description="Summarizes chat transcripts.",
    model=GlobalGemini(
        model=os.getenv("MODEL", "gemini-2.5-flash"),
        retry_options=RETRY_OPTIONS
    ),
    instruction="Summarize the provided chat transcript.",
)