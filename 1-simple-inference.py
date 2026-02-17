import openai
#here openai talk with local server not openai , so we need to set the base_url and api_key
client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded"
)

response = client.chat.completions.create(
    model="phi:latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is ollama?"}
    ],temperature=0.3)
print(response.choices[0].message.content)