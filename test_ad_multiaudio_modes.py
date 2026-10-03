import random
styles = ["PREMIUM", "DYNAMIQUE", "ELEGANT"]
style = None
print("")
print("STYLE VIDÉO")
print("1 = PREMIUM")
print("2 = DYNAMIQUE")
print("3 = ELEGANT")
style_choice = input("Choisissez le style (1-3) : ").strip()
style = {"1": "PREMIUM", "2": "DYNAMIQUE", "3": "ELEGANT"}.get(style_choice, "ELEGANT")
print("STYLE CHOISI :", style)
import os
from datetime import datetime
from moviepy import ImageClip, TextClip, CompositeVideoClip, AudioFileClip, CompositeAudioClip, vfx

image = "/home/szouhari/video-ad-editor/assets/images/dar_ghizlane_logo.png"
audio_dir = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR/musique et sons/MUSIQUES"
music_dir = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR/musique et sons/MUSIQUES"
voice_dir = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR/musique et sons/VOIX"
effects_dir = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR/musique et sons/EFFETS"
audio_files = sorted([os.path.join(root, f) for root, _, files in os.walk(audio_dir) for f in files if f.lower().endswith((".mp3", ".wav", ".m4a", ".aac", ".ogg"))])
music_files = sorted([os.path.join(root, f) for root, _, files in os.walk(music_dir) for f in files if f.lower().endswith((".mp3", ".wav", ".m4a", ".aac", ".ogg"))])
voice_files = sorted([os.path.join(root, f) for root, _, files in os.walk(voice_dir) for f in files if f.lower().endswith((".mp3", ".wav", ".m4a", ".aac", ".ogg"))])
effects_files = sorted([os.path.join(root, f) for root, _, files in os.walk(effects_dir) for f in files if f.lower().endswith((".mp3", ".wav", ".m4a", ".aac", ".ogg"))])
output_dir = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR"
print("MUSIQUES :", len(music_files), "| VOIX :", len(voice_files), "| EFFETS :", len(effects_files))

print("")
print("MODE AUDIO")
print("1 = une musique")
print("2 = deux musiques")
print("3 = plusieurs musiques")
print("4 = musique + voix")
print("5 = musique + voix + effets")
mode = input("Choisissez le mode audio (1-5) : ").strip()

if mode not in ("1", "2", "3", "4", "5"):
    mode = "3"
    print("Choix invalide → mode 3 sélectionné")

if mode in ("4", "5") and not voice_files:
    print("Aucune voix disponible → retour au mode 3")
    mode = "3"

if mode == "5" and not effects_files:
    print("Aucun effet disponible → mode 4 sélectionné")
    mode = "4"
date = datetime.now().strftime("%Y-%m-%d")
number = 1
while os.path.exists(os.path.join(output_dir, f"video_{date}_{number:03d}.mp4")):
    number += 1
output = os.path.join(output_dir, f"video_{date}_{number:03d}.mp4")

logo = ImageClip(image).with_duration(6)
logo = logo.resized(lambda t: 0.65 + (0.025 if style == "PREMIUM" else 0.10 if style == "DYNAMIQUE" else 0.06) * t)
logo = logo.with_position(lambda t: ("center", 180 - (30 if style == "PREMIUM" else 80 if style == "DYNAMIQUE" else 45) * min(t / 1.5, 1)))

from PIL import Image, ImageDraw, ImageFont

