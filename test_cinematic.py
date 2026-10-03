from moviepy import ImageClip

image = "/home/szouhari/video-ad-editor/assets/images/dar_ghizlane_logo.png"
output = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR/dar_ghizlane_cinematic.mp4"

video = ImageClip(image).with_duration(6)

video = video.resized(lambda t: 0.70 + 0.08 * t)

video = video.with_position("center")

video.write_videofile(
    output,
    fps=24,
    codec="libx264",
    audio=False
)

print("CINEMATIC LOGO OK")
