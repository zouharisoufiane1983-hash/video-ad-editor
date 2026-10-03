import random
styles = ["PREMIUM", "DYNAMIQUE", "ELEGANT"]
style = random.choice(styles)
print("STYLE CHOISI :", style)
import os
from datetime import datetime
from moviepy import ImageClip, TextClip, CompositeVideoClip, AudioFileClip, CompositeAudioClip, vfx

image = "/home/szouhari/video-ad-editor/assets/images/dar_ghizlane_logo.png"
audio_dir = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR/musique et sons/MUSIQUES"
audio_files = sorted([os.path.join(root, f) for root, _, files in os.walk(audio_dir) for f in files if f.lower().endswith((".mp3", ".wav", ".m4a", ".aac", ".ogg"))])
voice_audio_path = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR/musique et sons/VOIX/voice.mp3"
output_dir = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR"
date = datetime.now().strftime("%Y-%m-%d")
number = 1
while os.path.exists(os.path.join(output_dir, f"video_{date}_{number:03d}.mp4")):
    number += 1
output = os.path.join(output_dir, f"video_{date}_{number:03d}.mp4")

logo = ImageClip(image).with_duration(6)
logo = logo.resized(lambda t: 0.65 + (0.025 if style == "PREMIUM" else 0.10 if style == "DYNAMIQUE" else 0.06) * t)
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
print("MUSIQUE PRINCIPALE :", os.path.basename(selected_audio))

other_audio = [f for f in audio_files if f != selected_audio]

random.shuffle(other_audio)
intro_audio_path = other_audio[0]
transition_audio_path = other_audio[1]
final_audio_path = other_audio[2]

audio_full = AudioFileClip(selected_audio)
voice_full = AudioFileClip(voice_audio_path)
max_start = max(0, audio_full.duration - 6)
start = random.uniform(0, max_start)
print("DÉBUT MUSIQUE :", round(start, 2), "s")
audio = audio_full.subclipped(start, min(start + 6, audio_full.duration)).with_volume_scaled(0.70)
voice_audio = voice_full.subclipped(0, min(6, voice_full.duration)).with_volume_scaled(1.0).with_start(0)

intro_full = AudioFileClip(intro_audio_path)
intro_audio = (
    intro_full
    .subclipped(0, min(1.5, intro_full.duration))
    .with_volume_scaled(0.35)
    .with_start(0)
)

transition_full = AudioFileClip(transition_audio_path)
transition_audio = (
    transition_full
    .subclipped(0, min(1.0, transition_full.duration))
    .with_volume_scaled(0.25)
    .with_start(3)
)

final_full = AudioFileClip(final_audio_path)
final_audio = (
    final_full
    .subclipped(0, min(1.5, final_full.duration))
    .with_volume_scaled(0.30)
    .with_start(4.5)
)

print("SON INTRO :", os.path.basename(intro_audio_path))
print("SON TRANSITION :", os.path.basename(transition_audio_path))
print("SON FINAL :", os.path.basename(final_audio_path))
mixed_audio = CompositeAudioClip([
    audio,
    voice_audio,
    intro_audio,
    transition_audio,
    final_audio
])
video = CompositeVideoClip(
    [logo, text],
    size=(1280, 720)
)

video = video.with_audio(mixed_audio)
video.write_videofile(
    output,
    fps=24,
    codec="libx264",
    audio=True
)

video.close()
mixed_audio.close()
audio_full.close()
intro_full.close()
transition_full.close()
final_full.close()

print("DAR GHIZLANE AD OK")