text_img = Image.new("RGBA", (800, 120), (0, 0, 0, 0))
draw = ImageDraw.Draw(text_img)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 50)
bbox = draw.textbbox((0, 0), "DAR GHIZLANE", font=font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
draw.text(((800 - tw) / 2, (120 - th) / 2 - bbox[1]), "DAR GHIZLANE", font=font, fill="white")

text_path = "/tmp/dar_ghizlane_text.png"
text_img.save(text_path)

text = ImageClip(text_path).with_duration(6)
text = text.with_position(lambda t: ("center", 500 - (40 if style == "PREMIUM" else 120 if style == "DYNAMIQUE" else 65) * min(t / 1.5, 1)))

audio_clips = []
audio_sources = []

if mode == "1":
    selected_audio = random.choice(music_files)
    print("MUSIQUE PRINCIPALE :", selected_audio.split("/")[-1])

    audio_full = AudioFileClip(selected_audio)
    max_start = max(0, audio_full.duration - 6)
    start = random.uniform(0, max_start)
    print("DÉBUT MUSIQUE :", round(start, 2), "s")

    audio = audio_full.subclipped(start, min(start + 6, audio_full.duration)).with_volume_scaled(0.70)
    audio_clips.append(audio)
    audio_sources.append(audio_full)

elif mode == "2":
    selected_audio = random.choice(music_files)
    other_music = [f for f in music_files if f != selected_audio]

    if other_music:
        second_audio_path = random.choice(other_music)
    else:
        second_audio_path = selected_audio

    print("MUSIQUE 1 :", selected_audio.split("/")[-1])
    print("MUSIQUE 2 :", second_audio_path.split("/")[-1])

    audio_full = AudioFileClip(selected_audio)
    second_full = AudioFileClip(second_audio_path)

    max_start = max(0, audio_full.duration - 4.5)
    start = random.uniform(0, max_start)
    print("DÉBUT MUSIQUE 1 :", round(start, 2), "s")

    audio = audio_full.subclipped(start, min(start + 4.5, audio_full.duration)).with_volume_scaled(0.65)
    second_audio = second_full.subclipped(0, min(1.5, second_full.duration)).with_volume_scaled(0.35).with_start(4.5)

    audio_clips.extend([audio, second_audio])
    audio_sources.extend([audio_full, second_full])

elif mode == "3":
    selected_audio = random.choice(music_files)
    print("MUSIQUE PRINCIPALE :", selected_audio.split("/")[-1])

    other_audio = [f for f in music_files if f != selected_audio]
    random.shuffle(other_audio)

    intro_audio_path = other_audio[0]
    transition_audio_path = other_audio[1]
    final_audio_path = other_audio[2]

    audio_full = AudioFileClip(selected_audio)
    max_start = max(0, audio_full.duration - 6)
    start = random.uniform(0, max_start)
    print("DÉBUT MUSIQUE :", round(start, 2), "s")

    audio = audio_full.subclipped(start, min(start + 6, audio_full.duration)).with_volume_scaled(0.70)

    intro_full = AudioFileClip(intro_audio_path)
    intro_audio = intro_full.subclipped(0, min(1.5, intro_full.duration)).with_volume_scaled(0.35).with_start(0)

    transition_full = AudioFileClip(transition_audio_path)
    transition_audio = transition_full.subclipped(0, min(1.0, transition_full.duration)).with_volume_scaled(0.25).with_start(3)

    final_full = AudioFileClip(final_audio_path)
    final_audio = final_full.subclipped(0, min(1.5, final_full.duration)).with_volume_scaled(0.30).with_start(4.5)

    print("SON INTRO :", intro_audio_path.split("/")[-1])
    print("SON TRANSITION :", transition_audio_path.split("/")[-1])
    print("SON FINAL :", final_audio_path.split("/")[-1])

    audio_clips.extend([audio, intro_audio, transition_audio, final_audio])
    audio_sources.extend([audio_full, intro_full, transition_full, final_full])

elif mode == "4":
    selected_audio = random.choice(music_files)
    voice_path = random.choice(voice_files)

    print("MUSIQUE :", selected_audio.split("/")[-1])
    print("VOIX :", voice_path.split("/")[-1])

    audio_full = AudioFileClip(selected_audio)
    voice_full = AudioFileClip(voice_path)

    max_start = max(0, audio_full.duration - 6)
    start = random.uniform(0, max_start)
    print("DÉBUT MUSIQUE :", round(start, 2), "s")

    audio = audio_full.subclipped(start, min(start + 6, audio_full.duration)).with_volume_scaled(0.55)
    voice_audio = voice_full.subclipped(0, min(6, voice_full.duration)).with_volume_scaled(1.0).with_start(0)

    audio_clips.extend([audio, voice_audio])
    audio_sources.extend([audio_full, voice_full])

elif mode == "5":
    selected_audio = random.choice(music_files)
    voice_path = random.choice(voice_files)
    effect_path = random.choice(effects_files)

    print("MUSIQUE :", selected_audio.split("/")[-1])
    print("VOIX :", voice_path.split("/")[-1])
    print("EFFET :", effect_path.split("/")[-1])

    audio_full = AudioFileClip(selected_audio)
    voice_full = AudioFileClip(voice_path)
    effect_full = AudioFileClip(effect_path)

    max_start = max(0, audio_full.duration - 6)
    start = random.uniform(0, max_start)
    print("DÉBUT MUSIQUE :", round(start, 2), "s")

    audio = audio_full.subclipped(start, min(start + 6, audio_full.duration)).with_volume_scaled(0.50)
    voice_audio = voice_full.subclipped(0, min(6, voice_full.duration)).with_volume_scaled(1.0).with_start(0)
    effect_audio = effect_full.subclipped(0, min(2, effect_full.duration)).with_volume_scaled(0.40).with_start(3)

    audio_clips.extend([audio, voice_audio, effect_audio])
    audio_sources.extend([audio_full, voice_full, effect_full])

mixed_audio = CompositeAudioClip(audio_clips)

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
for source in audio_sources:
    source.close()

print("DAR GHIZLANE AD OK")
