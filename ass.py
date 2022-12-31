import openai
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import datetime

openai.api_key = "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"


Now = datetime.datetime.now()
Time = Now.strftime("%H_%M_%S")




v_engine = pyttsx3.init()
v_engine.setProperty('volume', 1.0)
v_engine.setProperty('rate', 120)

# Set the voice to use
voices = v_engine.getProperty('voices')
v_engine.setProperty('voice', voices[1].id)
v_engine.say("Hello, I am davinci")







def chatbot(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text #type: ignore
    return message




def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = f"{Time}"
    tts.save(f'')
    
  

r = sr.Recognizer()




while True:
    with sr.Microphone() as source:
        print("Listening....\n")
        audio = r.listen(source)
    try:
        user_input = r.recognize_google(audio)
        print("You said:\n",  user_input)
        if user_input == "exit":
            break
        response = chatbot(user_input)
        print("Chatbot:\n", response)
        speak(response)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error requesting results from Google Speech Recognition service; {0}".format(e))