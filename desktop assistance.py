import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good   morning")
    elif hour>=12 and hour<18:
        speak("good afternoon ")
    else:
        speak("good evening")
    speak("i am jarvis sir . please tell me how can i help u")
def takecommand():
      
    #it take microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as  source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"usersaid: {query}\n")
    except Exception as e:
        #print(e)
        print("Say again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia... ')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            starttime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {starttime}")

        '''elif 'play music' in query:
            music_dir='D:\\Non Critical\\songs\\Favourite Songs2'
            songs=os.listdir(music_dir)
            print(songs)'''
        






    