from moviepy import AudioFileClip, CompositeAudioClip, concatenate_audioclips

def load_audio(path):
    return AudioFileClip(path)

def add_audio(clip, audio):
    return clip.with_audio(audio)

def mix_audio(*tracks):
    return CompositeAudioClip(list(tracks))


def fit_audio_to_duration(audio, duration):
    if duration <= 0:
        return audio

    if audio.duration >= duration:
        return audio.subclipped(0, duration)

    count = int(duration / audio.duration) + 1
    looped = concatenate_audioclips([audio] * count)
    return looped.subclipped(0, duration)
