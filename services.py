#!/usr/bin/env python3
import json
from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave

SetLogLevel(0)

wf = wave.open('resources/240222.wav', "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    exit(1)

model = Model("vosk-model-ru-0.22")


rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
rec.SetPartialWords(True)

temp = list()
with open('putin240222.json', 'w', encoding='utf-8') as file:
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            rec_text = json.loads(rec.Result())
            temp.append(rec_text)
        else:
            pass

    temp.append(json.loads(rec.FinalResult()))
    json.dump(temp, file)


print(rec.FinalResult())
