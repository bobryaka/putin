from pydub import AudioSegment


def combine(text):
    audio = AudioSegment.from_file(f"cuted_audio/start.wav")
    gap = AudioSegment.from_file(f"cuted_audio/gap.wav")
    for word in text.split():
        next = AudioSegment.from_file(f"cuted_audio/{word}.wav")
        audio = audio.append(next)
        audio = audio.append(gap)
    return audio

popoo = combine('ты пидор')
popoo.export(f'done_audio/3.wav', format="wav")

