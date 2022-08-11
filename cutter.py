import json
from pydub import AudioSegment

data = list()


def cut_audio(start, end, word, path):
    t1 = start * 1000
    t2 = end * 1000 + 50
    new_audio = AudioSegment.from_wav(path)
    new_audio = new_audio[t1:t2]
    new_audio.export(f'cuted_audio240222/{word}.wav', format="wav")


with open('putin240222.json', 'r') as file:
    try:
        temp = json.load(file)
        for i in temp:
            for k in i['result']:
                data.append(k)
    except KeyError:
        pass


for i in data:
    cut_audio(i['start'], i['end'], i['word'], 'resources/240222.wav')
