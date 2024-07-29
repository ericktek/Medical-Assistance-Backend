import google.generativeai as genai

while True:
    input_message = input("what do you want help \n")

    genai.configure(api_key='AIzaSyCzvsGqemdf25EVXvWKy4qN18arGMGn6Y0')
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_message)

    print("\n")
    print(response.text)
    
    if input_message == "bye" or input_message == "Bye" or input_message == "exit":
        break
