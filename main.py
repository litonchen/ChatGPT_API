while True:
    msg=input()
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=msg,
        max_tokens=512,
        temperature=0.9,
    )
    completed_text = response["choices"][0]["text"]
    print(completed_text)
