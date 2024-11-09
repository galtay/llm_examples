# https://platform.openai.com/docs/guides/structured-outputs

import dotenv
from openai import OpenAI
from pydantic import BaseModel

env = dotenv.dotenv_values(".env")
client = OpenAI(api_key=env["OPENAI_API_KEY"])


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


chat_completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    response_format=CalendarEvent,
)
print(chat_completion)
