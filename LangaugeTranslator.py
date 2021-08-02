import speech_recognition as sr
from translate import Translator
import pyttsx3
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("[*] Speak English ...")
        audio = r.listen(source)
        print("[*] Reconizing Now ... ")
        try:
            dest = r.recognize_google(audio)
            print("[*] You have said : " + dest)
            translator= Translator(to_lang="spanish")
            translation = translator.translate(dest)
            print("[*] Translation : ", translation)
            speak(translation)
        except Exception as e:
            print("Error : " + str(e))
def main1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("[*] Speak Spanish .....")
        audio1 = r.listen(source)
        print("[*] Reconizing Now ... ")
        try:
            dest1 = r.recognize_google(audio1)
            print("[*] You have said : " + dest1)
            translator1= Translator(from_lang="spanish",to_lang="EN")
            translation1 = translator1.translate(dest1)
            print("[*] Translation : ", translation1)
            speak(translation1)
        except Exception as e:
            print("Error : " + str(e))            
if __name__ == "__main__":
    print("[*] English To Spanish Converter Will Be Starting In 5 Seconds")
    time.sleep(5)
    main()
    print("[*] Spanish To English Converter Will Be Starting In 5 Seconds")
    time.sleep(5)
    main1()
