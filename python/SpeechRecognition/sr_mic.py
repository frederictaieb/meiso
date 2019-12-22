import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything : ")
    #r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        txt = r.recognize_google(audio, language='fr-FR')
        if any(txt == "méso", txt == "meyson", txt =="maison"): 
            print('you said : {}'.format(txt))
            print ("Hello Alex!")
        
    except:
        print("Sorry could not recognize your voice")