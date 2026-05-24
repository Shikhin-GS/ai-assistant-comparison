from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct"
)

def chat_with_oss(messages):

    conversation = ""

    for msg in messages:

        if msg["role"] == "user":
            conversation += f"User: {msg['content']}\n"

        else:
            conversation += f"Assistant: {msg['content']}\n"

    prompt = f"""
System:
You are a professional AI assistant.

Rules:
- Answer accurately
- Never invent information
- If unknown, say "I don't know"
- Keep answers short
- Use maximum 1 sentence
- Never assume personal details
- Do not continue conversations unnecessarily

Conversation:
{conversation}

Assistant:
"""

    response = pipe(
        prompt,
        max_new_tokens=20,
        temperature=0.1,
        do_sample=True,
        repetition_penalty=1.2,
   

    )

    generated_text = response[0]["generated_text"]

    assistant_reply = generated_text.split("Assistant:")[-1].strip()

    assistant_reply = assistant_reply.split("User:")[0].strip()

    assistant_reply = assistant_reply.replace("#", "")

    assistant_reply = assistant_reply.replace("✨", "")

    assistant_reply = assistant_reply.replace("😊", "")

    assistant_reply = assistant_reply.replace("💖", "")

    return assistant_reply