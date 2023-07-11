import openai

openai.api_key = "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"
prompt = 'an astronaut longing in a tropical resort in space'
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="256x256",
)
print(response["data"][0]["url"])
