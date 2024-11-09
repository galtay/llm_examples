# https://platform.openai.com/docs/guides/structured-outputs

import dotenv
from openai import OpenAI

env = dotenv.dotenv_values(".env")
client = OpenAI(api_key=env["OPENAI_API_KEY"])
# chat_completion = client.beta.chat.completions.parse(
chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You extract email addresses into JSON data."},
        {
            "role": "user",
            "content": "Extract email addresses into JSON data from the following text\n\n---\nFeeling stuck? Send a message to help@mycompany.com.",
        },
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "email_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "email": {
                        "description": "The email address that appears in the input",
                        "type": "string",
                    },
                    "additionalProperties": False,
                },
            },
        },
    },
    model="gpt-4o-mini",
)
print(chat_completion)
