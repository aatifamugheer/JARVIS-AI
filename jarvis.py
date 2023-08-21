import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak("Good Morning!")

   elif hour>=12 and hour<18:
      speak("Good Afternoon!")

   else:
      speak("Good Evening!")

   speak("I am [JARVIS AI] Maam. Please tell me how may I help you")

def takeCommand():
    # It takes microsoft input from the user and returns string output  

    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening.......")
       r.pause_threshold = 1
    #    r.energy_threshold = 300
      
       audio = r.listen(source)

    try:
       print("Recognizing.....")
       query = r.recognize_google(audio, language='en-in')
       print("User said:{query}\n")

    except Exception as e:
    #    print(e)
         print("Say that again please....")
         return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("aatifamugheer34@gmail.com", "Aatifa123@")
    server.sendmail("aatifamugheer34@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
      query = takeCommand().lower()
   
      if 'wikipedia' in query:
         speak("Searching Wikipedia....")
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak("According to Wikipedia")
         print(results)
         speak(results)
      elif 'open youtube' in query:
         webbrowser.open("youtube.com")
      elif 'open google' in query:
         webbrowser.open("google.com")

      elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")

      elif 'play music' in query:
         music_dir = "C:\\song"
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[4]))

      elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Maam, The time is {strTime}")
      elif 'open code' in query:
         codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)
      # small_talk_topics = ["weather", "sports", "movies", "food"]


      elif "weather" in query:
        speak("The weather is great today!")
      elif "sports" in query:
        speak("I'm not much of a sports fan, but what's your favorite sport?")
      elif "movies" in query:
        speak("I love movies! What's your favorite genre?")
      elif "food" in query:
        speak("I enjoy all kinds of food. What's your favorite dish?")
      elif 'tell me a joke' in query:
        jokes = ["Why don't scientists trust atoms? Because they make up everything!", "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"]
        speak(jokes)

      elif 'tell me a fun fact' in query:
        facts = ["Honey never spoils. You could feasibly eat 3,000-year-old honey!", "Polar bears have black skin."]
        speak(facts)
      elif 'how are you' in query:
        speak("I'm an AI, so I don't have feelings, but I'm here to assist you!")
      elif 'quote' in query or 'inspiration' in query:
        quotes = ["The only way to do great work is to love what you do. - Steve Jobs", 
                  "In the middle of difficulty lies opportunity. - Albert Einstein"]
        speak(random.choice(quotes))

      elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a great day!")
            break



      #   elif 'email to Aatifa' in query:
      #    try:
      #       speak("What should I say?")
      #       content = takeCommand()
      #       to = "aatifayourEmail@gmail.com"
      #       sendEmail(to, content)
      #       speak("Email has been sent!")
      #    except Exception as e:
      #       print(e)
      #       speak("Sorry Aatifa maam , I am not able to send this email")



