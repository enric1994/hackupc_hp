import speech_recognition as sr
import soundfile as sf


r = sr.Recognizer()

harvard = sr.AudioFile('out.wav')
with harvard as source:
    audio = r.record(source)
out=r.recognize_google(audio)
print(out)