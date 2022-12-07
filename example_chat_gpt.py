import os
import openai

openai.api_key = "sk-xxxxxxxxx"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Convert this text to a programmatic command: i want an algorithm to convert audio to text in python.",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.2,
  presence_penalty=0
)

print('Response:', response.get('choices')[0].get('text'))