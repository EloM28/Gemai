def main():
    try:
        from .local_settings import API_KEY
    except ImportError:
        ...

    import google.generativeai as genai
    
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel("gemini-2.0-flash")
    chat = model.start_chat()

    print("Chat with Gemai! Type 'exit' to quit")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chat.send_message(user_input)
        print("Gemai: ", response.text)

if __name__ == "__main__":
    main()
