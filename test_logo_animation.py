from moviepy import ImageClip

image = "/home/szouhari/video-ad-editor/assets/images/dar_ghizlane_logo.png"
output = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR/dar_ghizlane_animation.mp4"

video = ImageClip(image).with_duration(5)

video = video.resized(lambda t: 0.75 + 0.10 * t)

video = video.with_position("center")

video.write_videofile(
    output,
    fps=24,
    codec="libx264",
    audio=False
)

print("LOGO ANIMATION OK")
