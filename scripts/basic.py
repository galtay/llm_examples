import dotenv
from openai import OpenAI

env = dotenv.dotenv_values(".env")
client = OpenAI(api_key=env["OPENAI_API_KEY"])
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o-mini",
)
print(chat_completion)
