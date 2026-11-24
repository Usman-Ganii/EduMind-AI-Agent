import streamlit as st
from google import genai
import time


def ask_gemini(prompt: str, context: str = "") -> str:

    api_key = st.secrets.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "Gemini API key not found. Check secrets.toml."
        )

    client = genai.Client(api_key=api_key)

    full_prompt = prompt

    if context:
        full_prompt += (
            "\n\nSTUDY MATERIAL / CONTEXT:\n" + context
        )

    model = "gemini-3.5-flash-lite"

    # Retry temporary server errors
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=model,
                contents=full_prompt
            )

            if not response.text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            return response.text

        except Exception as exc:

            error = str(exc).upper()

            temporary_error = (
                "503" in error
                or "UNAVAILABLE" in error
                or "HIGH DEMAND" in error
            )

            if temporary_error and attempt < 2:
                time.sleep(2 ** (attempt + 1))
                continue

            raise RuntimeError(str(exc)) from exc

    raise RuntimeError("Gemini could not respond. Please try again.")