from moviepy import vfx

def zoom(clip, start=0.75, speed=0.10):
    return clip.resized(lambda t: start + speed * t)


def ken_burns(clip, start=1.0, end=1.08):
    duration = clip.duration
    if duration <= 0:
        return clip

    def scale(t):
        progress = min(max(t / duration, 0), 1)
        return start + (end - start) * progress

    return clip.resized(scale)

def fade_in(clip, duration=0.5):
    return clip.with_effects([vfx.FadeIn(duration)])

def fade_out(clip, duration=0.5):
    return clip.with_effects([vfx.FadeOut(duration)])
