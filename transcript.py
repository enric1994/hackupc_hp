import speech_recognition as sr
import soundfile as sf

data, samplerate = sf.read('audio.ogg')
sf.write('audio.wav', data, samplerate)

r = sr.Recognizer()

harvard = sr.AudioFile('audio.wav')
with harvard as source:
    audio = r.record(source)
out=r.recognize_google(audio)
print(out)