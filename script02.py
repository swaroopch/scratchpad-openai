import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
print(response)


# https://platform.openai.com/docs/api-reference/completions/create#completions/create-temperature
# "Higher values like 0.8 will make the output more random, while 
# lower values like 0.2 will make it more focused and deterministic."
