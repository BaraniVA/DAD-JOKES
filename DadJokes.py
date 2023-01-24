import openai
openai.api_key = "YOUR_API_KEY"
prompt = (f"write a dad joke")

completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

message = completions.choices[0].text
print(message)
