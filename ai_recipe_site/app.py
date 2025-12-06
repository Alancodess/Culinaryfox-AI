from flask import Flask, render_template, request
from groq import Groq
import os
import json

app = Flask(__name__)

# Read API key securely from an environment variable (NO key in code)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY environment variable is not set.")

# Groq client
client = Groq(api_key=GROQ_API_KEY)

# Model used
MODEL_NAME = "llama-3.3-70b-versatile"


def _clean_model_json(content: str) -> str:
    """
    Clean the model content in case it is wrapped in ```json ... ``` or ``` ... ```.
    """
    if not content:
        return ""
    text = content.strip()
    if text.startswith("```"):
        parts = text.split("```")
        if len(parts) >= 3:
            text = parts[1]
        else:
            text = text.strip("`")
    return text.strip()


def call_groq_for_recipes(ingredients_text: str):
    """
    Ask the Groq model for recipes in a structured JSON format.
    Returns: (recipes_list_or_none, error_message_or_none)
    """

    system_message = (
        "You are a very patient cooking teacher for absolute beginners.\n"
        "The user will give you a list of ingredients they have.\n"
        "Your job is to suggest 1–3 realistic dishes that can be made mostly "
        "from those ingredients.\n"
        "\n"
        "For EACH dish, you MUST return a JSON object with:\n"
        "  - name (string)\n"
        "  - description (string) — 2–3 lines explaining what the dish is like.\n"
        "  - time_minutes (integer) — total approximate time from start to finish.\n"
        "  - required_ingredients (list of strings)\n"
        "  - optional_ingredients (list of strings)\n"
        "  - steps (list of strings)\n"
        "\n"
        "Use simple English.\n"
        "Return ONLY a JSON array. No markdown."
    )

    user_message = (
        f"I have these ingredients:\n\n{ingredients_text}\n\n"
        "Suggest some recipes ONLY in JSON format."
    )

    try:
        chat_completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ],
        )
    except Exception as e:
        return None, f"Error calling Groq API: {e}"

    raw_content = chat_completion.choices[0].message.content

    if not raw_content:
        return None, "Model returned an empty response."

    cleaned = _clean_model_json(raw_content)

    try:
        recipes = json.loads(cleaned)
        if not isinstance(recipes, list):
            recipes = [recipes]
        return recipes, None
    except Exception as e:
        return None, (
            "Failed to read JSON.\n\n"
            f"Raw response:\n{raw_content}\n\n"
            f"Error: {e}"
        )


@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []
    error = None
    ingredients = ""

    if request.method == "POST":
        ingredients = request.form.get("ingredients", "").strip()
        if ingredients:
            recipes, error = call_groq_for_recipes(ingredients)
        else:
            error = "Please enter at least one ingredient."

    return render_template(
        "index.html",
        recipes=recipes,
        error=error,
        ingredients=ingredients,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



