from moviepy import ImageClip

image = "/home/szouhari/video-ad-editor/assets/images/dar_ghizlane_logo.png"
output = "/mnt/c/Users/HP/Desktop/VIDEO-AD-EDITOR/dar_ghizlane_test.mp4"

video = ImageClip(image).with_duration(5)
video = video.resized(height=720)

video.write_videofile(
    output,
    fps=24,
    codec="libx264",
    audio=False
)

print("IMAGE VIDEO OK")
