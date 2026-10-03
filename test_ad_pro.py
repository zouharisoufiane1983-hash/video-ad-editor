import os
from datetime import datetime
from moviepy import ImageClip, TextClip, CompositeVideoClip, vfx

image = "/home/szouhari/video-ad-editor/assets/images/dar_ghizlane_logo.png"
output_dir = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR"
date = datetime.now().strftime("%Y-%m-%d")
number = 1
while os.path.exists(os.path.join(output_dir, f"video_{date}_{number:03d}.mp4")):
    number += 1
output = os.path.join(output_dir, f"video_{date}_{number:03d}.mp4")

logo = ImageClip(image).with_duration(6)
logo = logo.resized(lambda t: 0.65 + 0.06 * t)
logo = logo.with_position(("center", 180))
logo = logo.with_effects([vfx.CrossFadeIn(1.5)])

text = TextClip(
    text="DAR GHIZLANE",
    font="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    font_size=70,
    color="white"
).with_duration(6)

text = text.with_position(lambda t: ("center", 500 - 80 * min(t / 1.5, 1)))

video = CompositeVideoClip(
    [logo, text],
    size=(1280, 720)
)

video.write_videofile(
    output,
    fps=24,
    codec="libx264",
    audio=False
)

print("DAR GHIZLANE AD OK")
