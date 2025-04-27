import google.generativeai as genai
#go to google ai dev for your api key and paste
API_KEY = "YOUR API KEY "

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat With AMIN!")

while True:
    user_input = input("YOU: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("AMIN:", response.text)
