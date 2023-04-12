"""
Using a prompt template.

https://platform.openai.com/docs/quickstart/understand-the-code
"""

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(animal.capitalize())

animal = input("Which animal? ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=generate_prompt(animal),
  temperature=0.6
)
print(response)
