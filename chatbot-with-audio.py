import speech_recognition as sr  
import webbrowser as wb
import pyttsx3
import requests
import smtplib, ssl
import datetime
import socket 
import time
import random
import sys
import pyautogui
import wikipedia
import os
from cv2 import *

def speak(key):
    #  Text to speech conversion 
    engine = pyttsx3.init()
    engine.say(key)
    engine.runAndWait()

def wishMe():
    #  welcome wishes
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print('Good Morning')
        speak('Good Morning')
    elif hour == 12 and hour < 18:
        print('Good Afternoon')
        speak('Good Afternoon')
    else:
        print('Good Evening')
        speak('Good Evening')
    print('I am chatbot, Tell me how can I help you ?')
    speak('I am chatbot, Tell me how can I help you ?')


 
def listen():
    #  Listens and returns the text output
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        speak("I'm all ears, tell me...")
        audio = r.listen(source, phrase_time_limit=3)
    try:
        text = r.recognize_google(audio, language='en')
        text = text.lower()
        print("just to confirm, you said : {}".format(text))
    except:
        print("Unable to get your command")
        speak("Unable to get your command")
        speak("lets do one thing, just type  what you want instead")
        text = str(input("Type here: "))
    return text


 


def commands(text):
    if "hello" in text or "hi" in text:
        string1 = ("Hello,\nYou can ask questions.", "Hi There, You can ask questions.")
        out1 = random.choice(string1)
        print(out1)
        speak(out1)

     

    elif "how are you" in text or "what's up" in text:
        string2 = ("I am fine, Hope you are doing good too.", "I am good, Hope you are fine too.")
        out2 = random.choice(string2)
        print(out2)
        speak(out2)

    elif "who designed you" in text or "who is you master" in text:
        print("I got made by Anchal Singh")
        speak("I got made by Anchal Singh")

     

    elif "what is your name" in text or "what's your name" in text or "your name" in text:
        print("My name is ChatBot")
        speak("My name is ChatBot")

      

    elif "nothing" in text or "abort" in text or "stop working" in text:
        speak("Ok")
        sys.exit()

     

    elif 'thank you' in text or 'thankyou' in text:
        print("You're welcome ")
        speak("You're welcome ")

     

    elif 'what can you do' in text or 'what is your job' in text or 'how can you help me' in text:
        print("I'm here to make things easier for you, ")
        speak("I'm here to make things easier for you, ")
        print(
            "You can command me like -  'open gmail for me' , 'play music' , 'open c drive' , 'what is my location', 'play game' , 'open cmd' ")
        speak(
            "You can command me like -  'open gmail for me' , 'play music' , 'open c drive' , 'what is my location', 'play game' or 'open cmd' ")

     

    elif 'bye' in text or 'bye bye' in text or 'bye-bye' in text or 'good bye' in text:
        print("Hope I was able to help you today.")
        speak("Hope I was able to help you today.")
        print("Bye  !")
        speak("Bye  !")
        exit()

     

    elif 'gmail' in text:   
        wb.open('https://www.google.com/gmail/')

     

    elif 'netflix' in text:   
        wb.open('https://www.netflix.com/')

     

    elif 'facebook' in text:   
        wb.open('https://www.facebook.com/')

     

    elif 'open youtube' in text or 'youtube' in text or 'play video' in text:   
        wb.open('https://www.youtube.com/')

     

    elif 'google' in text or 'chrome' in text or 'google chrome' in text:
        wb.open('https://www.google.com/search?q=')

     

    elif "navigation" in text or "get directions" in text or 'get direction' in text or 'google maps' in text or 'google map' in text:
        print("Opening Google Navigation....")
        speak("Opening Google Navigation")
        wb.open("https://www.google.com/maps/dir/")

     

    elif 'time' in text:   
        hour = int(datetime.datetime.now().hour)
        minute = int(datetime.datetime.now().minute)
        print(" , The time is", hour, ':', minute, ':')
        speak(" , The time is", )
        speak(hour)
        speak(minute)

     

    elif 'c drive' in text or 'drive c' in text:
        print("Opening Local Drive C")
        speak("Opening Local Drive C")
        os.startfile("C:")

     

    elif 'd drive' in text or 'drive d' in text:
        print("Opening Local Drive D")
        speak("Opening Local Drive D")
        os.startfile("D:")

     

    elif 'f drive' in text or 'drive f' in text:
        print("Opening Local Drive F")
        speak("Opening Local Drive F")
        os.startfile("F:")

     

    elif 'g drive' in text or 'drive g' in text:
        print("Opening Local Drive G")
        speak("Opening Local Drive G")
        os.startfile("G:")

     

    elif 'system information' in text:
        hostename = socket.gethostname()
        ip = socket.gethostbyname(hostename)
        print("Hostname is : ", hostename)
        print("IP Address is : ", ip)
        speak(hostename)
        speak(ip)

     

    elif 'play music' in text or 'song' in text or 'music' in text:
         
        music_dir = 'Path'  
        songs = os.listdir(music_dir)
        s = random.choice(songs)
        os.startfile(os.path.join(music_dir, s))

      

    elif "control panel" in text:
        print("Opening Control Panel...")
        speak("Opening Control Panel")
        os.startfile(
            "C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel")


    elif 'cmd' in text in text or 'command prompt' in text or 'terminal' in text:
        os.system("start cmd")

    
    elif "go to run" in text or "open run" in text or 'run panel' in text:
        print("Opening Run Panel...")
        speak("Opening Run Panel")
        os.startfile("C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run")

    elif 'screenshot' in text:
        print('Capturing Screenshot, please wait !')
        speak('Capturing Screenshot, please wait !')
        pic = pyautogui.screenshot()
        print("Screenshot Captured.")
        speak("Screenshot Captured")
        print("Enter the filename to save the screenshot file : ")
        speak("Enter the filename to save the screenshot file : ")
        filename = input()
        output = filename + ".png"
        pic.save(output)
        print("Your screenshot has been saved, ")
        speak("Your screenshot has been saved, ")
        os.startfile("C:\\Users\\{username}\\"+output)

    elif 'camera' in text or 'webcam' in text:
        print("Press 'q' to close the camera")
        speak("Press 'q' to close the camera")
        cap = cv2.VideoCapture(0)
        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            # Our operations on the frame come here
            gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY)
            # Display the resulting frame
            cv2.imshow('frame', frame)
            cv2.imshow('gray', gray)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
           # When everything done, release the capture
            cap.release()
            cv2.destroyAllWindows()

    elif 'email' in text:
        print("Enter Reciever's email : ")
        speak("Enter Reciever's email")
        receiver_email = input()
        print("Enter message: ")
        speak("Enter message.")
        message = input()
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                server.login('mypythonassistant@gmail.com', 'zzzyz121005')
                server.sendmail('mypythonassistant@gmail.com', receiver_email, message)
                server.quit()
                print('Email sent !!')
                speak("Email sent !")
        except:
            wb.open('www.gmail.com')

    elif "start stopwatch" in text or 'stopwatch' in text:
        speak("Press enter to start the timer.")
        startTimer = input("Press enter to start the timer.")
        speak("The timer has started.")
        start = time.time()
        speak("Press enter to stop the timer.")
        endTimer = input("Press enter to stop the timer.")
        end = time.time()
        speak("The timer has stopped.")
        elapsed = end - start
        elapsed = str(elapsed)
        print("The time elapsed is " + elapsed + " seconds.")
        speak("The time elapsed is " + elapsed + " seconds.")

     

    elif "network ip" in text or 'ip address' in text:
        speak("Ok . Fetching your IP address")
        print("Ok . Fetching your IP address....")
        ip_request = requests.get("https://get.geojs.io/v1/ip.json")
        my_ip = ip_request.json()["ip"]
        print("Your Network's IP Address is: ", my_ip)
        speak("Your Network's IP Address is:")
        speak(my_ip)

     
    elif 'date' in text:
         day = int(datetime.datetime.now().day)
         date = (datetime.date())
         print(" , It's ",date,)

     

    elif 'location' in text or 'where am i' in text: 
        a = requests.get('https://ipinfo.io/')
        data = a.json()
        city = data['city']
        location = data['loc'].split(',')
        latitude = location[0]
        longitude = location[1]
        print(city)
        speak(city)
        print('Latitude : ', latitude)
        print('Longitude : ', longitude)

     

    elif 'temperature' in text or 'weather' in text:
        api = "http://api.openweathermap.org/data/2.5/weather?appid=a5cdd5b81160a2eb8247658da386a49c&q="
        print("Enter city name : ")
        speak("Enter city name")
        city = input()
        url = api + city
        data = requests.get(url).json()
        weather = data["weather"][0]["main"]
        temp_k = int(data["main"]["temp"])
        temp = (temp_k - 273)
        humidity = int(data["main"]["humidity"])
        print("Temperature: ", temp, "'C")
        speak("Temperature is")
        speak(temp)
        speak("degree celcius")
        print("Current weather: ", weather)
        speak("Current Weather : ")
        speak(weather)
        print("Humidity: ", humidity, "%")
        speak("Humidity is: ")
        speak(humidity)
        speak("percents")

    elif 'wikipedia' in text or 'search online' in text or 'search for' in text:  
        print("Do you want a wikipedia search ?    YES/NO")
        speak("Do you want a wikipedia search ?")
        res2 = listen()
        if 'yes' in res2:
            print('What do you want to search ?')
            speak('What do you want to search ?')
            content = listen()
            info = wikipedia.summary(content, sentences=2)  
            print("According to Wikipedia...\n", info)
            speak('According to Wikipedia ...')
            speak(info)
        elif 'no' in res2:
            print("Okay  !")
            speak('Okay  !')
        else:
            print("Invalid Response")
            speak("Invalid Response")

    else:
        command = text
        print("Searching Wikipedia.... ")
        speak("Searching Wikipedia.... ")
        try:
            info2 = wikipedia.summary(command, sentences=2)  
            print("According to Wikipedia -\n", info2)
            speak('According to Wikipedia : ')
            speak(info2)
        except:
            wb.open('www.google.com')

if __name__ == "__main__":
    date = datetime.datetime.now().date()
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    if int(hour) >= 0 and int(hour) < 12:
        a = 'am'
    else:
        a = 'pm'
    print(date, hour + ':' + minute, a)
    wishMe()
    while True: 
        command = listen()
        commands(command)

 
