import speech_recognition as sr
import soundfile as sf
import os

def transcript():
    ##transform to wav
    os.system('ffmpeg -y -i audio.ogg out.wav')

    r = sr.Recognizer()

    harvard = sr.AudioFile('out.wav')
    with harvard as source:
        audio = r.record(source)
    out=r.recognize_google(audio)
    return out