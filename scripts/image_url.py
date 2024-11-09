import dotenv
from openai import OpenAI

env = dotenv.dotenv_values(".env")
client = OpenAI(api_key=env["OPENAI_API_KEY"])

# 320 x 160 px
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/WMAP_2012.png/320px-WMAP_2012.png"
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "describe this image"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"{img_url}"},
                },
            ],
        }
    ],
    model="gpt-4o-mini",
)
print(chat_completion)
