import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour  = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("GOOD MORNING!")
    elif hour >= 12 and hour < 18:
        speak("GOOD AFTERNOON!")
    else:
        speak("GOOD EVENING!")
    speak("myself jarvis")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio  = r.listen(source)
    
    try:
        print("RECOGNIZING...")
        query = r.recognize_google(audio, language = 'en-IN')
        print(f"User said: {query}\n")

    except Exception as exception:
        print(exception)
        print("SAY THAT AGAIN...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("devkp786@gmail.com","kris@2002")
    server.sendmail("devkp786@gmail.com", to , content)
    server.close()

if __name__ == "__main__":
    speak("HELLO SIR, MYSELF JARVIS")
    #greeting()
    while True:
        query = takecommand().lower()
    # logic for executing tasks
        
        if 'wikipedia' in query:
            speak("seaching wikipedia...")
            query = query.replace("wikipedia",'')
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'date' in query:
            date = datetime.date.today()
            speak(f'sir, todays date is {date}')

        elif 'quit' in query:
            speak('yes sir')
            break

        elif 'email to harry' in query:
            try:
                speak("WHAT SHOULD I SAY?")
                content = takecommand()
                to = "devkp786@gmail.com"
                sendEmail(to, content)
                speak('EMAIL SENT')
            except:
                speak('email not sent due to some reason')
'''
        this jump statement is used to play song from the songs directory. it uses os module to play the song files

        elif "play music" in query:
            music_dir = 'D:\\Non Critical\\songs\\Favourite Songs2' # address of songs directory
            songs = os.listdir(music_dir) # to list all the songs
            print(songs) # to print all the songs in the comsole
            os.startfile(os.path.join(music_dir, songs[0])) # to play the first song labelled with index 0
        '''


