import base64
import dotenv
from openai import OpenAI

env = dotenv.dotenv_values(".env")
client = OpenAI(api_key=env["OPENAI_API_KEY"])


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


image_path = "data/wmap_2012_320x160px.png"
base64_image = encode_image(image_path)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "describe this image"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{base64_image}"},
                },
            ],
        }
    ],
    model="gpt-4o-mini",
)
print(chat_completion)
