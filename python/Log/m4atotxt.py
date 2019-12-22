#conda install -c conda-forge pydub
#brew install ffmpeg
#pip3 install SpeechRecognition

import os
import argparse
import speech_recognition as sr

from pydub import AudioSegment


folders = {
    "m4a": "m4a_files//", 
    "wav": "wav_files//", 
    "txt": "txt_files//"
}

extensions = {
    "m4a": ".m4a", 
    "wav": ".wav", 
    "txt": ".txt"
}

def create_filename(name, type):
    return folders[type] + name + extensions[type]


def convert_m4a_to_wav(name):

    m4a_filename = create_filename(name, "m4a")
    wav_filename = create_filename(name, "wav")

    try:
        print("Converting {} -> {} ...".format(m4a_filename, wav_filename))
        track = AudioSegment.from_file(m4a_filename,"m4a")
        track.export(wav_filename, format="wav")
        print ("M4A to WAV conversion done successfully.")
    except:
        print("Error Converting " + str(m4a_filename))

def convert_wav_to_txt(name):

    wav_filename = create_filename(name, "wav")
    txt_filename = create_filename(name, "txt")
    
    r = sr.Recognizer()
    harvard = sr.AudioFile(wav_filename)
    with harvard as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        print("Converting {} -> {} ...".format(wav_filename, txt_filename))
        transcript = r.recognize_google(audio)
        transcript_file  = open(txt_filename, 'w+')
        transcript_file.write(transcript+"\n")
        transcript_file.close()
        print ("WAV to TXT conversion done successfully. Please consult: {}.".format(txt_filename))
        print("Transcript : {}.".format(transcript))

os.system('clear')
convert_m4a_to_wav("ta")
convert_wav_to_txt("harvard")

