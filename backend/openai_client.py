from openai import OpenAI
import os

# Load the API key from environment variable
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def suggest_recipes(ingredients: list[str] = None, cuisine: str = None) -> str:
    prompt = "Suggest a recipe"

    if ingredients:
        prompt += f" with the following ingredients: {', '.join(ingredients)}"
    if cuisine:
        prompt += f" that is a {cuisine} cuisine."

    prompt += "\n\nRecipe:"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that suggests recipes.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.7,
    )

    recipe = response.choices[0].message.content.strip()
    return recipe
