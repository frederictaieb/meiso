import speech_recognition as sr
import pygame

r = sr.Recognizer()

file = "ding.mp3"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load()
pygame.mixer.music.play()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    word = r.recognize_google(audio, language="fr-FR")
    if "bof" in word:
        print("waiting for instructions")

        p.loadfile('')
        p.time_pos = 40
        p.length