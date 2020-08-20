import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib

print("Initializing virtual")
a="RITIKA"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    
    engine.say(text)
    engine.runAndWait()
#speak("this is working")

def greetme():
    hour=int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        speak("GOOD MORNING" + a)
    elif hour>=12 and hour<18:
        speak("GOOD NIGHT" + a)
    else:
        speak("GOOD EVENING" + a)

    speak("I am virtual!! how may i help you?")

def mycommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
          print("Listening...")
          audio = r.listen(source)
         
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    
    except Exception as e:
          print(e)
          speak('Sorry ! I didn\'t get that! Try typing the command!')
          #print('Sorry ! I didn\'t get that! Try typing the command!')
          return "None"
    return query

  
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls()  
    server.login('your email id', 'your email passowrd') 
    server.sendmail('your email id', to, content) 
    server.close() 


greetme()    
query=mycommand()
def main():

    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query=query.replace("wikipedia" , "")
        results= wikipedia.summary(query , sentences=3)
        speak(results)
        
    elif 'open youtube' in query.lower():
    # webbrowser.open("youtube.com")
        url='youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
    
        url='google.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'play music' in query.lower(): 
        speak("Lets play music") 
        music_dir = "C:\\Users\\Ritika\\Pictures\\musica"
        songs = os.listdir(music_dir) 
        print(songs)     
        random = os.startfile(os.path.join(music_dir, songs[0])) 
    





    elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 

    elif "who am i?" in query: 
            speak("If you talk then definately you are human.") 

    elif "who created you" in query:  
         speak("I have been created by Ritika.") 
    
    elif 'the time' in query.lower(): 
        strTime = datetime.datetime.now().strftime("% H:% M:% S")     
        speak(f"{a} the time is {strTime}") 
    elif 'open code' in query.lower():
        codepath="C:\\Users\\Ritika\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code.exe"
        os.startfile(codepath)
    elif "stop listening" in query: 
          speak("for how much time you want to stop jarvis from listening commands") 
          a = int(takeCommand()) 
          time.sleep(a) 
          print(a) 
              
    elif 'empty recycle bin' in query: 
          winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
          speak("Recycle Bin Recycled") 

    elif 'email to Nishtha' in query: 
        try: 
            speak("What should I say?") 
            content = mycommand() 
            to = "Receiver email address"    
            sendEmail(to, content) 
            speak("Email has been sent !") 
        except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
    elif "who are you" in query: 
            speak("I am your virtual assistant created by Ritika") 
  

    elif 'exit' in query: 
        speak("Thanks for giving me your time") 
        exit() 
main()