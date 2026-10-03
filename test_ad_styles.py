import random
styles = ["PREMIUM", "DYNAMIQUE", "ELEGANT"]
style = random.choice(styles)
print("STYLE CHOISI :", style)
import os
from datetime import datetime
from moviepy import ImageClip, TextClip, CompositeVideoClip, AudioFileClip, vfx

image = "/home/szouhari/video-ad-editor/assets/images/dar_ghizlane_logo.png"
audio_dir = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR/musique et sons"
audio_files = sorted([os.path.join(audio_dir, f) for f in os.listdir(audio_dir) if f.lower().endswith((".mp3", ".wav", ".m4a", ".aac", ".ogg"))])
output_dir = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR"
date = datetime.now().strftime("%Y-%m-%d")
number = 1
while os.path.exists(os.path.join(output_dir, f"video_{date}_{number:03d}.mp4")):
    number += 1
output = os.path.join(output_dir, f"video_{date}_{number:03d}.mp4")

logo = ImageClip(image).with_duration(6)
logo = logo.resized(lambda t: 0.65 + (0.04 if style == "PREMIUM" else 0.10 if style == "DYNAMIQUE" else 0.06) * t)
logo = logo.with_position(lambda t: ("center", 180 - (30 if style == "PREMIUM" else 80 if style == "DYNAMIQUE" else 45) * min(t / 1.5, 1)))
logo = logo.with_effects([vfx.CrossFadeIn(2.0 if style == "PREMIUM" else 0.7 if style == "DYNAMIQUE" else 1.5)])

text = TextClip(
    text="DAR GHIZLANE",
    font="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    font_size=70,
    color="white"
).with_duration(6)

text = text.with_position(lambda t: ("center", 500 - (40 if style == "PREMIUM" else 120 if style == "DYNAMIQUE" else 65) * min(t / 1.5, 1)))

selected_audio = random.choice(audio_files)
print("MUSIQUE CHOISIE :", os.path.basename(selected_audio))
audio_full = AudioFileClip(selected_audio); max_start = audio_full.duration - 6; start = random.uniform(0, max_start); print("DÉBUT AUDIO :", round(start, 2), "s"); audio = audio_full.subclipped(start, start + 6)
video = CompositeVideoClip(
    [logo, text],
    size=(1280, 720)
)

video = video.with_audio(audio)
video.write_videofile(
    output,
    fps=24,
    codec="libx264",
    audio=True
)

print("DAR GHIZLANE AD OK")
