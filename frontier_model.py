import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def chat_with_gemini(messages):

    conversation = ""

    for msg in messages:

        if msg["role"] == "user":
            conversation += f"User: {msg['content']}\n"

        else:
            conversation += f"Assistant: {msg['content']}\n"

    response = model.generate_content(conversation)

    return response.text