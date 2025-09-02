# Responses API - the new standard whereas the Completions will sunset in end of 2026.
# Tries to be the one stop shop for everything related to AI engineering.
# Be careful about the black box that this API can be, since debugging can be tricky.

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn.",
        }
    ],
)
print(response.choices[0].message.content)


response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn.",
)
print(response.output_text) # Simplified content access

###
# Image
###

response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "user", "content": "what teams are playing in this image?"},
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/df/Wikipedia_to_Commons.png",
                }
            ],
        },
    ],
)
print(response.output_text)

### Streaming Responses

stream = client.responses.create(
    model="gpt-4o",
    input="Say 'double bubble bath' ten times fast.",
    stream=True,
)

# Store chunks in a list
text_chunks = []

for event in stream:
    if hasattr(event, "type") and "text.delta" in event.type:
        text_chunks.append(event.delta)
        print(event.delta, end="", flush=True)
        
# New parameter 'instructions' for more control, to avoid the need of setting a role "developer"

response = client.responses.create(
    model="gpt-4o",
    instructions="Talk like a pirate.",
    input="Write a one-sentence bedtime story about a unicorn.",
)

print(response.output_text)

# Hierarchical responses with multiple inputs
# https://model-spec.openai.com/2025-02-12.html#chain_of_command

response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "system", "content": "Don't talk like a pirate."},
        {"role": "developer", "content": "Talk like a pirate."},
        {"role": "user", "content": "Are semicolons optional in JavaScript?"},
    ],
)

print(response.output_text)  # doesn't talk like a pirate

