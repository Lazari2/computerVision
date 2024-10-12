import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import sys

r = sr.Recognizer()
wikipedia.set_lang('pt')

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('ouvindo')
            speak('já ta podendo falar tá?!')
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin, language = 'pt-br')
            my_text = my_text.lower()
            print(my_text)

            if 'toca' in my_text:
                my_text = my_text.replace('toca', '')
                speak('claro meu rei maravilhoso te amo, tocando...' + my_text)
                pywhatkit.playonyt(my_text)
            
            elif 'que dia é hoje' in my_text:
                today = datetime.date.today().strftime('%d/%m/%Y')
                speak(today)

            elif 'que hora' in my_text:
                timenow = datetime.datetime.now().strftime('%H:%M')
                speak(timenow)

            elif 'fale sobre' in my_text:
                person = my_text.replace('me fale sobre', '')
                info = wikipedia.summary(person, 1)
                speak(info)
            
            elif 'tchau' in my_text:
                speak("falou brother, tamo junto")
                sys.exit()

            else:
                speak("Não entendi o que você quer não, fala direito")

    except sr.UnknownValueError as e:
        print(f"erro na solicitação {e}")
        speak('vai ti a merda, meti meu pé')
        sys.exit()

speak('bem vindo a lázarequíssa, a alexa do Lázari, o mais lindo, no que posso ajudar? Fale só quando eu falar que pode falar ok?')
while True:
    commands()