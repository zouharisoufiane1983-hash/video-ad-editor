from moviepy import ImageClip, TextClip, CompositeVideoClip

image = "/home/szouhari/video-ad-editor/assets/images/dar_ghizlane_logo.png"
output = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR/dar_ghizlane_ad.mp4"

logo = ImageClip(image).with_duration(6)
logo = logo.resized(lambda t: 0.65 + 0.06 * t)
logo = logo.with_position(("center", 180))

text = TextClip(
    text="DAR GHIZLANE",
    font="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    font_size=70,
    color="white"
).with_duration(6)

text = text.with_position(lambda t: ("center", 570 - 80 * min(t / 1.5, 1)))

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
