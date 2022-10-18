import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia


def assistant(audio):
    engine = pyttsx3.init()
    # getter: To get the current
    # engine property value
    voices = engine.getProperty('voices')
    # setter method
    # [0] for male voice
    # [1] for female voice
    engine.setProperty('voice', voices[1].id)
    # Method governing assistant's speech
    engine.say(audio)
    # Blocks/processes queued commands
    engine.runAndWait()


def greeting():

    # This is a simple greeting and
    # it informs the user that the
    # assistant has started
    assistant("Hello, I'm Friday , What you want me to do for you")

def audioinput():
    # this function is all about taking the audio input from the user
    aud = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening and processing')
        # The pause is optional here
        aud.pause_threshold = 0.7
        audio = aud.listen(source)
        # Using try (for valid commands) and exception for when the assistant
        # doesnt "catch" the command
        try:
            print("understanding")
            # en-eu is simply for the accent here english we can use 'en-GB' or 'en-au'
            # for UK and Australian accents
            phrase = aud.recognize_google(audio, language='en-us')
            print("you said: ", phrase)
        except Exception as exp:
            print(exp)
            print("Can you please repeat that")
            return "None"
    return phrase

def theDay():
    # This function is for the day
    day = datetime.datetime.today().weekday() + 1
    # assigning a number makes it a bit cleaner
    Day_dict = {
    1: 'Monday', 2: 'Tuesday',
    3: 'Wednesday', 4: 'Thursday',
    5: 'Friday', 6: 'Saturday',
    7: 'Sunday'
    }
    if day in Day_dict.keys():
        weekday = Day_dict[day]
        print(weekday)
    assistant("it's " + weekday)

def Goodword():
    print("You Good too ")
    
    assistant("Thank you so much ")
def theTime():
    # This function is for time
    time = str(datetime.datetime.now())
    # time needs to be sliced for
    # better audio comprehension
    print(time)
    hour = time[11:13]
    min = time[14:16]
    assistant("The time right now is" + hour + "Hours and" + min + "Minutes")

def core_code():

    # First, we will call greeting
    # to mark the starting
    greeting()

    while (True):
    # changing the query to lowercase
    # ensures it works most of the time
        phrase = audioinput().lower()

        if "what is your name" in phrase:
            assistant("I am Friday , Nice to meet you ")
            continue
        
        elif "what day is it" in phrase:
            theDay()
            continue

        elif "what time is it" in phrase:
            theTime()
            continue
        elif "you're so good" in phrase:
            Goodword()
            continue
        elif "open google" in phrase:
            assistant("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        elif "google search facebook" in phrase:
            assistant("Opening Google")
            phrase = phrase.replace("google search ","")
            webbrowser.open("https://www.google.com/search?q="+phrase)
        elif "wikipedia" in phrase:
            # to pull information from Wiki
            assistant("Checking the wikipedia ")
            phrase = phrase.replace("wikipedia", "computer network")
            # it will limit the summary to four lines
            result = wikipedia.summary(phrase, sentences=4)
            assistant("As per wikipedia")
            assistant(result)
            continue
        # trigger/condition to exit the program
        elif "bye" in phrase:
            assistant("Good bye. Have a Nice Day")
            exit()

core_code()

