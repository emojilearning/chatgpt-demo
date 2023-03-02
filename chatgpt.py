import openai
openai.organization = "org-QxuXR92JiMhuw3fMvrUG9DTj"
openai.api_key = "" # os.getenv("OPENAI_API_KEY")
openai.model = "gpt-3.5-turbo"
history = [{"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: {knowledge_cutoff} Current date: {current_date}"}]

while True:
    prompt = input("You: ")
    history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= history
    )
    r = response["choices"][0]["message"]['content']
    history.append({"role": "assistant", "content": r})
    print("AI:", r)
