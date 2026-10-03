from moviepy import ImageClip, TextClip, CompositeVideoClip

def add_image(clip, image, position=("center", "center"), duration=None):
    overlay = ImageClip(image)
    if duration is not None:
        overlay = overlay.with_duration(duration)
    else:
        overlay = overlay.with_duration(clip.duration)
    return CompositeVideoClip([clip, overlay.with_position(position)])

def add_text(clip, text, font_size=60, color="white", position=("center", "center"), duration=None):
    overlay = TextClip(text=text, font_size=font_size, color=color)
    if duration is not None:
        overlay = overlay.with_duration(duration)
    else:
        overlay = overlay.with_duration(clip.duration)
    return CompositeVideoClip([clip, overlay.with_position(position)])
