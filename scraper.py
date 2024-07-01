import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("GPT_KEY"))
from reader import read as read
# Load your API key from an environment variable or secret management service

with open ("prompt.txt", "r") as myfile:
    prompt=myfile.read().replace('\n', '')

chat_completion = client.chat.completions.create(model="gpt-4",
                                               messages=[{"role": "user", "content": prompt}])
with open("output.txt", "a+") as text_file:
    print(chat_completion.choices[0].message.content, file=text_file)
    print("\n---\n---\n---\n---\n", file=text_file)

read("output.txt")
