import speech_recognition as sr
import os

print("Meiso Transcript")

fileDir = os.path.dirname((os.path.abspath(__file__)))

print ("- Which File?")
filename = input("> ")

filename = os.path.join(fileDir, 'data/' + filename)

print ("\n- Which Language?")
print ("0 : FR")
print ("1 : EN")
lang = input("> ")

if lang == "1":
    lang = 'en-US'
else:
    lang = 'fr-FR'


r = sr.Recognizer()
af = sr.AudioFile(filename + ".wav")

with af as source:
    audio = r.record(source)
    transcript = r.recognize_google(audio, language=lang)
    print("\n- " + transcript)

    transcript_file  = open(filename + ".txt", 'w')
    transcript_file.write(transcript)
    transcript_file.close()